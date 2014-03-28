from pywb.framework.wsgi_wrappers import init_app, start_wsgi_server

from pywb.core.cdx_api_handler import create_cdx_server_app

#=================================================================
# init cdx server app
#=================================================================

# cdx-server only config
DEFAULT_CONFIG = 'configs/cdx-server-config.yaml'

application = init_app(create_cdx_server_app,
                       load_yaml=True,
                       config_file=DEFAULT_CONFIG)


def main():
    start_wsgi_server(application, 'CDX Server')

if __name__ == "__main__":
    main()