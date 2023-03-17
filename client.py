import requests 

colors_url = 'http://127.0.0.1:5000/api/favorite_color'

# Example JSON to send to API server 
json_data = {'color': 'green'}

# response = requests.post(colors_url, json=json_data)
# print(response, response.status_code)

# Get all the favorite colors 

response = requests.get(colors_url)
print(response.text, response.status_code)


# Delete all the colors 

response = requests.delete('http://127.0.0.1:5000/admin/delete_all_colors')
print(response.text, response.status_code)
