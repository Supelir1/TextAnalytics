# Semi-automatic evaluation of German party manifestos

### Requirements:
Install all requirements with pip:
> pip install -r .\requirements.txt

### Structure
* topic_classification.ipynb
  * The final pipline for classification and summarization
* data_exploration
  * All files used to find out different properties of the data
* diagrams
  * A selection of graphics for different presentations
* resources
  * Here are the party programs of the German parties for the year 2021 in text form
* summary
  * The code for the extractive summarization
---
### Distribution of work
Generally, we tried to work in groups, so the following is an approximation, 
of which persons are mainly responsible for the corresponding files.

* Tobias Kalmbach
  * [main.ipynb](data_exploration/main.ipynb)
  * [main.py](data_exploration/main.py)
  * [text_summarization.ipynb](summary/text_summarization.ipynb)

* Fabian Karl
  * [topic_modeling_playground.ipynb](data_exploration/topic_modeling_playground.ipynb)
  * [custom_stopwords.txt](data_exploration/custom_stopwords.txt)
  * [topic_classification.ipynb](topic_classification.ipynb)

* Tim Knittel

* Nicolas Zellner
  * [Preprocessing.py](data_exploration/Preprocessing.py)

### Notes
* This project was created on [github](https://github.com/Supelir1/TextAnalytics)