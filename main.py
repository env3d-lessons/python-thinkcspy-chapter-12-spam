"""
Exercise 1: open the spam.txt file and return a count of the number of spam messages included in the dataset
            HINT: simply count sentences that starts with the word "spam"
"""
def count_spam():
    f = open('spam.txt')
    spam_count = 0
    # use the accumulator pattern here 
    return spam_count


"""
Exercise 2: Similar to exercise 12.7.3 from the textbook, return a dictionary of all words and the corresponding 
            count in all spam messages.

            For instance, if we look at the following spam messages:
                "Free prize!"
                "Urgent! claim your free prize!"
                "Free bluetooth"

            The calling the function would return:
            {'free': 3, 'prize':2, 'urgent': 1, 'bluetooth': 1, 'claim': 1, 'your': 1}
"""
def get_spam_dictionary():
    # create the words dictionary to hold the word count
    words = {}
    f = open('spam.txt')
    # make sure you checkout exercise 12.7.3 from the textbook 
    f.close()                    
    return words


"""
Exercise 3: Repeat exercise 2, but create a word dictionary for ham messages instead of spam messages
"""
def get_ham_dictionary():
    words = {}
    f = open('spam.txt')

    # the solution here is very similar to exercise 2
    
    f.close()                    
    return words


"""
Exercise 4: Return only the words that are unique to the spam dictionary.  
"""
def get_unique_spam():
    ham = get_ham_dictionary()
    spam = get_spam_dictionary()

    # we need to delete all the ham entries from the spam entry
    
    return {}

"""
Exercise 5: Return unique spam words that are greater than a certain frequencies.  
            For instances, if the unique spam words are: 
            {'free': 3, 'prize':2, 'urgent': 1, 'bluetooth': 1, 'claim': 1, 'your': 1}
            Then we would have the following interaction in the conosle:

            > get_frequent_words(2)
            ['free', 'prize']

            After you have created this function, can you tell me what are the words that
            exist in over 10% of all spam messages?
"""
def get_frequent_words(gt):
    result = []

    # use the acculmulator pattern here
    
    return result


## DO NOT MODIFY THE CODE BELOW THIS LINE
## Gradio UI for the SMS Spam Analysis
if __name__ == "__main__":

    import gradio as gr
    def ui_count_spam():
        return count_spam()

    def ui_spam_dict():
        return get_spam_dictionary()

    def ui_ham_dict():
        return get_ham_dictionary()

    def ui_unique_spam():
        return get_unique_spam()

    def ui_frequent_words(gt):
        return get_frequent_words(gt)

    with gr.Blocks() as demo:
        gr.Markdown("# SMS Spam Analysis")
        with gr.Tab("Count Spam"):
            btn = gr.Button("Count Spam Messages")
            out = gr.Number(label="Spam Count")
            btn.click(fn=ui_count_spam, outputs=out)
        with gr.Tab("Spam Word Dictionary"):
            btn2 = gr.Button("Show Spam Word Dictionary")
            out2 = gr.JSON(label="Spam Dictionary")
            btn2.click(fn=ui_spam_dict, outputs=out2)
        with gr.Tab("Ham Word Dictionary"):
            btn3 = gr.Button("Show Ham Word Dictionary")
            out3 = gr.JSON(label="Ham Dictionary")
            btn3.click(fn=ui_ham_dict, outputs=out3)
        with gr.Tab("Unique Spam Words"):
            btn4 = gr.Button("Show Unique Spam Words")
            out4 = gr.JSON(label="Unique Spam Words")
            btn4.click(fn=ui_unique_spam, outputs=out4)
        with gr.Tab("Frequent Unique Spam Words"):
            freq_input = gr.Number(label="Frequency Greater Than", value=2)
            btn5 = gr.Button("Get Frequent Words")
            out5 = gr.JSON(label="Frequent Unique Spam Words")
            btn5.click(fn=ui_frequent_words, inputs=freq_input, outputs=out5)

    demo.launch()