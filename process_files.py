def count_words(filename):
    """
    Count the total number of words in a file.
    
    Args:
        filename (str): Path to the file to process
        
    Returns:
        int: Total word count
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0



def reverse_lines(input_filename, output_filename):
    """
    Reverse the order of lines in a file and save to a new file.
    
    Args:
        input_filename (str): Path to the input file
        output_filename (str): Path to save the reversed content
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(input_filename, 'r') as file:
            lines = file.readlines()
        
        # Reverse the lines
        reversed_lines = lines[::-1]
        
        with open(output_filename, 'w') as file:
            file.writelines(reversed_lines)
        
        print(f"Successfully reversed {len(lines)} lines")
        return True
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        return False
    except Exception as e:
        print(f"Error processing file: {e}")
        return False




def main():
    """Main entry point for the file processor"""
    print("File Processor v1.0")
    print("Contributors: [Add your names here]")
    print("\nAvailable operations:")
    print("1. Count words")
    print("2. Reverse lines")
    print("3. Convert to uppercase")
    print("4. Find and replace")
    
    # Test line reverser
    print("\n--- Testing Line Reverser ---")
    success = reverse_lines("data/sample.txt", "data/reversed.txt")
    if success:
        print("Check data/reversed.txt for the result!")
  if __name__ == "__main__":
    main()
  

