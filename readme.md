#Acikhack2024TDDI
Acikhack2024TDDI

<div style="text-align: right;">

![mech](https://github.com/user-attachments/assets/c48ba4f4-88d8-4455-81b5-cb282e1b9d9b)
![TEKNOFEST](https://img.shields.io/badge/TEKNOFEST-blue)
![Bilisim Vadisi](https://img.shields.io/badge/B%C4%B0L%C4%B0%C5%9E%C4%B0M%20VAD%C4%B0S%C4%B0-cyan)
![Open Source TR](https://img.shields.io/badge/A%C3%A7%C4%B1k%20Kaynak%20TR-green)
![HeisenMech](https://img.shields.io/badge/HeisenMech-purple)
</div>

# 2024 Teknofest Natural Language Processing - Free Category - HeisenMech Team Code Documentation

We are sharing our work in Turkish Natural Language Processing as an open source contribution to Turkish Language and Turkish Natural Language Processing Literature.
You can check out the project presentation -> [Presentation link](https://www.canva.com/design/DAGLXYyGpM0/fBd43zF1jDLFzCSVUExoZw/edit?utm_content=DAGLXYyGpM0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

Team: HeisenMech
Team ID: 2290338


# Bring home the bacon!

In today's conditions, the field of finance is quite valuable and of vital importance for our country. It plays a key role in ensuring economic growth and stability, directing investments, and securing individuals' financial security for the future. In our project, we worked under the title of "Financial Literacy Enhancement and Investment Advice Assistant." We named our developed model "Kazim."
Our project slogan is "Kazim, we need money" :)

One of our project's interfaces, the interface we developed for "Investment advice & Technical Analysis" operations
________________________________________________________________

https://github.com/user-attachments/assets/c12afd22-1398-4dfa-97b7-c47d6882e193

________________________________________________________________

The Buy-Sell interface we developed takes "Start-End date, Cryptocurrency unit, Interval" information with the Binance API, analyzes the values of the cryptocurrency unit according to this data, and delivers the technical analysis result.
A template can be provided to the model on the backend side for technical analysis. For Buy-Sell advice, we requested headings such as "Technical Analysis, Risk Analysis, Result" from the model.

# Model & Dataset

## Model

If you're developing a model in the finance field, you need a very powerful model and dataset. For the language model, we used Meta's open-source [Llama3.1](https://llama.meta.com/) architecture. We conducted our studies primarily on Qwen2, Mixtral, and LLama architectures. Among these architectures, LLama3.1 was the one that met our needs in the most suitable format. We will be providing comparisons of the models we used within the project in this document.

## Dataset

The goal was to design our model to help all users, both amateur and professional. Therefore, we needed very diverse and comprehensive datasets. In addition, to contribute to the "Turkish Natural Language Processing" scope of the competition and Turkish literature, we developed a magnificent pipeline, the "Gök-Boru Pipeline." Thanks to this system, you can create a language model training set on "Any" topic. All you need to do is provide your documents to the pipeline. (Detailed technical explanations are available under the dataset folder)

The systems we developed to create datasets work in a fully autonomous manner.

* Web page: You can provide the system with a web page related to a topic you want to develop, and obtain a dataset where all texts are used by accessing all sub-links on the website recursively.
  
* PDF & DOCX Documents: You can even use the information in your existing documents to create a training dataset for the model. Again, all you have to do is communicate the path of the PDF document.

* Existing datasets: Do you need a dataset in Turkish but your existing documents are in a foreign language? You can translate all existing datasets in JSON format into Turkish in a way that remains faithful to the binding with this program.


## Datasets We Developed:

* Financial Queries -> https://huggingface.co/datasets/RsGoksel/Teknofest_DS_1
* Emotional News Analysis -> https://huggingface.co/datasets/RsGoksel/Sentiment
* Technical Financial Questions -> https://huggingface.co/datasets/RsGoksel/Finansal

  We developed all datasets with our fully autonomous dataset creator. We named this pipeline the "Gök-Boru Pipeline."

## Models We Trained with Our Developed Datasets:

* Financial Analysis Language Model -> https://huggingface.co/RsGoksel/FinansLLM
* Technical Analysis & Query Language Model -> We will upload soon..->
________________________________________________________

UNSLOTH, a powerful framework, was used for training models with ready training sets. With Unsloth, language models can be trained very quickly and at low cost using the PEFT method.
Colab Notebook Link ->  [![Colab](https://img.shields.io/static/v1?label=Demo&message=Colab&color=orange)](https://colab.research.google.com/drive/10mfw8Yr51JldmdqfbsfABJmTcy0XS6As?usp=sharing)
