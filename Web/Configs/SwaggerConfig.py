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
        # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
        #    'clientId': "your-client-id",my_db
        #    'clientSecret': "your-client-secret-if-required",
        #    'realm': "your-realms",
        #    'appName': "your-app-name",
        #    'scopeSeparator': " ",
        #    'additionalQueryStringParams': {'test': "hello"}
        # }
    )
    return swagger_ui_blueprint

