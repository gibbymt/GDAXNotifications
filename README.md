## GDAXNotifications
A simple text notification service build with AWS lambda to notify on order fills

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

