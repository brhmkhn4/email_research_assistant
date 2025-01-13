def user_input_search_terms():
    search_terms = []
    prompt_user = ""
    while True:
                           
        try:
            if prompt_user == "":
                prompt_user = "Please enter what would you like to search for. For example, What is the best field to make AI apps for?"
            else: 
                 prompt_user = "Noted, Please enter another search term if you wish or type q to proceed."            

            user_input = input(f"{prompt_user}")

              # Validate input
            if not user_input:
                print("Input cannot be empty. Please try again.")
                continue

            if user_input.lower() in ["quit", "exit", "q"]:
                return search_terms

            search_terms.append(user_input)
            # print(f"User Search Terms{search_terms}")
          
        except (KeyboardInterrupt, EOFError):
            print("\nInput interrupted. Returning collected search terms.")
            return search_terms