
import boto3
import urllib.parse

# Create AWS service clients
s3 = boto3.client("s3")
sns = boto3.client("sns")

# Replace YOUR_ACCOUNT_ID with your AWS account ID
# when configuring this example in your own AWS environment.
SNS_TOPIC_ARN = (
    "arn:aws:sns:us-west-2:YOUR_ACCOUNT_ID:WordCountTopic"
)


def lambda_handler(event, context):
    # Get details of the uploaded S3 object
    record = event["Records"][0]

    bucket_name = record["s3"]["bucket"]["name"]
    file_key = urllib.parse.unquote_plus(
        record["s3"]["object"]["key"]
    )

    # Read the uploaded file from S3
    response = s3.get_object(
        Bucket=bucket_name,
        Key=file_key
    )

    # Decode the file and count its words
    file_content = response["Body"].read().decode("utf-8")
    word_count = len(file_content.split())

    # Get the file name
    file_name = file_key.split("/")[-1]

    # Prepare the email message
    message = (
        f"The word count in the {file_name} "
        f"file is {word_count}."
    )

    # Send the result through Amazon SNS
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="Word Count Result",
        Message=message
    )

    return {
        "statusCode": 200,
        "body": message
    }
