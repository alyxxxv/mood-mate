from transformers import pipeline
import streamlit as st

pipe_summarazation = pipeline("summarization", model="facebook/bart-large-xsum")
pipe_analys = pipeline("text-classification", model="rabiaqayyum/autotrain-mental-health-analysis-752423172")

def check_len(text):
  if len(text) > 1024:
    return text[:1024]
  else:
    return text

def resume_text(text):
  text = check_len(text)
  return pipe_summarazation(text, min_length=5, max_length=512)

def mental_healty(text):
  return pipe_analys(text)