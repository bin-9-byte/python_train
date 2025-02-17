def http_error(status):
    match status:
        case 400:
            return "bad request"
        case 404:
            return "not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "something's wrong with the internet"

mystatus = 400
print(http_error(400))