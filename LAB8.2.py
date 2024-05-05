import aiohttp
import asyncio


async def get_user_info(user_id, access_token):
    url = f"https://api.vk.com/method/users.get?user_ids={user_id}&access_token={access_token}&v=5.131"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            if 'error' in data:
                print(f"Error: {data['error']['error_msg']}")
                return None
            else:
                user_info = data['response'][0]
                print("User Info:")
                print(f"ID: {user_info['id']}")
                print(f"First Name: {user_info['first_name']}")
                print(f"Last Name: {user_info['last_name']}")
                return user_info


async def main():
    user_id = "321366961"
    access_token = "d07640d2d07640d2d07640d24bd36e76d7dd076d07640d2b641892e7790e62ab73c5bbc"

    user_info = await get_user_info(user_id, access_token)
    if user_info:
        print("User info retrieved successfully.")
    else:
        print("Failed to retrieve user info.")


asyncio.run(main())
