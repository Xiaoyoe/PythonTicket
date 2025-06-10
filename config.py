import os


# 基础配置类
class Config:
    # 应用密钥，用于会话签名和其他安全操作
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'

    # 数据库连接URI，使用SQLite作为示例
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/db_ticket'

    # 禁用SQLAlchemy的修改跟踪，减少内存使用
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 是否开启调试模式（默认关闭，用于生产环境）
    DEBUG = False

    # AI API Key
    OPENAI_API_KEY = os.environ.get('DASHSCOPE_API_KEY')

# 开发环境配置
class DevelopmentConfig(Config):
    DEBUG = True  # 开启调试模式
    SQLALCHEMY_ECHO = True  # 显示SQL语句，便于调试


# 测试环境配置
class TestingConfig(Config):
    TESTING = True  # 开启测试模式
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # 使用内存数据库
    WTF_CSRF_ENABLED = False  # 禁用CSRF保护


# 生产环境配置
class ProductionConfig(Config):
    pass  # 使用基础配置，可根据需要扩展


# 配置映射字典，方便根据环境名称获取配置类
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig  # 默认使用开发环境配置
}