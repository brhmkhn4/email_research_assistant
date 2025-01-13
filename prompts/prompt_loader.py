# general template for loading prompt md file, just give file name while calling this function
def load_prompt(prompt_name):
      with open(f"{prompt_name}", "r") as file:
          return file.read()

# import os

# def load_prompt(prompt_name):
#     try:
#         file_path = os.path.relpath(prompt_name)  # Convert to absolute path
#         with open(file_path, "r") as file:
#             return file.read()
#     except FileNotFoundError:
#         print(f"Error: The file '{file_path}' was not found.")
#         return None
#     except PermissionError:
#         print(f"Error: Permission denied when trying to read '{file_path}'.")
#         return None
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         return None


