#  Predicting Oil Prices Using an RNN with Watson Studio 

## Part 2 - Hyperparameter optimization, model deployment and scoring with Watson Studio

This Watson Studio labs continues working with the RNN developed in  [Part 1](https://github.com/djccarew/timeseries-rnn-lab-part1). It contains the steps and code to demonstrate support of deep learning experiments in Watson Machine Learning Service. It illustrates the use of  the  Watson Machine Learning Python API for getting data, experiment definition, hyper parameter optimization, model persistence, model deployment and scoring.

## Setup

**Note:** If you haven't done  the lab in [Part 1](https://github.com/djccarew/timeseries-rnn-lab-part1) then follow the following steps in the [setup instructions for Part 1](https://github.com/djccarew/timeseries-rnn-lab-part1#setup) before continuing:

   i. Sign up  for Watson Studio (if you haven't already)
   
   ii. Create a Watson Studio Project


### 1 Add Cloud Object Storage credentials for your code

Your code  will need access to Cloud Object Storage in this lab. An instance of Cloud Object Storage  will have been created for you when you created the Watson Studio Project in Part 1. 

1.1 In [Watson Studio](https://dataplatform.ibm.com/home?context=analytics) select **Services->Data Services**

![Data Services](images/ss0.png)


1.2 Click on your instance of Cloud Object Storage (this will take you to a new browser tab)

![COS Instance](images/ss1.1.png)


1.3 Click on **Manage**, then click on **Service Credentials** and then on **New credential** as shown in the screenshot below:

![New credential](images/ss1.2.png)


1.4 Type in the JSON string ```{"HMAC": true}``` in the field **Add Inline Configuration Parameters** and then click **Add**

![Add new credential](images/ss3.1.png)


1.5 Click on **View credentials** next to the  credential you just added and copy the entire JSON document to a new text file on your Desktop. You'll need this information when running your notebook later in the lab.

![Save credential](images/ss4.png)


### 2 Create an instance of the Watson Machine Learning service and associate it with your Wtason Studio Project

2.1 Go back to your Watson Studio tab and select **Projects->Time Series RNN Demo**

![Back to project](images/ss5.png)


2.2 Click on the **Settings** for your project

![Settings](images/ss6.png)


2.3 Scroll down to the **Associated services** section. click on **Add Service** and then select **Machine Learning**

![Add WML](images/ss8.png)


2.4 Click on **New**, select the **Lite plan** and then click **Create**. Click on **Confirm** when prompted.

2.5 From the Watson Studio menu bar at the top select **Services->Watson Services**

2.6 Click on the Watson Machine Learning instance you just created 

2.7 Select **Service credentials** and then click on **View credentials** for the one set of credentials already there.

![WML credentials](images/ss9.png)


2.8 Copy the JSON content to the  same text file you used to save the Cloud Object Storage credentials earlier.


### 3. Create  and run this lab's notebook

3.1 Go back to your Watson Studio tab and select **Projects->Time Series RNN Demo**

3.2 Click on the **Assets** tab 

![Assets](images/ss3.png)

3.2 Scroll down to the *Notebooks* section and click on **New Notebook**

3.3 Name the Notebook *My Time Series RNN Demo Part 2* . Select **From URL** and copy the following URL into the **Notebook URL** field

```https://raw.githubusercontent.com/djccarew/timeseries-rnn-lab-part2/master/oilpricernnpart2.ipynb```

3.4 Click on **Create Notebook**. After a few seconds the notebook should be loaded

![Notebook loaded](images/ss10.png)

3.5 Follow the instructions in the notebook to complete the exercise. 
