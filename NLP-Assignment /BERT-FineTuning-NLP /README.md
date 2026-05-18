# BERT Fine-Tuning on IMDB Movie Reviews Dataset

## Project Overview
This project demonstrates fine-tuning of the BERT (Bidirectional Encoder Representations from Transformers) model on the IMDB Movie Reviews dataset for sentiment classification.

The project was completed as part of the Data Science Internship – February 2026 NLP Assignment.

## Objective
- Understand BERT architecture
- Perform text preprocessing
- Apply tokenization using Hugging Face tokenizer
- Fine-tune a pre-trained BERT model
- Evaluate model performance using classification metrics

## Dataset
Dataset Used:
IMDB Movie Reviews Dataset

Source:
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
4. Tokenization
5. BERT Model Loading
6. Fine-Tuning
7. Model Evaluation
8. Confusion Matrix Visualization
9. Experimental Comparison

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
Fine-tune the last two layers of BERT.

## Results
The model achieved good performance in sentiment classification using fine-tuned BERT architecture.

## Repository Structure
BERT-FineTuning-NLP/
│
├── bert_finetuning.ipynb
├── README.md
├── requirements.txt
└── dataset/

## Conclusion
This project helped in understanding transformer-based NLP models, tokenization, fine-tuning techniques, and performance evaluation for text classification tasks.

