import json
import boto3
from datetime import datetime

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
s3 = boto3.client("s3")

MODEL_ID = "amazon.nova-lite-v1:0"
BUCKET_NAME = "morningbriefagent-jyothish-2026"

def lambda_handler(event, context):

    prompt = """
Generate today's morning brief.

Include:
1. One motivational quote
2. One productivity tip
3. One AWS learning tip

Keep it under 150 words.
"""

    response = bedrock.converse(
        modelId=MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    )

    answer = response["output"]["message"]["content"][0]["text"]

    filename = "brief-" + datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S") + ".txt"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body=answer,
        ContentType="text/plain"
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Morning brief saved successfully!",
            "file": filename,
            "brief": answer
        })
    }