import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.common import config


def get_ga_id():
    ga_id = config.get('ckanext-google_analytics.id', '')
    return ga_id

def get_src():
    ga_id = get_ga_id()
    src = "https://www.googletagmanager.com/gtag/js?id=%s" % (ga_id)
    return src

class Google_AnalyticsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    # Declare that this plugin will implement ITemplateHelpers.
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'google_analytics')



    def get_helpers(self):
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'google_analytics_ga_id': get_ga_id,
                'google_analytics_src': get_src,
                }
