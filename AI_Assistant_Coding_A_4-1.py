'''Problem Statement-1
Customer Email Classification
A company receives a large number of customer emails every day
and wants to automatically classify them into the following
categories:
• Billing
• Technical Support
• Feedback
• Others
Instead of training a new machine learning model, the company
decides to use prompt engineering techniques with an existing large
language model.'''
'''No. |News Headline                                    |Category
----------------------------------------------------------------------
    H1 |Government announces new education policy        |Politics
    H2 |Parliament passes new tax reform bill            |Politics
    H3 |India wins the T20 cricket series                |Sports
    H4 |Football club signs a new international player   |Sports
    H5 |Tech company launches a new AI-powered smartphone|Technology
    H6 |Cybersecurity firm reports major data breach     |Technology
    H7 |Upcoming movie breaks box office records         |Entertainment
    H8 |Popular actor announces next film project        |Entertainment'''
#Task-1: Email Classification Prompt
'''Classify the following customer emails into one of the categories: Billing, Technical Support, Feedback, Others.'''
#Prepare five short sample emails, and each belonging to one of the above categories. It should be in Tabular format with three columns: S. No., Emails, Category. Give the sample emails in the table. Like the above news headline table.
'''No. |Emails                                            |Category
----------------------------------------------------------------------
    1 |I have a question about my latest bill.           |Billing
    2 |My internet connection is not working properly.   |Technical Support
    3 |I would like to provide feedback on your service. |Feedback
    4 |Can you help me reset my account password?        |Technical Support
    5 |I have a complaint regarding my recent purchase.  |Others'''

#Task-2:
#Write a zero-shot prompt to classify a given email into one of the categories without providing any examples.
#Prompt: Classify the following email into one of the categories: Billing, Technical Support, Feedback, Others.
'''Email: "I need assistance with my account settings."
Category: Technical Support

Input: "The charges on my last invoice seem incorrect."
Output: Billing'''

#Task-3:
#Write a one-shot prompt by including one labeled email example and to classify a new email.
#Prompt: Classify the following email into one of the categories: Billing, Technical Support, Feedback, Others.
'''Example:
Email: "I have a question about my latest bill."
Category: Billing
New Email: "I would like to provide feedback on your service."
Category: Feedback

Input: "My internet connection is not working properly."
Output: Technical Support'''

#Task-4:
#Write a few-shot prompt by including two or three labeled email examples and ask the model to classify a new email.
#Prompt: Classify the following email into one of the categories: Billing, Technical Support, Feedback, Others.
'''Examples:
Email: "My internet connection is not working properly."
Category: Technical Support
Email: "I have a question about my latest bill."
Category: Billing
Email: "I would like to provide feedback on your service."
Category: Feedback
New Email: "Can you help me reset my account password?"
Category: Technical Support

Input: "I have a complaint regarding my recent purchase."
Output: Others'''

#Task-5:
#Compare the outputs obtained using zero-shot, one-shot, and few-shot prompting techniques and briefly comment on their effectiveness.
#Explanation:
'''Zero-shot prompting may provide a basic classification but can lack accuracy due to the absence of contextual examples. 
One-shot prompting improves accuracy by providing a single example, helping the model understand the task better. 
Few-shot prompting offers the highest accuracy as it provides multiple examples, allowing the model to learn patterns and nuances in classification. 
Overall, few-shot prompting is generally more effective for complex classification tasks.'''
#Comparison:
'''Zero-Shot Output: Technical Support
One-Shot Output: Technical Support
Few-Shot Output: Others'''
#Effectiveness: The few-shot prompting provided the most accurate classification due to the additional context from multiple examples.


#Problem Statement-2: Intent Classification in Chatbots queries
'''A company wants to deploy a chatbot to handle customer queries.
Each query must be classified into one of the following intents:
Account Issue, Order Status, Product Inquiry, or General Question
using prompt engineering techniques.
Tasks to be Completed
1. Prepare Sample Data
Create 6 short chatbot user queries, each mapped to one of
the four intents.
2. Zero-shot Prompting
Design a prompt that asks the LLM to classify a user query
into the given intent categories without examples.
3. One-shot Prompting
Provide one labeled query in the prompt before classifying a
new query.
4. Few-shot Prompting
Include 3–5 labeled intent examples to guide the LLM before
classifying a new query.
5. Evaluation
Apply all three techniques to the same set of test queries and
document differences in performance.'''

#1. Create a sample data of 6 short chatbot user queries and each mapped to one of the four intents.
'''No. |User Query                                      |Intent 
----------------------------------------------------------------------
    1 |I can't log into my account.                     |Account Issue
    2 |Where is my order?                               |Order Status
    3 |Do you have this product in stock?               |Product Inquiry
    4 |How can I reset my password?                     |Account Issue
    5 |What are your store hours?                       |General Question
    6 |Can I change the shipping address for my order?  |Order Status'''

#Classify the following user query into one of the intents: Account Issue, Order Status, Product Inquiry, General Question.
'''User Query: "I need help with my recent order."
Intent: Order Status'''

#Classify the following user query into one of the intents: Account Issue, Order Status, Product Inquiry, General Question.
'''Example:
User Query: "I can't log into my account."
Intent: Account Issue
New User Query: "Do you have this product in stock?"
Intent: Product Inquiry 
User Query: "Where is my order?"
Output: Order Status'''

#Classify the following user query into one of the intents: Account Issue, Order Status, Product Inquiry, General Question.
'''Examples:
User Query: "I can't log into my account."
Intent: Account Issue
User Query: "Where is my order?"
Intent: Order Status
User Query: "Do you have this product in stock?"
Intent: Product Inquiry
User Query: "What are your store hours?"
Intent: General Question
New User Query: "I need help with my recent order."
Intent: Order Status'''

#Evaluatioon: 
'''Zero-Shot Output: General Question
One-Shot Output: Order Status
Few-Shot Output: Order Status'''
#Apply all three techniques to the same set of test queries and document differences in performance.
#Effectiveness: The few-shot prompting provided the most accurate classification due to the additional context from multiple examples.
#Explanation:
'''Zero-shot prompting may provide a basic classification but can lack accuracy due to the absence of contextual examples.
One-shot prompting improves accuracy by providing a single example, helping the model understand the task better.
Few-shot prompting provides multiple examples, offering the most context and leading to the highest accuracy.
Overall, few-shot prompting is generally more effective for complex classification tasks.'''