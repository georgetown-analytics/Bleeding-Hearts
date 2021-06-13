def s3upload(name,df,folder):
    with open('/Volumes/Key/aws_keys.json') as f:
        creds = json.load(f)
    x = df.to_csv(None).encode()
    fs = s3fs.S3FileSystem(key=creds['AWSAccessKeyId'], secret=creds['AWSSecretKey'])
    with fs.open('s3://bleeding-hearts/'+folder + name + '.csv', 'wb') as f:
        f.write(x)
    print('saved')