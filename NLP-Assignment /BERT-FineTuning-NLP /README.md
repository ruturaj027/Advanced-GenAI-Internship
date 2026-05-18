# BERT Fine-Tuning on IMDB Dataset

## Project Overview
This project demonstrates fine-tuning of the BERT (Bidirectional Encoder Representations from Transformers) model on the IMDB Movie Reviews dataset for sentiment classification.

The project was completed as part of the Data Science Internship – February 2026 NLP Assignment.

## Objective
- Understand BERT for text classification
- Perform tokenization using Hugging Face tokenizer
- Fine-tune pre-trained BERT model
- Evaluate model using classification metrics

## Dataset
Dataset Used:
IMDB Movie Reviews Dataset

Dataset Link:
https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

## Technologies Used
- Python
- PyTorch
- Hugging Face Transformers
- Scikit-learn
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Workflow
1. Data Loading
2. Data Preprocessing
3. Train-Test Split
4. Tokenization using BERT Tokenizer
5. Model Building
6. Fine-Tuning BERT
7. Model Evaluation
8. Experiments and Comparison

## Model Used
- bert-base-uncased

## Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

## Experiments Performed
### Experiment 1
Freeze all BERT layers and train only classifier layer.

### Experiment 2
Fine-tune last 2 layers of BERT and compare performance.

## Results
The BERT model achieved good performance in sentiment classification on IMDB movie reviews.

## Repository Structure
BERT-FineTuning-NLP/
│
├── bert_finetuning.ipynb
├── README.md
├── requirements.txt
└── dataset/

## Conclusion
This project helped in understanding transformer-based NLP models and practical implementation of BERT fine-tuning for sentiment analysis tasks.

## Author
Ruturaj Tawde

LinkedIn:
https://linkedin.com/in/ruturaj-tawde-a9b054292

GitHub:
https://github.com/ruturaj027
