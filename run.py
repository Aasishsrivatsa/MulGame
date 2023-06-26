import webview
import multiprocessing
from MathMania import Server

def start_server():
    server = Server()
    server.app.run(port=5321, debug=False, threaded=True)

def start_app():    
    webview.create_window('MathMania', 'http://localhost:5321/')
    webview.start()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    multiprocessing.Process(target=start_server).start()
    multiprocessing.Process(target=start_app).start()