import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_hello_fargate.cdk_hello_fargate_stack import CdkHelloFargateStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_hello_fargate/cdk_hello_fargate_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkHelloFargateStack(app, "cdk-hello-fargate")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
