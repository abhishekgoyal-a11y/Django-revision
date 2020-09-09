import requests

########################################DELETE BLOG####################################################

# r = requests.delete("http://127.0.0.1:8000/api/delete_blog/abhishek1t")

########################################GET BLOG####################################################

# r = requests.get("http://127.0.0.1:8000/api/get_blog_api/b7e20b32fdd67855915b6880db6919f8f85fd301")

########################################CREATE BLOG####################################################

# data={
#         "title": "abhishekgomyal",
#         "description": ";lfvaks;ld/as",
#         "posted_date": "2020-09-06",
#         "last_updated": "14:56:02.125643",
#         "author": 1
#     }
# r = requests.post("http://127.0.0.1:8000/api/create_blog/",data=data)

########################################UPDATE BLOG####################################################

# data={
#         "title": "abhishekgomyaluodate",
#         "description": ";lfvaks;ld/as",
#         "posted_date": "2020-09-06",
#         "last_updated": "14:56:02.125643",
#         "author": 1
#     }
# r = requests.put("http://127.0.0.1:8000/api/put_blog/abhishekgomyal",data=data)

########################################CREATE ACCOUNT####################################################

# data = {
# "username":"alert1",
# "email":"alert@gmail.com",
# "password":"abhi@1234"
# }
# r = requests.post("http://127.0.0.1:8000/api/registration_api/",data=data)


########################################GET API####################################################

# data = {
# "username":"user",
# "password":"abhi@1234"
# }
# r = requests.post("http://127.0.0.1:8000/api/get_api/",data=data)

print(r.text)
