import os
import json
from google.cloud import pubsub_v1


with open("conf.json", "r") as conf_file:
    data = json.load(conf_file)
    project_id = data["project_id"]
    topic = data["topic"]

publisher = pubsub_v1.PublisherClient()

topic_name = f'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic='MY_TOPIC_NAME',  # Set this to something appropriate.
)

publisher.create_topic(name=topic_name)
future = publisher.publish(topic_name, b'My first message!', spam='eggs')
future.result()