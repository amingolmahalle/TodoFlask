from flask import request
import json
import Utils.Regex as regex

_rules = dict()


class Object:
    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__)


class ValidationFailedException(Exception):
    def __init__(self, message: str, validation: dict):
        Exception.__init__(self)
        self.message = message
        self.status_code = 400
        self.validation = validation

    def __str__(self):
        return self.message


class Context:
    key: str
    value: any
    args: list
    message: str


def _lexer_rule(rule, fn):
    scope_block = 0
    cut = 0
    in_block = False
    before = ' '
    ln = len(rule)
    param_start = 0
    arg_start = 0
    have_arguments = False
    args = list()

    i = 0
    for c in rule:
        if before != '\\':
            if c == '(':
                if scope_block == 0:
                    have_arguments = True
                    param_start = i
                    arg_start = i + 1
                    in_block = True
                scope_block += 1
            elif c == ')':
                scope_block -= 1
                if scope_block == 0:
                    args.append(_remove_slashes(rule[arg_start:i]))
                    arg_start = i
                    in_block = False
                    name = rule[cut - 1:param_start]
                    if not fn(name, args):
                        return
                    args = list()
            elif c == ',' and in_block:
                args.append(_remove_slashes(rule[arg_start:i]))
                arg_start = i + 1
        if not in_block:
            if before != ' ':
                if c == ' ' or i == ln - 1:
                    begin = cut - 1
                    if i == ln - 1:
                        cut = ln + 1
                    else:
                        cut = i + 1
                    if not have_arguments:
                        name = rule[begin:cut - 1]
                        if not fn(name, list()):
                            return
                    have_arguments = False
            else:
                cut += 1
        before = c
        i += 1


def _remove_slashes(val: str):
    return val.replace('\\)', ')').replace('\\(', '(').replace('\\,', ',').strip()


def register_rule(name: str, fn):
    global _rules
    _rules[name] = fn


def register_builtin_validators():

    def to_be_required(ctx: Context):
        if ctx.value is None:
            ctx.message = f'پر کردن این فیلد الزامی است.'

    def to_be_an_array(ctx: Context):
        if ctx.value is not None:
            if not isinstance(ctx.value, list):
                ctx.message = f'باید یک آرایه باشد.'

    def to_be_an_object(ctx: Context):
        if ctx.value is not None:
            if not isinstance(ctx.value, dict):
                ctx.message = f'باید یک دیکشنری باشد.'

    def to_be_a_string(ctx: Context):
        if ctx.value is not None:
            if not isinstance(ctx.value, str):
                ctx.message = f'باید یک رشته باشد.'

    def to_be_a_datetime(ctx: Context):
        if ctx.value is not None:
            if not regex.check_date_time_format(str(ctx.value)):
                ctx.message = f'باید یک تاریخ معتبر باشد.'

    def to_be_a_mobile_number(ctx: Context):
        if ctx.value is not None:
            if not regex.check_mobile_format(str(ctx.value)):
                ctx.message = f'باید یک شماره همراه معتبر باشد.'

    def to_be_a_phone_number(ctx: Context):
        if ctx.value is not None:
            if not regex.check_phone_format(str(ctx.value)):
                ctx.message = f'باید یک شماره تلفن معتبر باشد.'

    def to_be_in_alpha(ctx: Context):
        if ctx.value is not None:
            if not regex.check_alpha_format(str(ctx.value)):
                ctx.message = f'باید شامل حروف انگلیسی باشد.'

    def to_be_in_alpha_num(ctx: Context):
        if ctx.value is not None:
            if not regex.check_alpha_numeric_format(str(ctx.value)):
                ctx.message = f'باید شامل حروف انگلیسی و اعداد باشد.'

    def to_be_in_numeric(ctx: Context):
        if ctx.value is not None:
            if not isinstance(ctx.value, str) or not regex.check_numeric_format(ctx.value):
                ctx.message = f'باید شامل اعداد باشد.'
                return

    def to_be_a_float(ctx: Context):
        if ctx.value is not None:
            if not (isinstance(ctx.value, float) or isinstance(ctx.value, int)):
                ctx.message = f'باید شامل اعداد باشد.'
                return
            ctx.value = float(ctx.value)

    def to_be_a_integer(ctx: Context):
        if ctx.value is not None:
            if not (isinstance(ctx.value, float) or isinstance(ctx.value, int)):
                ctx.message = f'باید شامل اعداد باشد.'
                return
            ctx.value = int(ctx.value)

    def to_be_in_alpha_dash(ctx: Context):
        if ctx.value is not None:
            if not regex.check_alpha_dash_format(str(ctx.value)):
                ctx.message = f'باید شامل حروف انگلیسی و اعداد و خط تیره باشد.'

    def to_be_a_username(ctx: Context):
        if ctx.value is not None:
            if not regex.check_username_format(str(ctx.value)):
                ctx.message = f'باید یک نام کاربری معتبر باشد.'

    def to_be_an_email(ctx: Context):
        if ctx.value is not None:
            if not regex.check_email(str(ctx.value)):
                ctx.message = f'باید یک پست الکترونیک معتبر باشد.'

    def to_be_a_boolean(ctx: Context):
        if ctx.value is not None:
            if not isinstance(ctx.value, bool):
                ctx.message = f'باید true یا false باشد.'

    def to_be_a_national_code(ctx: Context):
        if ctx.value is not None:
            msg = f'باید یک شماره ملی معتبر باشد.'
            if not isinstance(ctx.value, str) or not regex.check_numeric_format(ctx.value) or len(ctx.value) != 10:
                ctx.message = msg
                return

            check = int(str(ctx.value[9]))
            sum = 0
            for i in range(9):
                sum += int(str(ctx.value[i])) * (10 - i)
            sum %= 11
            if not ((2 > sum == check) or (sum >= 2 and check + sum == 11)):
                ctx.message = msg
                return

    def to_have_length(ctx: Context):
        if ctx.value is not None:
            ln = int(ctx.args[0])
            if not isinstance(ctx.value, str) or len(ctx.value) != ln:
                ctx.message = f'باید {ln} حرف باشد.'

    def to_be_in(ctx: Context):
        if ctx.value is not None:
            if isinstance(ctx.value, str):
                if ctx.value not in ctx.args:
                    ctx.message = f'باید یکی از {"، ".join(ctx.args)} باشد.'
            elif isinstance(ctx.value, int):
                if ctx.value not in [int(a) for a in ctx.args]:
                    ctx.message = f'باید یکی از {"، ".join(ctx.args)} باشد.'
            elif isinstance(ctx.value, float):
                if ctx.value not in [float(a) for a in ctx.args]:
                    ctx.message = f'باید یکی از {"، ".join(ctx.args)} باشد.'

    def to_be_minimum(ctx: Context):
        if ctx.value is not None:
            ln = float(ctx.args[0])
            if isinstance(ctx.value, str):
                if len(ctx.value) < ln:
                    ctx.message = f'باید حداقل {int(ln)} حرف باشد.'
            elif isinstance(ctx.value, int) or isinstance(ctx.value, float):
                if ctx.value < ln:
                    ctx.message = f'باید حداقل {ln} باشد.'

    def to_be_maximum(ctx: Context):
        if ctx.value is not None:
            ln = float(ctx.args[0])
            if isinstance(ctx.value, str):
                if len(ctx.value) > ln:
                    ctx.message = f'باید حداکثر {int(ln)} حرف باشد.'
            elif isinstance(ctx.value, int) or isinstance(ctx.value, float):
                if ctx.value > ln:
                    ctx.message = f'باید حداکثر {ln} باشد.'

    register_rule('required', to_be_required)
    register_rule('string', to_be_a_string)
    register_rule('datetime', to_be_a_datetime)
    register_rule('array', to_be_an_array)
    register_rule('list', to_be_an_array)
    register_rule('object', to_be_an_object)
    register_rule('dict', to_be_an_object)
    register_rule('bool', to_be_a_boolean)
    register_rule('float', to_be_a_float)
    register_rule('int', to_be_a_integer)
    register_rule('mobile', to_be_a_mobile_number)
    register_rule('phone', to_be_a_phone_number)
    register_rule('nationalcode', to_be_a_national_code)
    register_rule('email', to_be_an_email)
    register_rule('username', to_be_a_username)
    register_rule('alpha_dash', to_be_in_alpha_dash)
    register_rule('alpha_num', to_be_in_alpha_num)
    register_rule('alpha', to_be_in_alpha)
    register_rule('numeric', to_be_in_numeric)
    register_rule('len', to_have_length)
    register_rule('min', to_be_minimum)
    register_rule('max', to_be_maximum)
    register_rule('in', to_be_in)


def from_request(**schema):
    global _rules
    errors = dict()
    data = dict()

    data.update(request.values.to_dict())

    if request.is_json:
        data.update(request.json)

    output = Object()
    raw = {}

    for key, rule in schema.items():
        value = data.get(key)

        if rule:
            context = Context()
            context.key = key
            context.value = value
            context.args = []
            context.message = None
            context.failed = False

            def check(command, args):
                context.args = args
                fn = _rules.get(command)

                if not fn:
                    raise ValidationFailedException(f'پیدا نشد: {command}', dict())

                fn(context)

                return not context.message

            _lexer_rule(rule, check)

            if not context.message:
                setattr(output, key, context.value)
                raw[key] = context.value
            else:
                errors[key] = context.message

    if len(errors) > 0:
        raise ValidationFailedException(f'مقادیر ارسالی اشتباه است.', errors)

    setattr(output, 'to_dict', raw)

    return output
