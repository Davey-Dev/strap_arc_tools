import argparse

def extract_data(strap_arc_file, main_dol_file="main.dol", start_offset=3478400, expected_size=132351):
    try:
        with open(main_dol_file, 'rb') as main_dol:
            main_dol.seek(start_offset)  # Move the file pointer to the start offset
            data = main_dol.read(expected_size)

        with open(strap_arc_file, 'wb') as output:
            output.write(data)

        print("Data extracted and saved successfully to", strap_arc_file)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract data from 'main.dol'.")
    parser.add_argument("strap_arc_file", help="Path to the '.arc' file.")

    args = parser.parse_args()
    extract_data(args.strap_arc_file)
