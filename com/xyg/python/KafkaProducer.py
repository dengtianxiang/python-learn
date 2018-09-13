# -*- coding: utf-8 -*-
'''
Created on 2017年10月17日
pip.exe install kafka-python
@author: root
'''
from kafka import KafkaProducer
from kafka import KafkaClient, SimpleProducer, SimpleConsumer
kafka = KafkaClient("hadoop1:9092")
producer = SimpleProducer(kafka)
producer.send_messages("RoadRealTimeLog","Hello world!")