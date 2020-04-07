from os import path
from flask import make_response, jsonify, Blueprint
from functools import wraps
from werkzeug.routing import parse_rule
import json


class SwaggerDist:
	instance = None

	class __Data:
		def __init__(self):
			pth = path.dirname(path.abspath(__file__))
			with open(path.join(pth, 'index.html'), 'r') as f:
				self.file_index = f.read()
			with open(path.join(pth, 'swagger-ui.css'), 'r') as f:
				self.file_css = f.read()
			with open(path.join(pth, 'swagger-ui-bundle.js'), 'r') as f:
				self.file_bundle = f.read()
			with open(path.join(pth, 'swagger-ui-standalone-preset.js'), 'r') as f:
				self.file_standalone = f.read()

	def __new__(cls):
		if not SwaggerDist.instance:
			SwaggerDist.instance = SwaggerDist.__Data()
		return SwaggerDist.instance


class Swagger(Blueprint):
	def __init__(self, name):
		Blueprint.__init__(self, name, __name__)
		self.m_routes = []
		self.url_prefix = ''
		self.tags = []

		@self.route('/swagger/index.html')
		def serve_html():
			a = SwaggerDist().file_index
			a = a.replace('{{ APP_NAME }}', name)
			response = make_response(a)
			response.headers['content-type'] = 'text/html;charset=utf-8'
			response.status_code = 200
			return response

		@self.route('/swagger/swagger-ui.css')
		def serve_css():
			response = make_response(SwaggerDist().file_css)
			response.headers['content-type'] = 'text/css'
			response.status_code = 200
			return response

		@self.route('/swagger/swagger-ui-bundle.js')
		def serve_bundle():
			response = make_response(SwaggerDist().file_bundle)
			response.headers['content-type'] = 'application/javascript'
			response.status_code = 200
			return response

		@self.route('/swagger/swagger-ui-standalone-preset.js')
		def serve_standalone():
			response = make_response(SwaggerDist().file_standalone)
			response.headers['content-type'] = 'application/javascript'
			response.status_code = 200
			return response

		@self.route('/swagger/swagger.json')
		def serve_schema():
			paths = {}
			for item in self.m_routes:
				if len(item['methods']) > 0:
					rule = str(item['rule'])
					parameters = []
					if item['body']:
						parameters.append(item['body'])
					done = ''
					for converter, arguments, variable in parse_rule(rule):
						if not converter:
							done += variable
						else:
							done += '{' + variable + '}'
							typ = ''
							if converter == 'int':
								typ = 'number'
							if converter == 'default' or converter == 'string' or converter == 'path':
								typ = 'string'
							if converter == 'float':
								typ = 'number'
							parameters.append({
								'name': variable,
								"in": "path",
								"required": True,
								"type": typ,
							})
					dummy = paths[done] = {}
					for method in item['methods']:
						dummy[method] = {
							'summary': item['summary'],
							'consumes': [item['consumes']],
							'produces': [item['produces']],
							'parameters': parameters,
							'security': item['security'],
							'tags': item['tags'],
							"responses": {
								"200": {
									"description": "successful operation",
								}
							},
						}
			return jsonify({
				"openapi": "3.0.0",
				"servers": [{
					'url': self.url_prefix,
				}],
				"paths": paths,
				"tags": [{'name': a} for a in self.tags],
				"components": {
					"securitySchemes": {
						"bearerAuth": {
							"type": "http",
							"scheme": "bearer",
							"bearerFormat": "JWT"
						}
					}
				}
			})

	def register_blueprint(self, parent, url_prefix=None):
		self.url_prefix = url_prefix
		parent.register_blueprint(self, url_prefix=url_prefix)

	def validated(self, **schema):
		def decorator(f):
			@wraps(f)
			def override(*args, **kwargs):
				pass
				# kwargs['data'] = from_request(**schema)
				return f(*args, **kwargs)

			return override

		return decorator

	def route(
		self,
		rule,
		summary='',
		consumes='application/json',
		produces='application/json',
		tags=None,
		validations=None,
		authorize=False,
		party_type=None,
		soft_check=None,
		**options
	):
		"""Like :meth:`Flask.route` but for a blueprint.  The endpoint for the
		:func:`url_for` function is prefixed with the name of the blueprint.
		"""
		have = False
		body = {}
		vals = {}
		desc = {}
		if validations:
			for key, v in validations.items():
				value = ''
				if '#' in v:
					spl = str(v).split('#')
					vals[key] = spl[0].strip(' ')
					desc[key] = [spl[0].strip(' '), spl[1].strip(' ')]
				else:
					value = v
					vals[key] = v
					desc[key] = [v]

				have = True
				body[key] = {
					'type': 'string',
				}
				if 'float' in value or 'int' in value:
					body[key] = {
						"type": 'number',
					}
				elif 'bool' in value:
					body[key] = {
						"type": 'boolean',
					}
				elif 'object' in value or 'dict' in value:
					body[key] = {
						"type": 'object',
					}
				elif 'array' in value or 'list' in value:
					body[key] = {
						"type": 'array',
						"items": {
							'type': 'string',
						}
					}
		if tags:
			if isinstance(tags, list):
				self.tags.extend(tags)
			else:
				self.tags.append(tags)
				tags = [tags]

		def define_rule(r):
			self.m_routes.append({
				'rule': r,
				'methods': options.get('methods', []),
				'summary': summary,
				'consumes': consumes,
				'produces': produces,
				'tags': tags,
				'security': [{"bearerAuth": []}] if authorize else [],
				'body': {
					'in': 'body',
					'name': 'body',
					'required': True,
					'description': f'<pre class="body-param__example microlight description">{json.dumps(desc, indent=2, sort_keys=True)}</pre>',
					'schema': {
						'type': 'object',
						'properties': body,
					}
				} if have else None,
			})

		if isinstance(rule, list):
			for r in rule:
				define_rule(r)
		else:
			define_rule(rule)

		def decorator(f):

			@wraps(f)
			def override(*args, **kwargs):
				if authorize:
					pass
					# raw_auth(dict(party_type=party_type, soft_check=soft_check), kwargs)
				if validations:
					pass
					# kwargs['data'] = from_request(**vals)
				return f(*args, **kwargs)

			if isinstance(rule, list):
				copy = override
				for r in rule:
					copy = Blueprint.route(self, r, **options)(copy)
				return copy
			else:
				return Blueprint.route(self, rule, **options)(override)

		return decorator
