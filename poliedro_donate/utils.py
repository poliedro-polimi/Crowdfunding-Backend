from poliedro_donate import app


def get_base_url():
    return (app.config["APP_SSL"] and "https://" or "http://") + \
           app.config["APP_DOMAIN"] + app.config["APP_WEB_ROOT"]