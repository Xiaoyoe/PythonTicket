import os
from openai import OpenAI
from flask import Blueprint, request, jsonify

# 创建 AI 聊天蓝图，用于组织 AI 聊天相关的路由
ai_chat_bp = Blueprint('ai_chat', __name__)

# 初始化 OpenAI 客户端
client = OpenAI(
    # 从环境变量中获取 API Key，若未配置环境变量，可手动替换为具体的 API Key
    api_key=os.environ.get('DASHSCOPE_API_KEY'),
    # 设置基础 URL 为阿里云百炼的兼容模式地址
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

@ai_chat_bp.route('/chat', methods=['POST'])
def chat():
    """
    处理 AI 聊天请求的路由函数。
    接收客户端发送的用户消息，并调用 OpenAI 模型获取回复。
    """
    # 从请求中获取 JSON 数据
    data = request.get_json()
    # 检查请求数据是否存在以及是否包含 'message' 字段
    if not data or 'message' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Missing message'
        }), 400

    # 提取用户发送的消息
    user_message = data['message']

    try:
        # 调用 OpenAI 模型进行聊天完成
        completion = client.chat.completions.create(
            # 指定使用的模型，这里以 deepseek-r1 为例，可按需更换
            model="deepseek-r1",
            # 构建消息列表，包含用户的消息
            messages=[
                {
                    'role': 'user',
                    'content': user_message
                }
            ]
        )

        # 提取模型的思考过程
        reasoning_content = completion.choices[0].message.reasoning_content
        # 提取模型的最终答案
        answer = completion.choices[0].message.content.strip()

        # 返回包含思考过程和最终答案的响应
        return jsonify({
            'status': 'success',
            'reasoning': reasoning_content,
            'answer': answer
        }), 200

    except Exception as e:
        # 若发生异常，返回包含错误信息的响应
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500