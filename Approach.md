# Main Approach and Method:

### AWS Lambda:
After doing some group discussions and research on what the best approach would be, we decided to go with Lambda. We were looking for simplicity in setup and maintenance, and with Lambda you can easily run simple jobs that do what you want.
A Lambda function in AWS is a piece of code that is executed in response to an event. In our case the event was a request to an API endpoint.
We chose Lambda as it’s serverless, easily scalable and it integrates with API Gateway.

### API Gateway:
We added API Gateway triggers to each of our Lambda functions in order to create APIs with HTTP endpoints. 
This allowed us to get URLs that can be accessed in our Forage dashboard. API Gateway is designed to provide low latency for API requests, this just means that the data in our dashboard will be seen in real-time, which was the goal of our task.

### EventBridge (CloudWatch Events):
One of our charts requested a count of hourly submissions, so we used EvmentBridge to trigger our Lambda function each hour and send an hourly submission count to one of our databases. This allowed us to efficiently automate this task.
