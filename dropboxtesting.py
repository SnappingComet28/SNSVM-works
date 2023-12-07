import dropbox 
# Replace 'YOUR_ACCESS_TOKEN' with the access token generated for your app
access_token = 'sl.Bq1_JpnG8yourgC1dsN9yYWrirdPcFuWddwV6VDivxvXIyJwZatO6T1Bmq_vwgNvogn4X2VKOjev5-ha0bw9jPvR2PY4JVDBWxnbCNI7nCP0ldFVfr6G5llobae9U8yoSE7_1QNPprBf'

# Create a Dropbox object
dbx = dropbox.Dropbox(access_token)

# Specify the path to the text file in Dropbox
file_path = '/test/ppl2.txt'

try:
    # Download the file directly as bytes
    metadata, response = dbx.files_download(file_path)
    content = response.content

    # Decode the content from bytes to string (assuming it's a text file)
    content_str = content.decode('utf-8')

    # Now 'content_str' contains the text content of the file
    print(content_str)

except dropbox.exceptions.HttpError as e:
    print(f"Error downloading the file: {e}")


#########CHange content##########
access_token = "sl.Bp_hDyds_JOu0SlMuFc2MrgPBngePcGTKbRT9GXk9uD-Bx2qHmxdHBbVGDB6ZAcbsE2GXpffvAN2m1WFaqhmkOr0ONRPy0rw-xzx4oucp6gxN2dOfSoMmcCb7hJn0wahsH6IV1NaILtv"


# Replace 'YOUR_ACCESS_TOKEN' with the access token generated for your app

# Create a Dropbox object
dbx = dropbox.Dropbox(access_token)

# Specify the path to the text file in Dropbox
file_path = '/test/dropbox.txt'

try:
    # Read the existing content of the file
    metadata, response = dbx.files_download(file_path)
    existing_content = response.content.decode('utf-8')

    # Modify the content as needed
    new_content = "This is the updated content."

    # Upload the modified content as a new version of the file
    dbx.files_upload(new_content.encode('utf-8'), file_path, mode=dropbox.files.WriteMode('overwrite'))

    print("File updated successfully.")

except dropbox.exceptions.HttpError as e:
    print(f"Error updating the file: {e}")

