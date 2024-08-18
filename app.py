import streamlit as st
import pandas as pd
import cohere
import plotly.express as px

# Initialize Cohere API
api_key = st.secrets["cohere"]["api_key"]
co = cohere.Client(api_key)

# Function to generate explanation using Cohere
def get_cohere_explanation(plot_type, column1, column2=None):
    prompts = {
        "histogram": f"Interpret the distribution of the '{column1}' column using a histogram. Include any skewness, peaks, and any insights that can be drawn from the distribution in short.",
        "boxplot": f"Interpret the boxplot of the '{column1}' column. Describe the distribution, outliers, and any patterns observed in short.",
        "violinplot": f"Provide insights into the shape and spread of the distribution of the '{column1}' column using the violin plot. Mention the distribution, peaks, and tails in short.",
        "scatterplot": f"Describe the relationship and potential correlation between '{column1}' and '{column2}' based on the scatter plot. Mention any trends, clusters, or anomalies in short.",
        "heatmap": f"Analyze the heatmap showing the correlation matrix of selected columns. Explain how the variables relate and any significant correlations in short.",
        "pairplot": f"Interpret the pair plot of '{column1}' and '{column2}'. Discuss patterns, correlations, and any interesting observations in short.",
        "barplot": f"Explain the bar plot showing counts or averages of '{column1}' across different categories. Mention any trends, anomalies, or significant differences in short.",
        "lineplot": f"Describe the trend shown in the line plot of '{column1}' over time or another continuous variable. Discuss any trends, peaks, and patterns observed in short."
    }

    prompt = prompts.get(plot_type, "Provide an explanation.")

    with st.spinner("Generating explanation..."):
        response = co.generate(
                model='command-xlarge-nightly',
                prompt=prompt,
                max_tokens=500
            )
        explanation = response.generations[0].text.strip()
    return explanation


# Function to generate model suggestions using Cohere
def get_model_suggestions(df):

    prompt = (
        f"Based on the provided dataset, suggest 3 suitable machine learning models'. "

    )

    with st.spinner("Generating model suggestions..."):
        response = co.generate(
            model='command-xlarge-nightly',
            prompt=prompt,
            max_tokens=500
        )
        suggestions = response.generations[0].text.strip()
    return suggestions

# Function to preprocess data for correlation analysis
def preprocess_data_for_correlation(df):
    # Select only numeric columns for correlation analysis
    df_numeric = df.select_dtypes(include=[float, int])
    return df_numeric


# Main Streamlit app
def main():
    st.title("DataWizz")
    st.write("Upload a CSV or Excel file to explore visualizations and get machine learning model suggestions.")
    st.image("Data-Visualization-Final.svg", use_column_width=True)

    # File upload
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        # Read the file
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            st.write("## Data Preview")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Error reading file: {e}")
            return

        # Allow users to select columns for analysis
        selected_columns = st.multiselect("Select columns for analysis", df.columns)

        if selected_columns:
            st.write("## Analysis Options")
            analysis_type = st.radio("Select Analysis Type", ("Univariate", "Bivariate", "Correlation Heatmap"))

            if analysis_type == "Univariate" and len(selected_columns) == 1:
                column = selected_columns[0]

                st.write(f"### {column} Analysis")

                plot_type = st.selectbox("Select plot type", ["Histogram", "Boxplot", "Violin Plot", "Pie Chart"])

                if plot_type == "Histogram":
                    bin_size = st.slider("Select number of bins for histogram", min_value=5, max_value=50, value=10)
                    color = st.color_picker("Pick a color for the histogram")
                    st.write(f"#### Histogram of {column}")
                    fig = px.histogram(df, x=column, nbins=bin_size, color_discrete_sequence=[color])
                    st.plotly_chart(fig)
                    explanation = get_cohere_explanation("histogram", column)
                    st.write(f"**Histogram Explanation**: {explanation}")

                elif plot_type == "Boxplot":
                    st.write(f"#### Boxplot of {column}")
                    fig = px.box(df, y=column)
                    st.plotly_chart(fig)
                    explanation = get_cohere_explanation("boxplot", column)
                    st.write(f"**Boxplot Explanation**: {explanation}")

                elif plot_type == "Violin Plot":
                    st.write(f"#### Violin Plot of {column}")
                    fig = px.violin(df, y=column)
                    st.plotly_chart(fig)
                    explanation = get_cohere_explanation("violinplot", column)
                    st.write(f"**Violin Plot Explanation**: {explanation}")

                elif plot_type == "Pie Chart":
                    if df[column].dtype == 'object':
                        st.write(f"#### Pie Chart of {column}")
                        fig = px.pie(df, names=column)
                        st.plotly_chart(fig)
                        explanation = get_cohere_explanation("barplot",
                                                             column)  # Using barplot for pie chart explanation
                        st.write(f"**Pie Chart Explanation**: {explanation}")
                    else:
                        st.warning("Pie Chart can only be created for categorical columns.")

            elif analysis_type == "Bivariate" and len(selected_columns) == 2:
                column1, column2 = selected_columns

                st.write(f"### Bivariate Analysis between {column1} and {column2}")

                plot_type = st.selectbox("Select plot type", ["Scatter Plot", "Line Plot"])

                if plot_type == "Scatter Plot":
                    st.write(f"#### Scatter Plot of {column1} vs {column2}")
                    fig = px.scatter(df, x=column1, y=column2)
                    st.plotly_chart(fig)
                    explanation = get_cohere_explanation("scatterplot", column1, column2)
                    st.write(f"**Scatter Plot Explanation**: {explanation}")

                elif plot_type == "Line Plot":
                    st.write(f"#### Line Plot of {column1} vs {column2}")
                    fig = px.line(df, x=column1, y=column2)
                    st.plotly_chart(fig)
                    explanation = get_cohere_explanation("lineplot", column1, column2)
                    st.write(f"**Line Plot Explanation**: {explanation}")

            elif analysis_type == "Correlation Heatmap":
                df_numeric = preprocess_data_for_correlation(df)
                if len(df_numeric.columns) > 1:
                    st.write("### Correlation Heatmap")
                    corr = df_numeric.corr()
                    fig = px.imshow(corr, color_continuous_scale='RdBu_r', title="Correlation Heatmap")
                    st.plotly_chart(fig)
                    explanation = get_cohere_explanation("heatmap", "", "")
                    st.write(f"**Correlation Heatmap Explanation**: {explanation}")
                else:
                    st.warning("Correlation heatmap requires at least two numeric columns.")

            # Model suggestion section
            st.write("## Learning Model Suggestions")

            if st.button("Get Model Suggestions"):

                model_suggestions = get_model_suggestions(df)
                st.write(model_suggestions)


if __name__ == "__main__":
    main()

