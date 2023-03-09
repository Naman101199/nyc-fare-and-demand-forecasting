import os
from tqdm import tqdm
from google.cloud import storage

storage_client = storage.Client(project='integral-plexus-375000')

#function for uploading the data from kaggle to google cloud services 
def upload_files(bucket_name, source_folder, directory_to_upload):
    bucket = storage_client.get_bucket(bucket_name)
    for filename in tqdm(os.listdir(source_folder)):
        blob = bucket.blob(directory_to_upload + filename)
        blob.upload_from_filename(source_folder + filename)

#create_folder('bigdata-naman','data/project/amex_default_prediction')
upload_files('bigdata-naman','/kaggle/input/tlc-trip-record-data-yellow-taxi/','data/project/tlc_trip_record_yellow_taxi/')