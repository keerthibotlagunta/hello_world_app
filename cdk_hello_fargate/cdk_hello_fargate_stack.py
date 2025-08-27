from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
)
from constructs import Construct

class CdkHelloFargateStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # VPC
        vpc = ec2.Vpc(self, "HelloVpc", max_azs=2)

        # ECS Cluster
        cluster = ecs.Cluster(self, "HelloCluster", vpc=vpc)

        # Fargate Service using Dockerfile from ./app folder
        ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "HelloFargateService",
            cluster=cluster,
            cpu=256,
            memory_limit_mib=512,
            desired_count=1,
            public_load_balancer=True,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_asset("./cdk-hello-fargate"),  # path to app
                container_port=8080,
            )
        )
