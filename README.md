# Hand-Written-Digit-Recognition
Hand Written Digit Recognition using a Simple Neural Network.



<h2>Importing the necessary Libraries and Data set which is availabe in Keras.</h2>

![image](https://github.com/user-attachments/assets/710b287d-3592-4395-abc3-f7dfb870bdbe)

<H2>Load the Data set into Training and Testing</H2>

![image](https://github.com/user-attachments/assets/28d92d69-56f6-4323-a0fc-10d1b4496988)

<h2>Scaling the Data</h2>
<p>Convert the pixel values as 0 to 1 and print a sample to ensure that your training data is Scaled</p>

![image](https://github.com/user-attachments/assets/adc3a522-87b0-4d4b-9f1c-fbfb3d400398)


<h2>Flatten the <b>2-d</b> Array into <b>1-d</b></h2>
<p>Converting 2-Dimensional Array to 1-Dimensional Array(Columns) to feed them as input to the Neural Networ (Input Layer)</p>

![image](https://github.com/user-attachments/assets/734bab1f-eb19-41f2-b64c-dbc7f7b98344)

<h2>Creating the Neural Network using <b>Keras.Sequential</b> </h2>
<p>Sequential, Which means our all Input neuron is Connected to the next Layer's Neurons and We can use inbuilt Flatten function provided by Keras or we can just Scale by the above mentioned Step(Flatten)</p>


![image](https://github.com/user-attachments/assets/40cc0bc7-6125-4b06-801d-e185d47119d1)

<p>We do have numerous Activation Function which can be used in Various Situation.</p>

<h2>Compiling the Model</h2>
<p>We Compile our model using various Attributes<br>
  
1. Optimizer function.
  <br>
2.Loss Function.
  <br>
3.Metrics  etc...</p>

![image](https://github.com/user-attachments/assets/df2c9d1f-1c3c-45a4-ab98-67ebcce59b65)


<h2>Fit the model using Training Samples</h2>
<p>So, that we can check out model's perfomance on unseen </p>
![image](https://github.com/user-attachments/assets/04c72b01-f3a1-4789-80d5-fd59c7fa4dfb)



