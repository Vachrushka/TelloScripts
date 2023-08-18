import socket

def set_ap(ssid, password):
    '''
    Функция для установки Tello в режиме AP
     :параметр ssid: ssid сети (например, имя Wi-Fi)
     :параметр password: пароль сети
    '''
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
    my_socket.bind(('', 8889))
    cmd_str = 'command'
    print ('sending command %s' % cmd_str)
    my_socket.sendto(cmd_str.encode('utf-8'), ('192.168.10.1', 8889))
    response, ip = my_socket.recvfrom(100)
    print('from %s: %s' % (ip, response))

    cmd_str = 'ap %s %s' % (ssid, password)
    print ('sending command %s' % cmd_str)
    my_socket.sendto(cmd_str.encode('utf-8'), ('192.168.10.1', 8889))
    response, ip = my_socket.recvfrom(100)
    print('from %s: %s' % (ip, response))

# пример установки Tello в командный режим
# работает только если сервер подключен к Tello Wi-Fi
set_ap('wifi_ssid', 'wifi_pass')
