# TextSummerizer-NLP
Text Summarization is a crucial and top Natural Language Processing task that involves generating concise and coherent summaries of longer pieces of text. It enables quick information retrieval and comprehension, making it invaluable for dealing with large volumes of textual data.

## Objective
This project aims to develop an abstractive or extractive text summarization model capable of creating informative and concise summaries from lengthy text documents. Before that, we saw we could use langchain to provide text summarization using OpenAI API though [NTA-LLM](https://github.com/parham075/NTA-LLM). now I am going to train a transformer model using transfer learning and try to fine-tune it to tackle the problem.

## Usecase:
The output model from this project can be useful for academic researcher, students, and anybody who doesn't have much time to read large amounts of text and looking for a solution to summerize their articles, course slides, etc. 

## Dataset Overview and Data Preprocessing

This project requires a dataset containing articles or documents with human-generated summaries. Data preprocessing involves tokenizing the text, handling punctuation, and creating input-target pairs for training.
For this project I used a well-known dataset from `Hugging Face`:
- [Samsum](https://huggingface.co/datasets/samsum?row=0)

## Model(s)
| Model| Weights|
| --- | --- |
|pre-trained model | [pegasus-cnn_dailymail](https://huggingface.co/google/pegasus-cnn_dailymail)|

## Queries for Analysis

Generate summaries for long articles or documents.
Evaluate the quality of generated summaries using ROUGE and BLEU metrics.
Key Insights and Findings

The text summarization model will successfully generate concise and coherent summaries, improving the efficiency of information retrieval and enhancing the user experience when dealing with extensive textual content.
