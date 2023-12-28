def get_evaluation_prompt(conv_length):
    return (
        "Considering the previous conversation, do you think the answers given by chatbot are consistent? "
        "If the chatbot's response matches closely with expected answer, reply with 'TASK DONE!'. "
        f"If task is not done after {conv_length} questions, reply with 'TASK FAILED!'."
    )
