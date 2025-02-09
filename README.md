**Project Overview**

This project focuses on extracting text and images from scanned documents using Optical Character Recognition (OCR) techniques. The extracted content is then processed using Natural Language Processing (NLP) techniques to clean the data and annotate named entities and part-of-speech tags. Furthermore, experiments with different OCR techniques are conducted, and their performance is compared.

**Dataset Description**

The dataset consists of scanned images categorized into the following 10 document types:

Advertisements
Emails
Forms
Letters
Memos
News
Notes
Reports
Resumes
Scientific Papers

**Project Tasks**

Task 1: OCR and Data Cleaning
Perform OCR on scanned images to extract text and images.
Clean the extracted text using NLP techniques.
Task 2: Feature Extraction
Annotate named entities.
Perform part-of-speech tagging.
Task 3: Performance Comparison of OCR Techniques
Experiment with multiple OCR tools (such as Tesseract and EasyOCR).
Evaluate their performance based on processing time, confidence score, and similarity.

**Implementation Details**

**OCR Methods Used:**

Tesseract OCR: Open-source OCR engine known for accuracy and text recognition capabilities.
EasyOCR: A deep-learning-based OCR framework that supports multiple languages.

**Performance Comparison Metrics:**

The extracted text's quality was assessed using the following criteria:

Processing Time: Measures the average time taken by each OCR engine.

Confidence Score: Indicates the reliability of the extracted text.

Text Similarity: Compares the extracted text against the original text.

**Summary of OCR Performance**

Based on the results stored in ocr_summary.json and performance_report.txt, the following insights were gathered:

Processing Time: EasyOCR was generally faster than Tesseract, especially for complex documents.

Accuracy: Tesseract performed slightly better in terms of confidence scores across most document categories.

Similarity Score: The extracted text from both OCR tools showed varying degrees of similarity with original text, with better performance observed in structured documents like Reports and Resumes.

**Files in the Project**

ocr_trial.py - The script used to run OCR processing on documents.

ocr_results.json - Contains the extracted text results from OCR models.

ocr_summary.json - Stores the comparison of Tesseract and EasyOCR performance.

performance_report.txt - Detailed report of OCR performance across different document categories.

**Conclusion**

This project provides an efficient pipeline for document digitization and text extraction using OCR and NLP techniques. The comparative study of different OCR methods allows for selecting the best model based on accuracy and processing efficiency. Future work may include integrating deep-learning-based OCR techniques for better accuracy and robustness.
