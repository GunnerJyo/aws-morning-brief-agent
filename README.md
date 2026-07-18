# AWS Morning Brief Agent

An Always-On AI Agent built with AWS.

## Services Used

- Amazon Bedrock (Nova Lite)
- AWS Lambda
- Amazon EventBridge
- Amazon S3
- IAM

## Architecture

EventBridge
    ↓
Lambda
    ↓
Amazon Bedrock (Nova Lite)
    ↓
Generate Morning Brief
    ↓
Save to Amazon S3

## Features

- Generates a daily morning brief
- AI-generated motivational quote
- Productivity tip
- AWS learning tip
- Automatically runs every day at 6:00 AM IST
- Saves output to Amazon S3

## Sample Output

Morning Brief

Good morning!

Motivational Quote:
"Success is not final..."

Productivity Tip:
Start with the hardest task first.

AWS Learning:
Explore AWS CloudFormation...

## Author

Jyothish