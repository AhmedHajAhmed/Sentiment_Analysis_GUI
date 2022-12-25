# Sentiment Analysis GUI Report 
### Team Members: Vivek Mittal-Henkle, Ahmed Haj Ahmed, Pau Pinya-Nadal
#### This is our final project for the course "CS105 Introduction to Computer Science"

### Problem  
Sentiment analysis is a branch of computer science that identifies and extracts subjective information from text using natural language processing and computational linguistics. This is a critical problem in natural language processing because it enables the automatic understanding of large amounts of unstructured text input. However, because natural language is inherently imprecise and subjective, computers struggle to do sentiment analysis effectively. This might lead to mistakes and misconceptions, which can be disastrous in applications like customer service or market research. Furthermore, sentiment analysis frequently relies on labeled training data, which can be time-consuming and expensive, and can introduce bias if the human is not diverse or consistent.

### Motivation 
Despite these difficulties, computer science sentiment analysis is still a significant and active topic of study. A sentiment analysis project can be undertaken for a variety of reasons, such as the ability to automatically analyze vast amounts of text data, the opportunity to learn important lessons from consumer feedback, and the enhancement of natural language processing systems.

An organization may utilize a sentiment analysis project, for instance, to automatically classify customer reviews of a good or service. This would enable it to quickly and precisely determine the sentiment of its customers and take the necessary action. Using positive reviews to develop marketing materials or responding to negative reviews to increase customer satisfaction are two examples.

The potential to learn important lessons from text data is another reason to do a sentiment analysis project. Researchers and analysts can better comprehend people's thoughts and emotions on a variety of issues by automatically extracting sentiment data from text. This could be used to investigate public opinion on a certain subject or to spot patterns and trends in client feedback.

Initially, we wanted to look at a set of tweets and apply sentiment analysis to detect which were racist or hateful. However, after aligning our goals with the scope of this class, we decided to create a simple GUI that shows where the majority of sentiment is coming in some text, allowing someone to become familiar with sentiment analysis who is not already. It can also be used to check if the pattern sentiment analysis algorithm is flawed or biased in certain cases.

### Results 
When our GUI is launched, a blue window appears with a text box with the placeholder text ‘please enter some text’ and a button. We can then enter any text. We enter “I usually feel good but today I feel awful”.

After pressing the button, our GUI shows the resulting sentiment of -0.183. This is reasonable given the fact that the text contains “awful,” which has very negative sentiment, but also “good,” which has positive sentiment. “Awful” is highlighted in red since it had the most negative sentiment in the text.

Next, we enter “Apples and oranges are fruits,” which outputs a sentiment of 0.0 and has no words highlighted. This output is expected.

Finally, we enter “This book is very exciting,” which outputs a sentiment of .39 and the words “very exciting” highlighted in green. The sentiment result of .39 makes sense given that the book is neither ‘a little exciting’ nor the ‘best book ever’. The fact that “very exciting” was highlighted in green stems from the fact that “very exciting” has a more positive sentiment than either “very” or “exciting” by themselves.

### Conclusion 
For this project, we were excited by the prospect of using sentiment analysis in order to detect racist or hate speech in tweets. However, after rethinking our scope, we decided to make a simple GUI that shows which word or words in a phrase contribute most to its sentiment using the pattern and Tkinter libraries. This functionality allows users to better understand how sentiment analysis works and test different cases to see if the pattern algorithm has any biases. Our final code includes a text box for entering a phrase and a button that will show the total sentiment and print the phrase showing the highest contributing word(s) in red or green. We also encountered many challenges in implementing our GUI, but learned valuable problem-solving skills that we will take to future projects.
