import boto3
def get_security_hub_arn(session):
   securityhub = session.client('securityhub')
   try:
       hub_description = securityhub.describe_hub()
       return hub_description['HubArn']
   except Exception as e:
       print(f"Could not describe hub: {e}")
       return None
def tag_security_hub_resource(session, hub_arn, tags):
   securityhub = session.client('securityhub')
   # Get current tags
   current_tags = securityhub.list_tags_for_resource(ResourceArn=hub_arn).get('Tags', {})
   print(f"Current tags for {hub_arn}: {current_tags}")
   # Only add tags that don't exist
   tags_to_add = {k: v for k, v in tags.items() if k not in current_tags}
   if tags_to_add:
       try:
           securityhub.tag_resource(ResourceArn=hub_arn, Tags=tags_to_add)
           print(f"Tagged Security Hub resource {hub_arn} with tags: {tags_to_add}")
       except Exception as e:
           print(f"Failed to tag resource {hub_arn}: {e}")
   else:
       print(f"Security Hub resource {hub_arn} already has the specified tags.")
   # Get updated tags
   updated_tags = securityhub.list_tags_for_resource(ResourceArn=hub_arn).get('Tags', {})
   print(f"Updated tags for {hub_arn}: {updated_tags}")
if __name__ == "__main__":
   profiles = [ 'example-1']
   region = 'us-east-1'
   tags = {
       'AppId': '0123456799',
       'OwnerEmail': 'example@xyz.com'
   }
   for profile_name in profiles:
       print(f"\nAWS Account: {profile_name}")
       session = boto3.Session(profile_name=profile_name, region_name=region)
       hub_arn = get_security_hub_arn(session)
       if hub_arn:
           tag_security_hub_resource(session, hub_arn, tags)
