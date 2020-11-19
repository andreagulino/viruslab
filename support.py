def setupMailConfig(app, CONF):
    app.config['MAIL_SERVER']='smtp.aol.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = CONF["mail_address"]
    app.config['MAIL_PASSWORD'] = CONF["mail_password"]
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True