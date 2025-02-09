# -*- coding: utf-8 -*-
"""OCR-TRIAL1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1urTz8lULFxPdDqR2RgYbWWBsGFRMDS_Q
"""

# Install OpenCV
!pip install opencv-python

# Install Tesseract OCR
# Windows
!pip install pytesseract
# Mac/Linux

!pip install spacy
!python -m spacy download en_core_web_sm

!sudo apt install tesseract-ocr
!sudo apt install libtesseract-dev



from google.colab import drive
drive.mount('/content/drive')

!pip install easyocr

import os
import json
import cv2
import time
import pytesseract
import easyocr
import spacy
import numpy as np
from PIL import Image
from collections import defaultdict
from difflib import SequenceMatcher
from concurrent.futures import ThreadPoolExecutor
import re

# Initialize OCR engines and NLP model
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
reader = easyocr.Reader(['en'])
nlp = spacy.load('en_core_web_sm')

DOCUMENT_CATEGORIES = [
    'ADVE', 'Email', 'Form', 'Letter', 'Memo',
    'News', 'Note', 'Report', 'Resume', 'Scientific'
]

class OCRComparison:
    def __init__(self, img_dir, output_dir):
        self.img_dir = img_dir
        self.output_dir = output_dir
        self.performance_metrics = defaultdict(dict)

    def clean_text(self, text):
        """Clean text by removing extra whitespace and unwanted characters."""
        return re.sub(r'\s+', ' ', text).strip()

    def annotate_text(self, text):
        """
        Annotate named entities and part-of-speech (POS) tags from text using spaCy.
        Returns two lists: named_entities and pos_tags.
        """
        doc = nlp(text)
        named_entities = [(ent.text, ent.label_) for ent in doc.ents]
        pos_tags = [(token.text, token.pos_) for token in doc]
        return named_entities, pos_tags

    def extract_text_tesseract(self, img):
        """Extract text using Tesseract OCR"""
        try:
            start_time = time.time()
            text = pytesseract.image_to_string(img)
            processing_time = time.time() - start_time
            return text.strip(), processing_time
        except Exception as e:
            print(f"Tesseract error: {str(e)}")
            return "", 0

    def extract_text_easyocr(self, img):
        """Extract text using EasyOCR"""
        try:
            start_time = time.time()
            results = reader.readtext(img)
            text = ' '.join([result[1] for result in results])
            processing_time = time.time() - start_time
            return text.strip(), processing_time
        except Exception as e:
            print(f"EasyOCR error: {str(e)}")
            return "", 0

    def calculate_confidence_score(self, text):
        """Calculate a confidence score based on text quality."""
        if not text:
            return 0
        words = text.split()
        avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
        length_score = min(1.0, avg_word_length / 5.0)
        word_count_score = min(1.0, len(words) / 100.0)
        return (length_score + word_count_score) / 2

    def process_image(self, category, filename):
        """Process a single image with both OCR methods and perform text cleaning and annotation."""
        img_path = os.path.join(self.img_dir, category, filename)
        img = cv2.imread(img_path)

        # Extract text with both OCR methods
        tesseract_text, tesseract_time = self.extract_text_tesseract(img)
        easyocr_text, easyocr_time = self.extract_text_easyocr(img)

        # Clean extracted text
        tesseract_text_cleaned = self.clean_text(tesseract_text)
        easyocr_text_cleaned = self.clean_text(easyocr_text)

        # Annotate text with named entities and POS tags
        tesseract_entities, tesseract_pos_tags = self.annotate_text(tesseract_text_cleaned)
        easyocr_entities, easyocr_pos_tags = self.annotate_text(easyocr_text_cleaned)

        # Calculate confidence scores
        tesseract_confidence = self.calculate_confidence_score(tesseract_text_cleaned)
        easyocr_confidence = self.calculate_confidence_score(easyocr_text_cleaned)

        # Calculate similarity between the two outputs
        similarity = SequenceMatcher(None, tesseract_text_cleaned, easyocr_text_cleaned).ratio()

        return {
            'filename': filename,
            'tesseract': {
                'text': tesseract_text_cleaned,
                'entities': tesseract_entities,
                'pos_tags': tesseract_pos_tags,
                'time': tesseract_time,
                'confidence': tesseract_confidence
            },
            'easyocr': {
                'text': easyocr_text_cleaned,
                'entities': easyocr_entities,
                'pos_tags': easyocr_pos_tags,
                'time': easyocr_time,
                'confidence': easyocr_confidence
            },
            'similarity': similarity
        }

    def process_category(self, category):
        """Process all images in a category"""
        category_dir = os.path.join(self.img_dir, category)
        results = []

        # Get first 25 images
        image_files = [f for f in os.listdir(category_dir)
                      if f.endswith(('.jpg', '.png', '.jpeg'))][:25]

        # Process images in parallel
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.process_image, category, filename)
                      for filename in image_files]
            results = [future.result() for future in futures]

        return results

    # The remaining methods for analyzing results, saving data, and generating the report are unchanged

    def run(self):
        """Run the OCR comparison"""
        all_results = {}

        for category in DOCUMENT_CATEGORIES:
            print(f"Processing category: {category}")
            all_results[category] = self.process_category(category)

        # Analyze results
        summary = self.analyze_results(all_results)

        # Save results
        self.save_results(all_results, summary)
        print(f"Results saved to {self.output_dir}")

def main():
    img_dir = "/content/drive/MyDrive/dataset"
    output_dir = "/content/drive/MyDrive/dataset/TRIAL2"

    ocr_comparison = OCRComparison(img_dir, output_dir)
    ocr_comparison.run()

if __name__ == "__main__":
    main()

