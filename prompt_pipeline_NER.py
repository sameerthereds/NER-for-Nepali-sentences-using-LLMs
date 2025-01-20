# %%
# !pip install mistralai
# !pip install huggingface_hub
# !pip install transformers
# !pip install torch
# !pip install openai
# !pip install seqeval


# K = 0, 1, 5, 10

from huggingface_hub import login
login("")
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import re
import pickle

import os
import time
from openai import OpenAI
from mistralai import Mistral
# Set up OpenAI API key
client_openai=  OpenAI(api_key="",
)

torch.backends.cuda.enable_mem_efficient_sdp(False)
torch.backends.cuda.enable_flash_sdp(False)


tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")

client_mistral = Mistral(api_key="")

import random

# Set the seed for reproducibility
random.seed(42)


#




def generate_NER(model_name,prompt):


    generated_text=""

    if model_name=="openai":
        completion = client_openai.chat.completions.create(
            model = 'gpt-4o',
           messages = [
                {'role':'system',"content": "You are an excellent linguist. "},
                # {'role':'system',"content": "तपाईं एक उत्कृष्ट भाषाविज्ञ हुनुहुन्छ। "},
                {'role': 'user', 'content':prompt}
            ],
            # temperature = 0  ,
                max_tokens=500,
                temperature=0,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                n=1
            )

        generated_text = completion.choices[0].message.content.strip()

    
    return generated_text


entities_list=["Location","Date","Person","Organization","Event"]

english_entities_dict={"Location":"Location",
                       "Date":"Date",
                       "Person":"Person",
                       "Organization":"Organization",
                       "Event":"Event"}


nepali_entities_dict={"Location":"स्थानको नाम",
                       "Date":"मिति या समय",
                       "Person":"व्यक्तिको नाम",
                       "Organization":"सङ्घ संस्थाको नाम",
                       "Event":"उत्सव, पर्व या घटनाको नाम"}

with open("output_path/train_datasets_with_tagging.pkl", "rb") as file:  # "rb" stands for read binary
    train_datasets_with_tagging = pickle.load(file)

with open("output_path/test_datasets_with_tagging.pkl", "rb") as file:  # "rb" stands for read binary
    test_datasets_with_tagging = pickle.load(file)

with open("output_path/entity_random_k_examples.pkl", "rb") as file:  # "rb" stands for read binary
    entity_random_k_examples = pickle.load(file)

with open("output_path/entity_NN_k_examples_testsentences.pkl", "rb") as file:  # "rb" stands for read binary
    entity_NN_k_examples_testsentences = pickle.load(file)


def create_prompt_with_k_NN_examples(k,entity,entity_prompt,test_sentence):

    # person_prompt ="The task is to label " + entity_prompt + " entities in the given Nepali sentence."
    person_prompt ="गर्नुपर्ने काम भनेको दिइएको नेपाली वाक्यमा " + entity_prompt + "लाई @@ ## भित्र लेबल गर्नु हो।"
    if k > 0:
        #  person_prompt+=" Below are some examples with Input and Output pairs. For the prediction, you should generate the output in the same format as in the examples. Do not give any explanations. \n Examples:"
        person_prompt+="तल वाक्य र लेबल गरेका नतिजाका केही उदाहरणहरू दिइएका छन्। वाक्यलाई लेबल गर्दा उदाहरणको जस्तै ढाँचामा मात्र गर्नुहोस्। कुनै थप व्याख्या नगर्नुहोस्। \n उदाहरणहरू:  "
    else:
        person_prompt+=" Output the whole sentence and enclose the entity within @@ and ##."
        #  person_prompt+=" पुरा वाक्यनै नतिजामा राख्नुहोस् र लेबललाई @@ र ## भित्र राख्नुहोस्।"

    k_nn_examples=[]
    count=0
    for i in entity_NN_k_examples_testsentences[entity][test_sentence]:
        k_nn_examples.append([i,entity_NN_k_examples_testsentences[entity][test_sentence][i][0]])
        count+=1
        if count ==k :
            break
 
    if k==0:
        person_prompt+="\n" + "Input: " + test_sentence + "\n" + "Output: "
        # person_prompt += "\n" + "वाक्य: " + test_sentence + "\n" + "नतिजा: "
    else:
        for i in k_nn_examples:
            
            # person_prompt+="\n" + "Input: " + i[0] + "\n" + "Output: "+ i[1] + "\n"
            person_prompt += "\n" + "वाक्य: " + i[0] + "\n" + "नतिजा: "+ i[1] + "\n"
        # person_prompt+="\n" + " Now predict the output for the following input sentence. \n Input: " + test_sentence + "\n" 
        person_prompt += "\n" + "अब तल दिईएको वाक्यलाई लेबल गर्नुहोस्।  \nवाक्य: " + test_sentence + "\n" 
    return person_prompt




def create_prompt_with_k_random_examples(k,entity,entity_prompt,test_sentence):

    person_prompt ="The task is to label " + entity_prompt + " entities in the given Nepali sentence."
    # person_prompt ="गर्नुपर्ने काम भनेको दिइएको नेपाली वाक्यमा " + entity_prompt + "लाई लेबल गर्नु हो।"
    if k > 0:
         person_prompt+="  Below are some examples with Input and Output pairs. For the prediction, you should generate the output in the same format as in the examples. Do not give any explanations. \n Examples:"
        # person_prompt+="यहाँ केही उदाहरणहरू छन्: "
    else:
        person_prompt+=" Output the whole sentence and enclose the entity within @@ and ##."
        # person_prompt+=" पुरा वाक्यनै नतिजामा राख्नुहोस् र लेबललाई @@ र ## भित्र राख्नुहोस्।"



    random_k_examples=[]
    count=0
    for i in entity_random_k_examples[entity]:
        random_k_examples.append([i,entity_random_k_examples[entity][i][0]])
        count+=1
        if count ==k :
            break

    if k==0:
        person_prompt+="\n" + "Input: " + test_sentence + "\n" + "Output: "
        # person_prompt += "\n" + "वाक्य: " + test_sentence + "\n" + "नतिजा: "
    else:
        for i in random_k_examples:
            
            person_prompt+="\n " + "Input: " + i[0] + "\n" + "Output: "+ i[1] + "\n"
            # person_prompt += "\n" + "वाक्य: " + i[0] + "\n" + "नतिजा: "+ i[1] + "\n"
        person_prompt+="\n" + " Now predict the output for the following input sentence. \n Input: " + test_sentence + "\n" 
        # person_prompt += "\n" + "वाक्य: " + test_sentence + "\n" + "नतिजा: "
    return person_prompt



start_time = time.time()
k = 10
type_examples = "random"
lang = "ENG"
output_file_name = f"k_{k}_{type_examples}_{lang}.pkl"
output_file_path = f"output/{output_file_name}"

output_dict = {}

# Load existing pickle file if it exists
if os.path.exists(output_file_path):
    with open(output_file_path, "rb") as file:
        output_dict = pickle.load(file)
    print(f"Loaded existing data with {len(output_dict)} entries.")

count = len(output_dict)

for sentence in test_datasets_with_tagging:
    if sentence in output_dict:
        # Skip sentences that are already processed
        continue
    
    temp_entity = {}
    for entity in entities_list:
        prompt = create_prompt_with_k_random_examples(k, entity, english_entities_dict[entity], sentence)
        # prompt = create_prompt_with_k_NN_examples(k, entity, nepali_entities_dict[entity], sentence)
        output = generate_NER("openai", prompt)
        temp_entity[entity] = output
        time.sleep(1)
    
    # Save result for the current sentence
    output_dict[sentence] = temp_entity

    # Save the updated dictionary to a pickle file after each sentence
    with open(output_file_path, "wb") as file:
        pickle.dump(output_dict, file)
    
    count += 1
    print(f"Processed sentence {count}: {sentence} \n {prompt}")
    print(f"Sample Output {count}:  {output}")
    print("***************************************************")
    
    # Optional: Add break condition for testing
    if count % 100== 0:
        print("Checkpoint reached, processing continues...")
        print("*******************")
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Time taken to Checkpoint: {elapsed_time:.6f} seconds")
        # break


end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken to run whole: {elapsed_time:.6f} seconds")
