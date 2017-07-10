## GDAX Notifications
A simple cost effective SMS notification service build with AWS Lambda to notify on GDAX order fills

### Config and Setup
1. Configure a CloudWatch rule that runs every 1 minute
2. Create a new Lambda that uses the CloudWatch rule from step one as a trigger
3. `sh ./bundle_for_deployment.sh`
4. upload `deployment_bundle.zip` to aws lambda
5. set all the required environment variables, see example below
```
pass_phrase	aasd0f9870asdf
aws_access_key_id	ASDF0897ASDF0978ASDF
aws_secret_access_key	kasgsfdgsd+gdapoagdopiue
phone_number	+12223334444
region_name	us-east-1
secret	asdflkaihfjoeijafpoijfaAFSODFIHAOEIJFADF==/=
key	asdf0987asdf0987asdf0987as0df987
```
6. test your lambda function by passing in the following
```
"test"
```
7. If you get a text message then you're configured the lambda correctly

### Cost
The great thing about running this serverless application is that's esentially free! 
- You get 3,200,000 seconds of computute free each month while using AWS Lambda
- You get 100 SNS SMS messages each month free. Each additional SMS costs $0.00645
