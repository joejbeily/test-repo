from flask import Flask
from keycloak_adapter.caching import sensitive_cache, public_cache
from keycloak_adapter.adapters.flask_adapter import FlaskPolicyEnforcerExtension, enforcer_proxy

app = Flask(__name__)
# Set KEYCLOAK_ADAPTER_CONFIG_FILE in the Flask config
# app.config['KEYCLOAK_ADAPTER_CONFIG_FILE'] = '/path/to/keycloak.json'

# Configure the cache in some way
sensitive_cache.configure('dogpile.cache.memory', expiration_time=300, replace_existing_backend=True)
public_cache.configure('dogpile.cache.redis', expiration_time=300, arguments=dict(url='redis://localhost:6379/0'), replace_existing_backend=True)

policy_enforcer = FlaskPolicyEnforcerExtension(app)
# If you are using a factory function for your app, you can use:
# policy_enforcer.init_app(app)

# Setup the other app routes, apis, etc.
@app.route('/')
@policy_enforcer.protected()
def view_index():
    # Read information about the user:
    # g.security_context.token will contain the parsed OAuth2 token
    # See the AccessTokenSchema class
    #
    # Make API calls to the Keycloak server through the enforcer_proxy:
    # enforcer_proxy.authz_client
    pass


app.run()