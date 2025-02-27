import azure.functions as func
import logging
import re
import json
app = func.FunctionApp()

@app.blob_trigger(arg_name=[BLOB_NAME], path=[BLOB_PATH],
                               connection=[STORAGE ACCOUNT]) 
def exojson([BLOB_NAME]: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
    [BLOB_NAME].name.match(r".*(\.json)$")
    if re.match(r".*(.json)\Z"): # Is it a .json ?
        try : BufferDict = json.load([BLOB_NAME]) # Is it a *good* json ?
            if text = BufferDict.get("text") # is there text in the json ? (this doesn't account for the nested dictionaries a more complex json would make, or multiple text keys, but no time to develop that)
                text = httpPOST(text,AzureTranslateAPI) #pseudocode, because, again, no time
                BufferDict.update({"text":text}) # Overwriting with the translated text
                BlobUpload(json.dump(BufferDict)) #Pseudocode yet again
        except: logging.error("JSON failed to decode")
    else:
        logging.error("The file submitted was not a JSON file.")
