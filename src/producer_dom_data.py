from FinamPy import FinamPy
from google.protobuf.json_format import MessageToDict
import datetime
import pika
import json
import src.config as config




def main():



    connection = pika.BlockingConnection(pika.ConnectionParameters(config.RABBIT_MQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue='rts_dom')

    fp_provider = FinamPy(config.TOKEN)
    security_board = 'FUT'  # Код площадки
    security_code = 'RIM3'  # Тикер
    orderbook_name = security_code + '_dom'

    def order_book_stream_handler(order_book):
        receive_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        order_book = MessageToDict(order_book,preserving_proto_field_name=True)
        order_book['receive_time'] = receive_time
        order_book = json.dumps(order_book)
        channel.basic_publish(exchange='',
                              routing_key='rts_dom',
                              body=order_book)

    fp_provider.on_order_book = order_book_stream_handler
    fp_provider.subscribe_order_book(security_code, security_board, orderbook_name)

    # Выход
    input('Enter - выход\n')
    fp_provider.unsubscribe_order_book(orderbook_name, security_code, security_board)  # Отписываемся от стакана тикера
    fp_provider.close_channel()  # Закрываем канал перед выходом

if __name__ == '__main__':
    main()
