import torch
import transformers
from transformers import DistilBertTokenizerFast
from transformers import DistilBertForSequenceClassification
import gradio as gr

# Load the pre-trained tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained('./model_save/',local_files_only=True)

# Load the pre-trained DilBERT model
model = DistilBertForSequenceClassification.from_pretrained('./model_save/',local_files_only=True)
model.eval()

# Define a predict function
def predict(text):
    encoding=tokenizer(text,return_tensors='pt')
    input_ids, attention_mask = encoding['input_ids'],encoding['attention_mask']
    outputs = model(input_ids,attention_mask=attention_mask)
    logits = outputs['logits']
    pred_label = torch.argmax(logits,1)[0]
    return 'Positive' if pred_label > 0.5 else 'Negative'

# Initialize the Gradio interface
title = "Write a movie review"
description = "Enter a review for a movie you've seen.  This tool will try to guess whether your review is positive or negative."
gr.Interface(fn=predict, 
             inputs="text",
             outputs="label",
             title = title,
             description = description,
              ).launch()