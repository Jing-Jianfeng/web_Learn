import socket
from urllib.parse import unquote
from homework.routes import *

class Request():
    def __init__(self):
        self.method="GET"
        self.path=""
        self.query={}
        self.body=""
        self.headers={}
        self.cookies={}

    def form(self):
        body=unquote(self.body)
        args=body.split('&')
        f={}
        for arg in args:
            k,v=arg.split("=")
            f[k]=v
        return f

    def get_cookies(self):
        cookies_str=self.body.split("\r\n")[-3].replace("Cookie: ","")
        cookies_list=cookies_str.split("; ")
        cookies={}
        for cookie in cookies_list:
            k , v=cookie.split("=")
            cookies[k]=v
        return cookies
request=Request()

def log(*args, **kwargs):
    print("log", *args, **kwargs)

def parsed_path(path):
    if path.find("?") == -1:
        return path,{}
    else:
        path,query_str=path.split("?",1)
        querys=query_str.split("&")
        query={}
        for arg in querys:
            k,v=arg.split("=")
            query[k]=v
        return path,query


def error(request,code=404):
    e={
        404:b'HTTP/1.x 404 NOT FOUND\r\n\r\n<h1>NOT FOUND</h1>'
    }
    return e.get(code,b'')


def response_for_path(path):
    path,query=parsed_path(path)
    request.path=path
    request.query=query
    route_dir={
        "/static":route_static,
       # "/": route_index,
    }
    route_dir.update(route_dict)
    response=route_dir.get(path,error)
    return response(request)

def run(**kwargs):
    # 启动服务器
    host, port = kwargs.get("host"), kwargs.get("port")
    log("start server")
    with socket.socket() as s:
        s.bind((host, port))
        while True:
            s.listen(3)
            connection, address = s.accept()
            revive = ""
            while True:
                r = connection.recv(1000).decode("utf-8")
                revive += r
                if len(r) < 1000:
                    break

            if len(revive.split())<2:
                continue
            path=revive.split()[1]
            request.method=revive.split()[0]
            request.path=path
            request.body=revive.split("\r\n",1)[1]
            log(revive)
            log("request.body",request.body)
            response=response_for_path(path)
            connection.sendall(response)
            connection.close()
def main():
    config = dict(
        host="localhost",
        port=3000,
    )
    run(**config)


if __name__ == "__main__":
    main()
