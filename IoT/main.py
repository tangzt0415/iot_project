from io import BytesIO
import uvicorn
from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
from keras.preprocessing import image
import numpy as np
from PIL import Image
from skimage import transform


# Hide GPU from visible devices
tf.config.set_visible_devices([], 'GPU')
labels = {0: '10dollar', 1: '2dollar', 2: '50dollar', 3: '5dollar'}
IMAGE_WIDTH,IMAGE_HEIGHT = 224,224

app = FastAPI(title='Hello world')


@app.post("/predict")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = predict(image)
    return prediction

def load_model():
    model = tf.keras.models.load_model('my_model')
    print("Model loaded")
    return model

model = load_model()

def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image
    
def predict(image: Image.Image):
    image = np.asarray(image.resize((224, 224)))[..., :3]       
    image = np.expand_dims(image, 0)
    predictions  = model.predict(image)
    pred = predictions[0]
    label = np.argmax(pred)
    print(predictions)
    return labels[label]


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0",debug=True)

@app.get('/index')
async def hello_world():
    return "hello world"

# def predict(np_image: Image.Image):
    # image = np.asarray(image.resize((299, 299)))[..., :3]
    # image = np.array(   image).astype('float32')/255
    # image = np.expand_dims(image, 0)
    #np_image = np.array(np_image).astype('float32')/255
    # np_image = transform.resize(np_image, (224, 224, 3))
    # np_image = np.expand_dims(np_image, axis=0)
    # predictions  = model.predict(np_image)
    # pred = predictions[0]
    # print(predictions)
    # label = np.argmax(pred)
    # print(labels[label])
    # return labels[label]
    # print(note_classes[predictions.argmax()])
    # return (note_classes[predictions.argmax()])



# img = image.load_img('photo_2022-04-14_02-18-34.jpg', target_size = (IMAGE_WIDTH, IMAGE_HEIGHT))
# img = image.img_to_array(img)
# img = np.expand_dims(img, axis = 0)
# predictions  = model.predict(img)
# print(predictions)
# pred = predictions[0]
# label = np.argmax(pred)
# print(labels[label])