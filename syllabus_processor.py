# syllabus_processor.py



import re



# Patterns and keywords to skip entirely

SKIP_PATTERNS = [

  r'^Subject:', r'^Course\s*Code', r'^Program:', r'^Topic:',

  r'^Example:', r'^Used\s+in\s+the\s+form', r'^Ethyl\s+fluid',

  r'^QUESTION\s+FOR\s+PRACTICE', r'^THANK\s+YOU', r'^[A-Z]\s*\+',

]



def extract_topics(text):

  """

  Extract only the core topic headings:

   - Lines start with an uppercase letter

   - Contain at least one space (multi-word headings)

   - Do NOT contain '=', '•', '(', ')'

   - Do NOT match any SKIP_PATTERNS

   - Are between 2 and 7 words long

  """

  topics = []

  for raw in text.splitlines():

    line = raw.strip()

    if not line:

      continue



    if any(re.match(pat, line, re.IGNORECASE) for pat in SKIP_PATTERNS):

      continue



    # Skip lines with formulas or bullets

    if any(ch in line for ch in ['=', '•', '(', ')', '%', '–', '𝐻', '𝑂', '2']):

      continue



    words = line.split()

    # Must be 2–7 words

    if not (2 <= len(words) <= 7):

      continue



    if not line[0].isupper():

      continue



    if line[0].isdigit():

      continue



    clean_line = line.rstrip(':').strip()



    if clean_line not in topics:

      topics.append(clean_line)



  return topics







