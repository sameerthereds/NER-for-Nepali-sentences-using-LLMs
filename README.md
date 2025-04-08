# NER for Nepali Sentences using OpenAI GPT-4

This repository presents a Named Entity Recognition (NER) system for Nepali sentences using the **OpenAI GPT-4** model. It identifies entities such as persons, locations, organizations, dates, and events within Nepali text.

## Overview

The NER system leverages **OpenAI GPT-4**, a powerful large language model, and is evaluated on Nepali sentence datasets using standard train-test splits. In addition to traditional evaluation metrics, the system includes a **self-verification mechanism** to verify the model's outputs, enhancing reliability and relevance.

## Sample Prompts

### Prompt in English (1 shot)

The task is to label Organization entities in the given Nepali sentence.  Below are some examples with Input and Output pairs. 
For the prediction, you should generate the output in the same format as in the examples.  Do not give any explanations. 

**Examples:**

**Input**:  
  तर , भारत को राष्ट्रिय टोली बाट खेलि सकेका खेलाडी लाई बिसीसीआई ले अन्य देश को लिग मा खेल्ने अनुमति दिँदैन ।  
  **Output**:  
  तर , @@भारत## को राष्ट्रिय टोली बाट खेलि सकेका खेलाडी लाई बिसीसीआई ले अन्य देश को लिग मा खेल्ने अनुमति दिँदैन ।

Now predict the output for the following input sentence:

**Input**:  
अङ्क तालिका मा युएई शीर्षस्थान मा छ भने नेपाल दोस्रो स्थान मा छ ।




### Prompt in Nepali (1 shot)

गर्नुपर्ने काम भनेको दिइएको नेपाली वाक्यमा सङ्घ संस्थाको नाम नामलाई @@ ## भित्र लेबल गर्नु हो।  
तल वाक्य र लेबल गरेका नतिजाका केही उदाहरणहरू दिइएका छन्।  
**वाक्यलाई लेबल गर्दा उदाहरणको जस्तै ढाँचामा मात्र गर्नुहोस्। कुनै थप व्याख्या नगर्नुहोस्।**

**उदाहरणहरू:**

 **वाक्य**:  
  तर , भारत को राष्ट्रिय टोली बाट खेलि सकेका खेलाडी लाई बिसीसीआई ले अन्य देश को लिग मा खेल्ने अनुमति दिँदैन ।  
  **नतिजा**:  
  तर , @@भारत## को राष्ट्रिय टोली बाट खेलि सकेका खेलाडी लाई बिसीसीआई ले अन्य देश को लिग मा खेल्ने अनुमति दिँदैन ।

अब तल दिईएको वाक्यलाई लेबल गर्नुहोस्:

**वाक्य**:  
अङ्क तालिका मा युएई शीर्षस्थान मा छ भने नेपाल दोस्रो स्थान मा छ ।




## Features

- **NER for Nepali**: Detects named entities in Nepali sentences (e.g., people, locations, organizations, dates, events).
- **Powered by GPT-4**: Utilizes OpenAI’s GPT-4 for robust language understanding and generation.
- **Self-Verification**: Integrates a mechanism to validate model predictions for improved accuracy.
- **Evaluation Setup**: Uses a train-test split and standard performance metrics to assess the model.