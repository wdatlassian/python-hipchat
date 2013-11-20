from configobj import ConfigObj

api_server = 0
api_url = 0
api_version = 0
proxy_server = 0
proxy_type = 0
token = 0

def init_cfg(config_fname):
    cfg = ConfigObj(config_fname)
    print "Using configuration file: %s" % config_fname
    global api_server, api_url, api_version, proxy_server, proxy_type, token
    try:
        token = cfg['token']
    except KeyError:
        return
    if len(token) == 40:
        api_version = 2
    else:
        api_version = 1
    api_server = cfg.get('api_server', 'api.hipchat.com')
    api_url = "https://%s/v%i/" % (api_server, api_version)
    proxy_server = cfg.get('proxy_server', 0)
    proxy_type = cfg.get('proxy_type', 0)
