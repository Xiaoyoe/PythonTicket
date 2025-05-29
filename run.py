from app import create_app

# 创建Flask应用实例（使用默认配置）
app = create_app()

# 主程序入口
if __name__ == '__main__':
    # 启动应用，debug=True表示开启调试模式
    app.run(debug=True)
