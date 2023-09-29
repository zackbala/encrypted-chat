import asyncio
import websockets
from auth import *

users = {'isac': '1995'}


def login(user, passwd):
    user.lower().strip()

    if user in users:
        passwd.lower().strip()

        if users[user] == passwd:
            print("Acesso autorizado!")
            return True
        else:
            print("acesso negado!")
            return False
    else:
        print("este usuário não existe")
        return False


def cadastrar_usuario(user, x, y) -> bool:
    user.lower().strip()

    if user in users:
        print("O usuário não pode ser cadastrado")
        return False
    else:
        x.lower().strip()
        y.lower().strip()

        if x == y:
            users[user] = x
            print("Usuário cadastrado")
            return True
        else:
            print("senhas incompatíveis")
            return False


async def handle(websocket):
    # async for option in websocket:

    option = await websocket.recv()
    # option = desencriptar(option)
    print(option)

    if option == '1':
        user = await websocket.recv()
        user = desencriptar(user)

        senha1 = await websocket.recv()
        senha1 = desencriptar(senha1)

        rs = str(login(user, senha1))
        await websocket.send(rs)

    elif option == '2':
        user = await websocket.recv()
        user = desencriptar(user)

        senha1 = await websocket.recv()
        senha1 = desencriptar(senha1)

        senha2 = await websocket.recv()
        senha2 = desencriptar(senha2)

        rs = str(cadastrar_usuario(user, senha1, senha2))
        await websocket.send(rs)

    elif option == '3':
        user = str(users)
        print(user)
        all_users = encriptar(user)
        await websocket.send(all_users)

        msg = await websocket.recv()
        print(msg)

    else:
        print('Programa encerrado!')


start_server = websockets.serve(handle, "localhost", 8765)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
