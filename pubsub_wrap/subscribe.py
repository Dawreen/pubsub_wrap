import os
import json
from google.cloud import pubsub_v1


with open("conf.json", "r") as conf_file:
    data = json.load(conf_file)
    project_id = data["project_id"]
    topic_id = data["topic"]
    subscription_id = data["subscription_id"]

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()
topic_path = publisher.topic_path(project_id, topic_id)
subscription_path = subscriber.subscription_path(project_id, subscription_id)

# Wrap the subscriber in a 'with' block to automatically call close() to
# close the underlying gRPC channel when done.
with subscriber:
    subscription = subscriber.create_subscription(
        request={"name": subscription_path, "topic": topic_path}
    )

print(f"Subscription created: {subscription}")