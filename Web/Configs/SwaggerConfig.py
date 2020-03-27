from flask_swagger_ui import get_swaggerui_blueprint


def setup_swagger(swagger_url, api_url):
    # Call factory function to create our blueprint
    swagger_ui_blueprint = get_swaggerui_blueprint(
        swagger_url,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        api_url,
        config=
        {
            # Swagger UI config overrides
            'app_name': "Todo Flask application"
        },
    )
    return swagger_ui_blueprint

