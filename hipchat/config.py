from configobj import ConfigObj

token = 0
proxy_server = 0
proxy_type = 0

def init_cfg(config_fname):
    cfg = ConfigObj(config_fname)
    global api_server, api_url, api_version, token, proxy_type, proxy_server
    token = cfg['token']
    if token.length == 40:
        api_version = 2
    else:
        api_version = 1
    api_server = cfg.get('api_server', 'api.hipchat.com')
    api_url = "https://%s/v%i" % (api_server, api_version)
    proxy_server = cfg.get('proxy_server', 0)
    proxy_type = cfg.get('proxy_type', 0)
