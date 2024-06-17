import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class HarbourPlugin(plugins.SingletonPlugin, toolkit.DefaultGroupForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IGroupForm, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "harbour")

    # IGroupForm
    def group_types(self):
        return ["subject_area"]
