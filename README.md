# Crop_Recommendation_Model_using_Automl_on_Azure
This project implements a machine learning model for crop recommendation using Automated Machine Learning (AutoML) on Microsoft Azure.

# Project Overview
This project details the development and deployment of a crop recommendation model. It utilizes Azure services for data storage, computation, and real-time deployment. The model analyzes various factors that influence crop growth, such as soil properties and climate data, to suggest the most suitable crop for a given set of conditions.

# Technologies Used
  1. Azure Blob Storage: Stores the dataset used for training the model. This dataset may includes features like soil composition (pH, Nitrogen, Phosphorus, Potassium), historical weather data (temperature, rainfall, humidity).
  2. Azure Machine Learning (AutoML): Automates the model training process, optimizing hyperparameters for the best performance. AutoML explores various algorithms and configurations to find the one that best fits the data and delivers the most accurate crop recommendations.
  3. Azure Compute Instance: Provides the computational resources for training the model. The complexity of the model and the size of the dataset will determine the required computing power.
  4. Azure Machine Learning Service (optional): Enables real-time deployment and consumption of the trained model. Once trained, the model can be deployed as a web service on Azure Machine Learning Service. This allows farmers and agricultural professionals to interact with the model in real-time and receive crop recommendations for their specific needs.

# Interconnected Services
The project leverages the following workflow:

  # Create an Azure Machine Learning workspace 
  To use Azure Machine Learning, you need to provision an Azure Machine Learning workspace in your Azure subscription. Then you’ll be able to use Azure Machine Learning studio to work with the resources     in your workspace. 
  1. Sign in to the Azure portal at https://portal.azure.com using your Microsoft credentials. 
  
  ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/1f674a8a-5b4a-45f3-ae7e-1fdd65cedb47)

  2. Select + Create a resource, search for Machine Learning, and create a new Azure Machine Learning resource with the following settings: 
     1. Subscription: Your Azure subscription. 
     2. Resource group: Create or select a resource group. 
     3. Name: Enter a unique name for your workspace. 
     4. Region: Select the closest geographical region. 
     5. Storage account: Note the default new storage account that will be created for your workspace. 
     6. Key vault: Note the default new key vault that will be created for your workspace. 
     7. Application insights: Note the default new application insights resource that will be created for your workspace. 
     8. Container registry: None (one will be created automatically the first time you deploy a model to a container).
  
  ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/f0692e7f-6169-4565-8909-e11d740669cb)

  3. Select Review + create, then select Create. Wait for your workspace to be created (it can take a few minutes), and then go to the deployed resource.

     ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/c514564e-7669-4fa1-aff4-da0f88e9e001)

  4. Select Launch studio.

     ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/ae8da505-6896-47fc-820c-b324d2b37f68)

  5. In Azure Machine Learning studio, you should see your newly created workspace.

     ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/3982f89d-ce50-48cc-899f-0be3258c02d5)


  # Create and load a dataset as a data asset
  1. In left pane, select Data under Assets.
    
  ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/f289ffd7-ec99-4aaf-a213-459a3a417544)

  2. Now, click on Create under Data Assets.
      1. Name : Crop-recommendation-dataset
      2. Description : Crop recommendation model using Automl.
      3. Type : Tabular

  ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/633b40a0-4764-4ef9-97c7-0c0ba199927b)

  3. In Data Source, select From local files.

     ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/fa634610-207f-4820-9215-eda2e32182d6)

  4. Destination Storage type : Azure Blob Storage

     ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/813ae69d-4ee4-46ba-809e-958cddc018d4)

  5. File or Folder selection : Upload File

     ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/449a7a97-f582-4590-a839-fca918900383)

  6. Settings :

     ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/7fbbb3f8-8e8d-422c-bd80-9bd87da5580a)

  7. Click create to create the data asset.

     ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/6ac6e71c-f63f-4fd7-ad3e-e228272ba140)

    
  # Create Compute 

  1. In left pane, select Compute under Manage.

     ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/a636b533-f448-4fe4-bd3c-0d7bec1d2b8e)

  2. Click Create under Compute Instances. Name your compute and select virtual machine.

     ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/0c06e3fb-9e48-43b0-b441-bd8375e8c2ff)

  3. Then, click review + create and then create. The compute will be ready in 5 - 10 min.

     ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/093b1db7-ae23-44c8-b058-cd06015d4d39)

     
  # Use automated machine learning to train a model 
  Automated machine learning enables you to try multiple algorithms and parameters to train multiple models, and identify the best one for your data. In this exercise, you’ll use a dataset of historical     bicycle rental details to train a model that predicts the number of bicycle rentals that should be expected on a given day, based on seasonal and meteorological features. 
  
  1. In Azure Machine Learning Studio, view the Automated ML page (under Authoring). 

     ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/5d4ca1f3-f5b7-4f1b-8542-34d36ecb8eb0)

  3. Create a new Automated ML job with the following settings, using Next as required to progress through the user interface: 
     1. Basic settings: 
        1. Job name: Crop-recommendation-model-project
        2. New experiment name: Crop-recommendation-Automl
        3. Description: Automated machine learning for crop recommendation. 
        4. Tags: none 
     
     ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/707ccf9f-3433-49e3-b34a-fbc71919d267)

      2. Task type & data: 
         1. Select task type: Classification 
         2. Select dataset: Select the previously created data asset. 

      ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/8799db77-e86b-4082-8002-5fb2afbc752e)

      3. Task settings: 
         1. Task type: Regression 
         2. Dataset: crop-recommendation-dataset 
         3. Target column: label (String) 
      
      ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/ddce53c8-646a-4eb9-b22b-a21b9dc01dd1)

      4. Compute: 
         1. Select compute type: Azure Compute Instance. 
         2. Select Azure ML compute instance : select the compute instance created earlier.
      
      ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/4cfb3730-7a1f-4510-b2de-1c215a355fd4)

        
  4. Submit the training job. It starts automatically. 
  5. Wait for the job to finish.

     ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/6614dff2-945c-4894-b772-f59dbb9ddbbe)

     ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/526aa3b4-cd4e-42ca-8e58-6433ee75fdf5)

  # Deploy and test the model 
  1. On the Model tab for the best model trained by your automated machine learning job, select Deploy and use the Real Time endpoint option to deploy the model with the following settings: 
      1. Virtual Machine
      2. Endpoint Name: crop-recommendation-proje-lkwci
      3. Deployment Name: Croprecommendat42-1
    
  ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/c731ae1f-d1fa-4ffe-bee7-f254d587aa8b)

  2. Wait for the deployment to start - this may take a few seconds. The Deploy status for the predict-rentals endpoint will be indicated in the main part of the page as Running. 
  3. Wait for the Deploy status to change to Succeeded. This may take 5-10 minutes. 
    
  ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/a2dbd52e-c140-4cd3-a0aa-cdf0f3a8d7e7)
    
  4. Test : paste code from test.txt file.

  ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/67420404-7b80-4f8f-aacd-d6a5ab26f92e)


  # Using Google Colab to test : 
  1. Paste the consume.txt code to colab.
  2. Enter the api key provided on consume tab.
  3. Run the notebook.
  
  ![image](https://github.com/nirmalchoudhary9/Crop_Recommendation_Model_using_Automl/assets/121570151/9f938c58-a4e6-4a80-92c9-e2eda0eb1fea)

# Benefits
This project offers several benefits:

  # Improved decision-making: 
    Farmers can leverage data-driven insights to make informed decisions about crop selection, potentially leading to increased yields and improved farm profitability.
  # Reduced risk: 
    By considering various factors that influence crop growth, the model can help farmers mitigate risks associated with unsuitable crop choices.
  # Increased efficiency: 
    The automated recommendation process saves farmers time and effort in researching and selecting the right crops.
  # Scalability: 
    The cloud-based infrastructure allows the model to be easily scaled to accommodate a growing user base.

# Conclusion
This crop recommendation model using AutoML on Azure demonstrates the potential of machine learning for enhancing agricultural practices. By leveraging data and automation, farmers can gain valuable insights and make informed decisions to optimize their yields and improve overall farm management.
