# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return '<p>Hello, World!<p>'



# from markupsafe import escape

# @app.route("/name")
# def hello(name):
#     return f"hello,{escape(name)}!"


# @app.route('/')
# def index():
#     return "Index Page"

# # 定义一个简单的hello函数，用于返回问候语
# def hello():
#     """返回'Hello, World'字符串作为简单的欢迎信息。"""
#     return "Hello, World"

# # 导入escape函数，用于转义HTML特殊字符，提高安全性
# from _markupbase import escape

# # 使用@app.route装饰器定义一个路由，该路由处理/user/后跟用户名的请求
# @app.route('/user/<username>')
# def show_user_profile(username):
#     """
#     根据提供的用户名展示用户个人主页。
#     参数:
#     - username: 用户名，动态从URL中获取，使用escape函数转义以确保安全。
#     """
#     return f'User {escape(username)}'

# # 定义一个路由，处理/post/后跟整数形式的帖子ID的请求
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     """
#     展示特定ID的帖子详情。
#     参数:
#     - post_id: 帖子的唯一ID，作为整数类型从URL中提取。
#     """
#     return f'Post {post_id}'

# # 定义一个路由，处理/path/后跟随任意子路径的请求
# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     """
#     显示跟在'/path/'后面的子路径，适用于处理多级或复杂路径结构。
#     参数:
#     - subpath: 任意子路径字符串，可以从URL中获取并安全地转义。
#     """
#     # 使用escape函数确保子路径中的特殊字符被安全转义后展示
#     return f'Subpath {escape(subpath)}'


# # 唯一的 URL / 重定向行为
# # 以下两条规则的不同之处在于是否使用尾部的斜杠。
# @app.route('/projects')

# def projects():
#     return 'The project page'


# @app.route('/about')
# def about():
#     return 'The about page'



from flask import url_for
app = Flask(__name__)

# 首页路由
@app.route('/')
def index():
    """
    首页路由函数
    
    参数: 无
    
    返回值: 返回字符串 'index'
    """
    return 'index'

# 登录路由
@app.route('/login')
def login():
    """
    登录路由函数
    
    参数: 无
    
    返回值: 返回字符串 'login'
    """
    return 'login'

# 用户个人资料路由
@app.route('/user/<username>')
def profile(username):
    """
    用户个人资料路由函数
    
    参数:
    - username: 用户名，字符串类型
    
    返回值: 返回格式化后的字符串，表示用户的个人资料页面
    """
    return f'{username}\'s profile'

# 使用测试请求上下文，测试生成的URL
with app.test_request_context():
    # 生成首页的URL
    print(url_for('index'))
    # 生成登录页面的URL
    print(url_for('login'))
    # 生成登录页面的URL，带next参数，用于登录后重定向
    print(url_for('login', next='/'))
    # 生成指定用户名的个人资料页面URL
    print(url_for('profile', username='John Doe'))





