# AWS Lambda S3 SNS Word Count Challenge

## Project Overview

This project demonstrates how to build an event-driven application using AWS Lambda, Amazon S3, and Amazon SNS.

When a text file is uploaded to an Amazon S3 bucket, an AWS Lambda function is automatically triggered. The function reads the file, counts the words, and sends the result to an email subscriber through Amazon SNS.

## Architecture

```text
User uploads a text file
          |
          v
     Amazon S3
          |
          | ObjectCreated event
          v
     AWS Lambda
   WordCountFunction
          |
          | Counts words
          v
     Amazon SNS
    WordCountTopic
          |
          v
   Email notification
```

Amazon CloudWatch Logs records the Lambda function's execution activity.

## AWS Services Used

| Service | Purpose |
|---|---|
| Amazon S3 | Stores uploaded text files |
| AWS Lambda | Reads files and counts words |
| Amazon SNS | Sends word-count results by email |
| Amazon CloudWatch | Stores Lambda execution logs |
| AWS IAM | Provides permissions to access AWS services |

**AWS Region:** US West (Oregon) — `us-west-2`

## Lambda Function

**Function name:** `WordCountFunction`

**Execution role:** `LambdaAccessRole`

The function reads the uploaded file, decodes its contents as UTF-8, counts the words, and publishes the result to the SNS topic.

## Test Results

| Test file | File content | Expected word count | Result |
|---|---|---:|---|
| `sample.txt` | AWS Lambda makes cloud automation easy. | 7 | Passed |
| `sample2.txt` | Cloud computing helps teams build secure applications faster. | 8 | Passed |

Both tests successfully triggered the Lambda function and produced email notifications containing the correct word counts.

## Screenshots and Evidence

The `screenshots` folder will contain evidence captured during the lab, including:

- SNS topic and confirmed email subscription
- Lambda function code
- S3 bucket and Lambda trigger configuration
- CloudWatch execution logs
- Word-count email notifications

Only screenshots that have actually been captured should be added.

## Key Learnings

- Creating and configuring an Amazon SNS topic and email subscription
- Creating an AWS Lambda function using Python
- Triggering Lambda automatically when an S3 object is uploaded
- Reading objects from Amazon S3 using the AWS SDK for Python (Boto3)
- Publishing notifications using Amazon SNS
- Checking Lambda execution activity in CloudWatch Logs
- Testing and validating a serverless workflow

## Security Considerations

- Keep the S3 bucket private and Block Public Access enabled.
- Apply least-privilege IAM permissions.
- Do not publish account-specific ARNs, personal email addresses, or other sensitive details in a public repository.
- Do not commit AWS credentials or secrets to GitHub.

## Project Status

**Completed and tested successfully.**
# aws-lambda-s3-sns-word-count
Project overview, architecture, results and key learnings.
