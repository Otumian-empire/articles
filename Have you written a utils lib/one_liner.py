# def add_one(x: int):
#     return x + 1


# def add_two(x: int):
#     return add_one(add_one(x))


# print(add_one(12))  # -> 13
# print(add_two(12))  # -> 14

from http.client import HTTPSConnection as httpConn


class Validator:

    def is_existing_email(self, domain):
        """
        ping the domain's server to see if the domain exists
        using http.client and get a response of 200 OK
        """

        conn = httpConn(domain)
        print(conn.host)

        conn.request("HEAD", "/")
        res = conn.getresponse()
        print(res.status)

        return res.status == 200


print(Validator().is_existing_email("google.com"))
