from vidstream import AudioSender
from vidstream import AudioReceiver

import threading

receiver = AudioReceiver('192.168.1.2', 9999)
receive_thread = threading.Thread(target=receiver.start_server)

sender = AudioSender('', 8888)
sender_thread = threading.Thread(target=sender.start_stream)

receive_thread.start()
sender_thread.start()
