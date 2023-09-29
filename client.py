import asyncio
import websockets
from auth import *


async def main():
    # Conecta-se ao servidor WebSocket
    async with websockets.connect("ws://localhost:8765") as websocket:
        option = input(OPTION)
        await websocket.send(option)

        if option == '1':
            user = input('user: ').lower().strip()
            user = encriptar(user)
            await websocket.send(user)
            # senha 1
            senha1 = input('password: ').lower().strip()
            senha1 = encriptar(senha1)
            await websocket.send(senha1)

            rs = await websocket.recv()

            if rs == 'True':
                print('Login concluído com sucesso!')
            else:
                print('Login não autorizado!')

        elif option == '2':
            # user
            user = input('user: ').lower().strip()
            user = encriptar(user)
            await websocket.send(user)
            # senha 1
            senha1 = input('password: ').lower().strip()
            senha1 = encriptar(senha1)
            await websocket.send(senha1)
            # senha 2
            senha2 = input('confirm the password: ').lower().strip()
            senha2 = encriptar(senha2)
            await websocket.send(senha2)

            rs = await websocket.recv()

            if rs == 'True':
                print('Usuário cadastrado!')
            else:
                print('O usuário não pôde ser cadastrado!')

        elif option == '3':
            all_users = await websocket.recv()
            all_users = desencriptar(all_users)
            print(all_users)

            await websocket.send('usuários recebidos')

        elif option == '4':
            print('Programa encerrado')

        else:
            print('Opção inválida!')

if __name__ == "__main__":
    # Executa o cliente WebSocket
    asyncio.get_event_loop().run_until_complete(main())
