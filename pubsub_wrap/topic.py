import json
from google.cloud import pubsub_v1


with open("conf.json", "r") as conf_file:
    data = json.load(conf_file)
    project_id = data["project_id"]
    topic_id = data["topic"]
    subscription_id = data["subscription_id"]

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

topic = publisher.create_topic(request={"name": topic_path})

print(f"Created topic: {topic.name}")