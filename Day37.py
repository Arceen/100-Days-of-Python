# api requests post, put and delete
import datetime
import requests

#creating an user
username = "randomdude"
pixela_endpoint = 'https://pixe.la/v1/users'
# parameters = {
#     "token": "thisissecret",
#     "username": username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# res = requests.post(pixela_endpoint, json=parameters)
# print(res.text)

pixela_graph_endpoint = pixela_endpoint+'/'+username+'/graphs'
graph_id= "cycling-graph"
req_header = {
    'X-USER-TOKEN':'thisissecret'
}
# req_body={
#     "id":"pushups-graph",
#     "name":"Pushups",
#     "unit":"pushups",
#     "type":"int",
#     "color":"kuro",
#     "isSecret": True,
#     "publishOptionalData": True
# }
# req_body={
#     "id":graph_id,
#     "name":"cycling",
#     "unit":"km",
#     "type":"float",
#     "color":"sora",
#     "isSecret": True,
#     "publishOptionalData": True
# }

# res = requests.post(pixela_graph_endpoint, json=req_body, headers=req_header)
# print(res.text)
# print(res)

d = datetime.datetime.now().strftime('%Y%m%d')


pixela_post_pixel_endpoint = pixela_endpoint+'/'+username+'/graphs/'+graph_id
post_pixel_req_body={
    "date": d,
    "quantity": "100",
}


# res = requests.post(pixela_post_pixel_endpoint, json=post_pixel_req_body, headers=req_header)
# print(res.text)
# print(res)

pixela_update_delete_pixel_endpoint = pixela_endpoint+'/'+username+'/graphs/'+graph_id+'/'+d
# update_pixel_req_body={
#     "date": d,
#     "quantity": "2",
# }

# #update request using put
# res = requests.put(pixela_update_delete_pixel_endpoint, json=update_pixel_req_body, headers=req_header)
# print(res.text)
# print(res)


#update request using put
res = requests.delete(pixela_update_delete_pixel_endpoint, headers=req_header)
print(res.text)
print(res)
