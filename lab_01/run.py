from producer_consumer.producer import Producer
from producer_consumer.consumer import Consumer
import threading

#Create producer and consumer
topic = {'Air': 'AIR2308.csv', 'Water': 'WATER2308.csv', 'Earth': 'EARTH2308.csv'}
producer = Producer(topic)

consumers = []
for key, value in topic.items():
    consumer = Consumer(key)
    consumers.append(consumer)


# Create threads for each producer and consumer
producer_threads = []
consumer_threads = []

for key, value in topic.items():
    producer_thread = threading.Thread(target=producer.send, args=(key,))
    producer_threads.append(producer_thread)
    
for consumer in consumers:
    consumer_thread = threading.Thread(target=consumer.getValue)
    consumer_threads.append(consumer_thread)


# Start all Producer threads
for thread in producer_threads:
    thread.start()

# Start all Consumer threads
for thread in consumer_threads:
    thread.start()

# Wait for all threads to complete
for thread in producer_threads:
    thread.join()

for thread in consumer_threads:
    thread.join()

producer.close()
for consumer in consumers:
    consumer.close()