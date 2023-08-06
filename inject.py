import argparse

def inject_data(strap_arc_file, main_dol_file="main.dol", start_offset=3478400, expected_size=132351):
    try:
        with open(main_dol_file, 'r+b') as main_dol, open(strap_arc_file, 'rb') as strap_arc:
            data_to_inject = strap_arc.read()

            if len(data_to_inject) == expected_size:
                main_dol.seek(start_offset)
                main_dol.write(data_to_inject)
                print("Data injected successfully.")
            elif len(data_to_inject) < expected_size:
                padding_size = expected_size - len(data_to_inject)
                padding_data = bytes([0] * padding_size)
                main_dol.seek(start_offset)
                main_dol.write(data_to_inject + padding_data)
                print("Data injected with padding.")
            else:
                print("Injection canceled. 'strap.arc' size is greater than expected.")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inject data from 'strap.arc' into 'main.dol' at specific offset.")
    parser.add_argument("strap_arc_file", help="Path to the '.arc' file.")

    args = parser.parse_args()
    inject_data(args.strap_arc_file)
