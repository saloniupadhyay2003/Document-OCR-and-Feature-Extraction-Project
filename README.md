# **Document Classification and OCR-based Feature Extraction using LLMs**

## **Project Overview**
This project focuses on extracting and analyzing text from scanned document images using Optical Character Recognition (OCR) techniques, Natural Language Processing (NLP), and Large Language Models (LLMs). The project is divided into two tasks:

- **Task 1:** Perform OCR on document images, clean extracted text and images, conduct feature extrapolation, and compare various OCR techniques.
- **Task 2:** Summarize extracted text using LLMs, store the processed data in an SQL database, perform vectorization for retrieval, and compare different embedding models.

## **Dataset Description**
The dataset consists of scanned images belonging to 10 categories of documents:

1. Advertisements  
2. Emails  
3. Forms  
4. Letters  
5. Memos  
6. News  
7. Notes  
8. Reports  
9. Resumes  
10. Scientific Papers  

## **Project Structure**

/project-directory

│── ocr_trial.py  # Python script for OCR and NLP processing

│── documents.db   # SQL database storing extracted text and metadata

│── embedding_model_comparison.txt  # Performance comparison of embedding models

│── LLMSummary.ipynb  # Jupyter Notebook for LLM-based summarization

│── performance_report.txt  # OCR performance evaluation report

│── ocr_results.json  # Raw OCR extraction results

│── ocr_summary.json  # Summary of OCR performance



---

## **Task 1: OCR-based Text Extraction and Feature Analysis**
1. **OCR Processing**  
   - Applied Tesseract and EasyOCR to extract text from scanned images.  
   - Evaluated OCR performance in terms of accuracy, processing time, and confidence scores.  

2. **Text Cleaning & NLP Techniques**  
   - Removed noise, special characters, and irrelevant text elements.  
   - Annotated Named Entities (NER) and Part-of-Speech (POS) tags for deeper text understanding.  

3. **Performance Evaluation of OCR Models**  
   - Conducted multiple experiments to compare the effectiveness of Tesseract and EasyOCR.  
   - Results are documented in `performance_report.txt` and `ocr_summary.json`.  

---

## **Task 2: LLM-based Summarization & Data Storage**
1. **Text Summarization using LLMs**  
   - Implemented LLMs to generate concise summaries for extracted text.  
   - Compared various summarization techniques for efficiency and coherence.  

2. **Database Storage & Retrieval**  
   - Structured and stored extracted text in `documents.db` using SQL.  
   - Implemented retrieval functionality using keyword-based search queries.  

3. **Vectorization & Embedding Comparison**  
   - Converted text and images into vectorized formats for retrieval.  
   - Compared different embedding models and reported findings in `embedding_model_comparison.txt`.  

---

## **Performance Insights**
From the `performance_report.txt` and `ocr_summary.json`, key findings include:

- **OCR Performance:**
  - Tesseract and EasyOCR showed competitive confidence scores (~90%), with EasyOCR being faster.
  - Letters and reports had the highest OCR accuracy, while handwritten notes performed poorly.  

- **Embedding Model Comparisons:**
  - Various vectorization techniques were tested for improved document retrieval.
  - Results showed that transformer-based embeddings offered superior retrieval performance.

---

## **Conclusion**
This project successfully extracted, processed, and stored text data from scanned images. The integration of LLMs for summarization and vectorization enhances text retrieval efficiency. Future improvements could focus on refining OCR accuracy for handwritten text and exploring advanced embedding techniques for better document searchability.
