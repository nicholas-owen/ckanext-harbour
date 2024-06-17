import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


# import ckanext.harbour.cli as cli
# import ckanext.harbour.helpers as helpers
# import ckanext.harbour.views as views
# from ckanext.harbour.logic import (
#     action, auth, validators
# )


class HarbourPlugin(plugins.SingletonPlugin, toolkit.DefaultGroupForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IGroupForm, inherit=True)
    
    # plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    # plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    # plugins.implements(plugins.ITemplateHelpers)
    # plugins.implements(plugins.IValidators)
    

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "harbour")

    # IGroupForm
    def group_types(self):
        return ["subject_area"]

    # IAuthFunctions

    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    # def get_blueprint(self):
    #     return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers

    # def get_helpers(self):
    #     return helpers.get_helpers()

    # IValidators

    # def get_validators(self):
    #     return validators.get_validators()
    
