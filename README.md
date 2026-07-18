# AWS Morning Brief Agent

An Always-On AI Agent built using AWS services.

## Architecture

EventBridge
    ↓
AWS Lambda
    ↓
Amazon Bedrock (Nova Lite)
    ↓
Generate Morning Brief
    ↓
Amazon S3

## AWS Services Used

- Amazon Bedrock (Nova Lite)
- AWS Lambda
- Amazon EventBridge
- Amazon S3
- IAM

## Features

- Generates a morning brief every day
- Motivational quote
- Productivity tip
- AWS learning tip
- Automatically saves output to Amazon S3

## Schedule

Runs every day at **6:00 AM IST** using Amazon EventBridge.

## Author

Jyothish
