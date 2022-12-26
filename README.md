# movie_reviews_2
A Bidirectional Encoder Representations from Transformers (BERT) model for predicting the sentiment ('Positive' or 'Negative') of user-submitted movie reviews.  We fine-tuned a DistilBERT model on a dataset of IMDB movie reviews. Includes Gradio web app implementation.

The prediction is made using a Bidirectional Encoder Representations from Transformers (BERT) model, namely a fine-tuned version of DistilBERT (https://arxiv.org/abs/1910.01108)

We started with the DistilBertForSequenceClassification pre-trained model in the Hugging Face transformers library (https://huggingface.co/docs/transformers/v4.25.1/en/model_doc/distilbert#transformers.DistilBertForSequenceClassification) and DistilBertTokenizerFast (https://huggingface.co/docs/transformers/v4.25.1/en/model_doc/distilbert#transformers.DistilBertTokenizerFast)

We fine-tuned the model using the IMDb Large Movie Review Dataset (https://ai.stanford.edu/~amaas/data/sentiment/) for 3 epochs using batch sizes of 16 samples and a learning rate of 1e-5. The loss and accuracy progressed as follows:

Epoch 0001 of 0003, batch 0000 of 2188 === Loss: 0.6800

Epoch 0001 of 0003, batch 0250 of 2188 === Loss: 0.2488

Epoch 0001 of 0003, batch 0500 of 2188 === Loss: 0.4501

Epoch 0001 of 0003, batch 0750 of 2188 === Loss: 0.1309

Epoch 0001 of 0003, batch 1000 of 2188 === Loss: 0.4273

Epoch 0001 of 0003, batch 1250 of 2188 === Loss: 0.3193

Epoch 0001 of 0003, batch 1500 of 2188 === Loss: 0.5093

Epoch 0001 of 0003, batch 1750 of 2188 === Loss: 0.4583

Epoch 0001 of 0003, batch 2000 of 2188 === Loss: 0.3154

Training accuracy: 96.62 === Valid accuracy: 92.54

Epoch 0002 of 0003, batch 0000 of 2188 === Loss: 0.1179

Epoch 0002 of 0003, batch 0250 of 2188 === Loss: 0.0136

Epoch 0002 of 0003, batch 0500 of 2188 === Loss: 0.1435

Epoch 0002 of 0003, batch 0750 of 2188 === Loss: 0.0454

Epoch 0002 of 0003, batch 1000 of 2188 === Loss: 0.0768

Epoch 0002 of 0003, batch 1250 of 2188 === Loss: 0.2802

Epoch 0002 of 0003, batch 1500 of 2188 === Loss: 0.0200

Epoch 0002 of 0003, batch 1750 of 2188 === Loss: 0.1257

Epoch 0002 of 0003, batch 2000 of 2188 === Loss: 0.1308

Training accuracy: 98.76 === Valid accuracy: 92.46

Epoch 0003 of 0003, batch 0000 of 2188 === Loss: 0.0074

Epoch 0003 of 0003, batch 0250 of 2188 === Loss: 0.0039

Epoch 0003 of 0003, batch 0500 of 2188 === Loss: 0.0611

Epoch 0003 of 0003, batch 0750 of 2188 === Loss: 0.0306

Epoch 0003 of 0003, batch 1000 of 2188 === Loss: 0.1513

Epoch 0003 of 0003, batch 1250 of 2188 === Loss: 0.0014

Epoch 0003 of 0003, batch 1500 of 2188 === Loss: 0.0020

Epoch 0003 of 0003, batch 1750 of 2188 === Loss: 0.1905

Epoch 0003 of 0003, batch 2000 of 2188 === Loss: 0.1545

Training accuracy: 99.43 === Valid accuracy: 92.38
