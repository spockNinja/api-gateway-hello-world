# api-gateway-hello-world
A starting point for a simple REST API backed by a python lambda function.

NOTE: Requires AWS Account (shouldn't break past the free tier) with cli configuration


### Getting Started
First things first, fork this repo so you can customize it.

The only required change to the code before you get up and running is to change the `Source` `Location` in `/development-resources.yaml` to point to your new fork.

Now we can really have some fun!

1. Get yourself a virtual environment for this project.
2. `pip install -r requirements-dev.txt`
3. `aws cloudformation create-stack --stack-name PythonAPIDevResources --template-body file://development-resources.yaml --capabilities CAPABILITY_IAM`
4. In the AWS console, run the newly created CodeBuild job (should have "LambdaPackageJob" in the name)
5. Test it out. You can add, list, and get books by default.
12. Make it your own and do something awesome!

When you make a change to your fork's master branch, you can simply re-run the CodeBuild job to update the Lambda stack. The API will automatically use the updated lambda function.


#### TODOs
* Tests!!!
* CI/CD with full CodeBuild/CodePipeline suite
* More or different functionality
