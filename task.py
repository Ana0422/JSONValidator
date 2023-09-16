import json
import jsonschema


class JsonValidator:
    def __init__(self):
        self.schema = None

    def load_schema(self, schema_file):
        """
        Load JSON schema from a file.

        Args:
            schema_file (str): Path to the schema file.

        Returns:
            bool: True if schema loading succeeds, False otherwise.
        """
        try:
            with open(schema_file, 'r') as file:
                self.schema = json.load(file)
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            return False

    def validate_schema(self, json_file):
        """
        Validate a JSON file against the loaded schema.

        Args:
            json_file (str): Path to the JSON file to be validated.

        Returns:
            bool: True if validation succeeds, False otherwise.
        """
        if self.schema:
            try:
                with open(json_file, 'r') as file:
                    data = json.load(file)
                jsonschema.validate(data, self.schema)
                return True
            except (FileNotFoundError, json.JSONDecodeError, jsonschema.exceptions.ValidationError):
                return False
        else:
            return False


if __name__ == "__main__":
    validator = JsonValidator()

    # Load the schema from a schema file
    schema_loaded = validator.load_schema('schema.json')

    if schema_loaded:
        # Validate a JSON file against the loaded schema
        is_valid = validator.validate_schema('data.json')

        if is_valid:
            print("JSON validation succeeded.")
        else:
            print("JSON validation failed.")
    else:
        print("Failed to load the schema.")
