# CZ4171: Internet of Things: Communication & Networking

## Flutter App to Classify Money

# Step 1: Training Machine Learning Model

The model is trained via google colab using their GPU, the dataset used contained 250 custom pictures of the Singapore Dollar(SGD). 
- Epochs: 15
- Batch Size: 32
- Optimizer: Adam
- Loss: categorical_crossentropy

The result of this training are as follows:

## Accuracy per Epoch

![Accuracy per Epoch](images/accuracy.png)

## Sample predictions on input images

![Loss per Epoch](images/input_prediction.png)

With the completed training, the model will be exported to Tensorflow in the Keras format under my_model folder.

The training images and saved model can be found in this drive: https://drive.google.com/drive/folders/1psxBNAUH8L5OcEMnzhKs2r7q-w_83T4X?usp=sharing

# Step 2: Building Backend Endpoint

The backend server will be hosted locally and deployed via FastApi framework to allow easy debuging and ease of use. FastApi provides a web UI to test out the different api endpoints. Tensorflow is also installed locally to carry out the prediction. By default, fastapi supports concurrency and multiple user via async endpoints which is used to build our "predict" endpoint.

![Api Endpoint](images/fastapi.png)

# Part 3: Mobile Application

The mobile application was created using Flutter. This allows for cross-platform development using a single code base. For this project, I will primarily be focusing on Android. The source code for the app can be found in _'/CX4171 Project - Bank Note Image Classification/iotbanknoteclassification'_. Please read the README.md inside the folder to know how to set up the app.

## Main Page

<img src="images/1.jpg" width="250">

This is the main page of the application. The placeholder shows where the image the user selected will be displayed. The app allows the user to upload an image either using the smartphone's native camera or from the user's gallery. Once the user selected an image, they can tap on submit to send the request.

## Selection - Taking Picture

<img src="images/2.jpg" width="250">

If the user tap on the Camera button, it will open up the device's camera and the user will have to take a picture of the bank note. Once they are satisfied with the picture, they can tap on the Ok button.

## Submit - Taking Picture

<img src="images/3.jpg" width="250">

The image taken will be shown in the placeholder and the user can tap on Submit to send the classification request to the model in Azure Machine Learning service. Once the model predicted the result, it will send the result back to the app and the result will be displayed to the user via a dialog box.

## Selection - Gallery 1

<img src="images/5.jpg" width="250">

By tapping on the Device button, the user is able to to select an image from their gallery.

## Selection - Gallery 1

<img src="images/6.jpg" width="250">

Once they have selected a bank note image, the image will be displayed on the placeholder.

## Submit - Gallery

<img src="images/7.jpg" width="250">

When the user tap on the Submit button, a request will be sent to the model in Azure Machine Learning service. The model will conduct a prediction and send the result back to the user. The result will be displayed to the user via a dialog box.

# Tasks Checklist

- Local Inference:
  - Collect User Input (15)
    - Collected real-time input using camera :white_check_mark:
  - Infer locally and display result (20)
    - Inference is offload to Azure Machine Learning in the cloud :white_check_mark:
    - Result is displayed to user via dialog box :white_check_mark:
  - Run on Emulated/physical IoT device (15)
    - Ran on physical Android Device :white_check_mark:
- Cloud Inference:
  - Run inference in cloud virtual machine (10)
    - Model is hosted on Azure Machine Learning :white_check_mark:
  - Communicate between IoT device & cloud (20)
    - App can send image data to Azure Machine Learning end point for inference :white_check_mark:
    - Results from the model's prediction can be sent back from the cloud to the app :white_check_mark:
- Advanced Tasks:
  - Train your own model (10)
    - Trained my own model using Google's Teachable Machine Learning Platform :white_check_mark:
  - Support multiple concurrent users (10)
    - Azure Machine Learning is able to support multiple concurrent users hitting it's service's end point :white_check_mark:

# Video Demo on Actual Android Device

<a href="https://youtu.be/q5GzTx9mBoc" target="_blank">Youtube Link</a>
