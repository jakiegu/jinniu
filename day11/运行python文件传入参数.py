import flask
import sys,time
server = flask.Flask(__name__)
@server.route('/')
def index():
    return 'ok'
if len(sys.argv)>1:
    port = sys.argv[1]
    if port.isdigit():
        server.run(port=port)
    elif port == '--help':
        print('这个文件的作用是运行flask案例')
    elif port == '--time':
        print(time.time())
    else:
        print('端口号必须是整数')

else:
    print('运行错误，请+端口号\n')
server.run(port=5000)

# sys.argv的作用是获取运行python文件时，传入的参数
# python xx.py --help
# 默认运行python文件时，不传参数，argv中只有一个元素
# 就这个python文件的文件名