import requests
import json
from config import base_url, list_of_users
from pprint import pprint

# 1. Finds Pets by status
status = 'available'
res_get_by_status = requests.get(f'{base_url}/pet/findByStatus?status={status}',
                                 headers={'accept': 'application/json'})
print(f'1. {res_get_by_status.status_code} - статус-код Finds Pets by status')
if 'application/json' in res_get_by_status.headers['Content-Type']:  # Эта структура - из юнита 19.3
    print(f'Тело ответа:')
    print(res_get_by_status.json())
else:
    print(f'Тело ответа:')
    print(res_get_by_status.text)
print('---------------------------------------------------------------------------------------------------------------')

# 2. Add a new pet to the store
data_post_pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "dog"
  },
  "name": "Doggick",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res_post_pet = requests.post(f'{base_url}/pet', headers={'accept': 'application/json',
                             'Content-Type': 'application/json'}, data=json.dumps(data_post_pet, ensure_ascii=False))
print(f'2. {res_post_pet.status_code} - статус-код Add a new pet to the store')
if 'application/json' in res_post_pet.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_post_pet.json(), width=40, indent=10)  # А здесь уже с форматированием)
else:
    print(f'Тело ответа:')
    pprint(res_post_pet.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# Достаём из ответа petID, чтобы использовать его для следующих запросов
petId = res_post_pet.json()['id']

# 3. Find pet by ID
res_get_by_id = requests.get(f'{base_url}/pet/{petId}', headers={'accept': 'application/json'})
print(f'3. {res_get_by_id.status_code} - статус-код Find pet by ID')
if 'application/json' in res_get_by_id.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_get_by_id.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_get_by_id.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# 4. Updates a pet in the store with form data
post_upd_data = {'name': 'Doge', 'status': 'sold'}
res_post_upd_pet = requests.post(f'{base_url}/pet/{petId}', headers={'accept': 'application/json',
                                 'Content-Type': 'application/x-www-form-urlencoded'}, data=post_upd_data)
print(f'4. {res_post_upd_pet.status_code} - статус-код Updates a pet in the store with form data')
if 'application/json' in res_post_upd_pet.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_post_upd_pet.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_post_upd_pet.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# 5. Uploads an image
photo = 'doge.jpeg'
files = {'file': (photo, open(photo, 'rb'), 'image/jpeg')}
res_post_upload_img = requests.post(f'{base_url}/pet/{petId}/uploadImage', headers={'accept': 'application/json'},
                                    files=files)
print(f'5. {res_post_upload_img.status_code} - статус-код Uploads an image')
if 'application/json' in res_post_upload_img.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_post_upload_img.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_post_upload_img.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# 6. Update an existing pet
put_data = {
    "id": petId,
    "category": {
        "id": 0,
        "name": "cat"
    },
    "name": "Kittie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

res_put_upd_pet = requests.put(f'{base_url}/pet', headers={'accept': 'application/json',
                               'Content-Type': 'application/json'}, data=json.dumps(put_data, ensure_ascii=False))
print(f'6. {res_put_upd_pet.status_code} - статус-код Update an existing pet')
if 'application/json' in res_put_upd_pet.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_put_upd_pet.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_put_upd_pet.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# 7. Deletes a pet
res_del_pet = requests.delete(f'{base_url}/pet/{petId}', headers={'accept': 'application/json'})
print(f'7. {res_del_pet.status_code} - статус-код Deletes a pet')
if 'application/json' in res_del_pet.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_del_pet.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_del_pet.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# 8. Returns pet inventories by status
res_get_invent = requests.get(f'{base_url}/store/inventory', headers={'accept': 'application/json'})
print(f'8. {res_get_invent.status_code} - статус-код Returns pet inventories by status')
if 'application/json' in res_get_invent.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_get_invent.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_get_invent.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# 9. Place an order for a pet
order_data = {
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2023-01-19T12:02:05.357Z",
  "status": "placed",
  "complete": "true"
}
res_post_order = requests.post(f'{base_url}/store/order', headers={'accept': 'application/json',
                               'Content-Type': 'application/json'}, data=json.dumps(order_data, ensure_ascii=False))
print(f'9. {res_post_order.status_code} - статус-код Place an order for a pet')
if 'application/json' in res_post_order.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_post_order.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_post_order.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# 10. Find purchase order by ID
orderId = 2
res_get_order = requests.get(f'{base_url}/store/order/{orderId}', headers={'accept': 'application/json'})
print(f'10. {res_get_order.status_code} - статус-код Find purchase order by ID')
if res_get_order.status_code == 404:
    print(f'Кажется, кто-то удалил заказ с ID = {orderId}')
if 'application/json' in res_get_order.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_get_order.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_get_order.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# 11. Delete purchase order by ID
new_orderId = res_post_order.json()['id']
res_del_order = requests.delete(f'{base_url}/store/order/{new_orderId}', headers={'accept': 'application/json'})
print(f'11. {res_del_order.status_code} - статус-код Delete purchase order by ID')
if 'application/json' in res_del_order.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_del_order.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_del_order.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# 12. Create user
user_data = {
  "id": 0,
  "username": "Arsenij",
  "firstName": "Arsenij",
  "lastName": "Petrov",
  "email": "arseniy@mail.ru",
  "password": "string",
  "phone": "+782394",
  "userStatus": 0
}
res_post_user = requests.post(f'{base_url}/user', headers={'accept': 'application/json',
                              'Content-Type': 'application/json'}, data=json.dumps(user_data, ensure_ascii=False))
print(f'12. {res_post_user.status_code} - статус-код Create user')
if 'application/json' in res_post_user.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_post_user.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_post_user.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# 13. Creates list of users with given input array
res_post_with_array = requests.post(f'{base_url}/user/createWithArray', headers={'accept': 'application/json',
                                    'Content-Type': 'application/json'}, data=json.dumps(list_of_users,
                                    ensure_ascii=False))
print(f'13. {res_post_with_array.status_code} - статус-код Creates list of users with given input array')
if 'application/json' in res_post_with_array.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_post_with_array.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_post_with_array.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# 14. Creates list of users with given input list
res_post_with_list = requests.post(f'{base_url}/user/createWithList', headers={'accept': 'application/json',
                                   'Content-Type': 'application/json'}, data=json.dumps(list_of_users,
                                   ensure_ascii=False))
print(f'14. {res_post_with_list.status_code} - статус-код Creates list of users with given input list')
if 'application/json' in res_post_with_list.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_post_with_list.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_post_with_list.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# 15. Get user by user name
username = user_data['username']
res_get_user = requests.get(f'{base_url}/user/{username}', headers={'accept': 'application/json'})
print(f'15. {res_get_user.status_code} - статус-код Get user by user name')
if 'application/json' in res_get_user.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_get_user.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_get_user.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# 16. Updated user
put_user = {
  "id": 0,
  "username": "Arsenii",
  "firstName": "Arsenii",
  "lastName": "Petroff",
  "email": "arseniy@mail.ru",
  "password": "string",
  "phone": "+782394",
  "userStatus": 0
}

res_put_upd_user = requests.put(f'{base_url}/user/{username}', headers={'accept': 'application/json',
                                'Content-Type': 'application/json'}, data=json.dumps(put_user, ensure_ascii=False))
print(f'16. {res_put_upd_user.status_code} - статус-код Updated user')
if 'application/json' in res_put_upd_user.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_put_upd_user.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_put_upd_user.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# 17. Logs user into the system
new_username = put_user['username']
password = put_user['password']
res_get_login = requests.get(f'{base_url}/user/login?username={new_username}&password={password}',
                             headers={'accept': 'application/json'})
print(f'17. {res_get_login.status_code} - статус-код Logs user into the system')
if 'application/json' in res_get_login.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_get_login.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_get_login.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# 18. Logs out current logged in user session
res_get_logout = requests.get(f'{base_url}/user/logout', headers={'accept': 'application/json'})
print(f'18. {res_get_logout.status_code} - статус-код Logs out current logged in user session')
if 'application/json' in res_get_logout.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_get_logout.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_get_logout.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')

# 19. Delete user
res_del_user = requests.delete(f'{base_url}/user/{new_username}', headers={'accept': 'application/json'})
print(f'19. {res_del_user.status_code} - статус-код Delete user')
if 'application/json' in res_del_user.headers['Content-Type']:
    print(f'Тело ответа:')
    pprint(res_del_user.json(), width=40, indent=10)
else:
    print(f'Тело ответа:')
    pprint(res_del_user.text, indent=10)
print('---------------------------------------------------------------------------------------------------------------')