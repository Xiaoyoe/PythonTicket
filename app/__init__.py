from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config

# 初始化数据库连接
db = SQLAlchemy()
# 初始化序列化工具
ma = Marshmallow()



# 应用工厂函数，创建Flask应用实例
def create_app(config_class=Config):
    app = Flask(__name__)  # 创建Flask应用
    app.config.from_object(config_class)  # 加载配置

    # 初始化扩展（绑定到Flask应用）
    db.init_app(app)
    ma.init_app(app)

    # 注册蓝图（模块化路由）
    from app.auth import auth_bp
    from app.users import users_bp
    from app.test import test_bp
    from app.tickets import tickets_bp
    from app.stuffs import  stuffs_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(test_bp, url_prefix='/test')
    app.register_blueprint(tickets_bp, url_prefix='/tickets')
    app.register_blueprint(stuffs_bp, url_prefix='/stuffs')

    return app