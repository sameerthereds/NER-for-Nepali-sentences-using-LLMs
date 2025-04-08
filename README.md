# NER-for-Nepali-sentences-using-LLMs

# NER for Nepali Sentences using OpenAI GPT-4

This repository presents a Named Entity Recognition (NER) system for Nepali sentences using the **OpenAI GPT-4** model. The system performs entity recognition on Nepali text, identifying entities such as persons, locations, organizations, dates, and events within a sentence.

## Overview

The NER model is based on the **OpenAI GPT-4** (a powerful large language model) and has been evaluated using a training and testing set of Nepali sentences. In addition to the traditional evaluation metrics, the system also incorporates a **self-verification** mechanism to verify the accuracy of the LLM output. This ensures that the model's predictions are more reliable and relevant.

## Sample Prompts

Prompt in English
The task is to label Location entities in the given Nepali sentence.  Below are some examples with Input and Output pairs. 
For the prediction, you should generate the output in the same format as in the examples.  Do not give any explanations. 
Examples:
Input: तर , भारत को राष्ट्रिय टोली बाट खेलि सकेका खेलाडी लाई बिसीसीआई ले अन्य देश को लिग मा खेल्ने अनुमति दिँदैन ।
Output: तर , @@भारत## को राष्ट्रिय टोली बाट खेलि सकेका खेलाडी लाई बिसीसीआई ले अन्य देश को लिग मा खेल्ने अनुमति दिँदैन ।
Now predict the output for the following input sentence. 
Input: अङ्क तालिका मा युएई शीर्षस्थान मा छ भने नेपाल दोस्रो स्थान मा छ ।

Prompt in Nepali
गर्नुपर्ने काम भनेको दिइएको नेपाली वाक्यमा स्थानको नामलाई @@ ## भित्र लेबल गर्नु हो।तल वाक्य र लेबल गरेका नतिजाका केही उदाहरणहरू दिइएका छन्।
वाक्यलाई लेबल गर्दा उदाहरणको जस्तै ढाँचामा मात्र गर्नुहोस्। कुनै थप व्याख्या नगर्नुहोस्। 
उदाहरणहरू: 
वाक्य: तर , भारत को राष्ट्रिय टोली बाट खेलि सकेका खेलाडी लाई बिसीसीआई ले अन्य देश को लिग मा खेल्ने अनुमति दिँदैन ।
नतिजा: तर , @@भारत## को राष्ट्रिय टोली बाट खेलि सकेका खेलाडी लाई बिसीसीआई ले अन्य देश को लिग मा खेल्ने अनुमति दिँदैन ।
अब तल दिईएको वाक्यलाई लेबल गर्नुहोस्। 
वाक्य: अङ्क तालिका मा युएई शीर्षस्थान मा छ भने नेपाल दोस्रो स्थान मा छ ।

## Features

- **NER for Nepali**: Recognizes named entities in Nepali sentences, such as people, locations, organizations, dates, and events.
- **OpenAI GPT-4 Model**: Utilizes OpenAI's GPT-4 for generating predictions and handling complex language understanding tasks.
- **Self-Verification**: Implements a self-verification technique to cross-check the accuracy of the model's predictions. This step improves the reliability of the NER results.
- **Evaluation**: The model is evaluated using a train-test split, with performance metrics to assess its accuracy and effectiveness.

