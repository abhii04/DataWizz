# DataWizz


DataWizz is a powerful yet user-friendly Streamlit application tailored for students, educators, and data enthusiasts who want to explore and visualize their datasets effortlessly. The app combines intuitive data visualization tools with AI-powered insights to help you uncover hidden patterns and make informed decisions based on your data.
Try it [here!](https://datawizz.streamlit.app/) 

## Features

### 1. **Data Upload and Preview**
   - **File Support:** Easily upload your dataset in CSV or Excel format.
   - **Data Preview:** After uploading, the app displays the first few rows of your dataset, allowing you to verify the contents and structure before analysis.
     
     ![image](https://github.com/user-attachments/assets/913eb5f5-9efa-455e-8d6a-5b0b117c979c)


### 2. **Visualization Options**
   - **Univariate Analysis:** 
     - Generate histograms, box plots, violin plots, and pie charts to understand the distribution of individual columns.
   - **Bivariate Analysis:**
     - Explore relationships between two variables using scatter plots or line plots.
   - **Multivariate Analysis:**
     - Create a correlation heatmap to visualize the relationships between multiple numeric columns, highlighting significant correlations.
      ![image](https://github.com/user-attachments/assets/339ccdc4-6dcd-4e21-87b7-297d55dc502c)


### 3. **AI-Powered Insights**
   - **Cohere API Integration:** The app utilizes Cohere's language model to provide automated explanations for the generated visualizations. This feature helps users interpret the data without requiring deep statistical knowledge.
     - **Example Explanations:**
       - **Histogram:** Insights on distribution, skewness, and peaks.
       - **Scatter Plot:** Analysis of trends, correlations, and outliers.
       - **Correlation Heatmap:** Detailed explanation of correlations between variables.
        ![image](https://github.com/user-attachments/assets/599c9117-a07c-4faa-8b83-a572b556349d)


### 4. **Machine Learning Model Suggestions**
   - **Intelligent Recommendations:** Based on the characteristics of your dataset, DataViz Genie suggests the most suitable machine learning models. These recommendations can guide you in selecting the right algorithms for predictive analysis or other data-driven tasks.
    ![image](https://github.com/user-attachments/assets/2be5cd25-4cf8-494a-b7fd-024d71ed2d1b)
    
### 5. **Interactive and Customizable Visualizations**
   - **Customization:** Adjust parameters like color, bin size, and more to tailor the visualizations to your needs.
   - **Interactivity:** The visualizations are interactive, allowing you to explore the data dynamically.

## How It Works

1. **Upload Your Data:**
   - Begin by uploading a CSV or Excel file through the app’s interface. The file is read and displayed for an initial review.

2. **Select Your Columns and Analysis Type:**
   - Choose one or more columns for analysis. Depending on your selection, you can opt for univariate, bivariate, or multivariate analysis.

3. **Generate Visualizations:**
   - Select the desired plot type (e.g., histogram, scatter plot, heatmap) and adjust any parameters as needed. The app generates the visualization and displays it in the main panel.

4. **Receive Automated Explanations:**
   - For each generated visualization, an explanation is provided using Cohere's API. This helps you understand what the visualization reveals about your data.

5. **Get Model Suggestions:**
   - At the click of a button, receive machine learning model recommendations tailored to your dataset. This feature helps guide your next steps in analysis.


## Conclusion

DataWizz is designed to bridge the gap between data visualization and interpretation, making it easier for users to gain actionable insights from their data. Whether you're a student looking to understand your dataset better or a data enthusiast wanting to experiment with visualizations and machine learning, DataWizz has you covered.
