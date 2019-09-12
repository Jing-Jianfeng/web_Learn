def templates(name):
    path="templates/"+ name
    with open(path,"r",encoding="utf-8") as file:
        return file.read()

def currentuser(request):
    print("start :\r\n")
    print("--------------",request.get_cookies())
    return ""

def route_msg(request):
    headers="HTTP/1.1 210 VERY OK\r\nContent-type:Text/html\r\n"
    body=templates('html_basic.html')
    r=headers+"\r\n"+body
    return r.encode("utf-8","ignore")


def route_register(request):
    headers="HTTP/1.1 210 VERY OK\r\nContent-type:Text/html\r\n"
    body=templates('register.html')
    r=headers+"\r\n"+body
    return r.encode("utf-8","ignore")

def route_login(request):
    headers="HTTP/1.1 210 VERY OK\r\nContent-type:Text/html\r\n"
    body=templates('login.html')
    r=headers+"\r\n"+body
    return r.encode("utf-8","ignore")




def route_static(request):
    path=request.path.strip("/")+"/"+request.query.get("file")
    with open(path,"rb") as pic:
        header=b'HTTP/1.x 200 OK \r\n Content-Type:image/gif\r\n\r\n'
        return header+pic.read()


def route_index(request):
    headers="HTTP/1.1 210 VERY OK\r\nContent-type:Text/html\r\n"
    body=templates('index.html')
    username=currentuser(request)
    body=body.replace("{{username}}",username)
    r=headers+"\r\n"+body
    return r.encode("utf-8","ignore")

route_dict={
    "/":route_index,
    "/login":route_login,
    "/register":route_register,
    "/msg":route_msg,
}