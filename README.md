# Description

Reads a text, extracts all words with a given length and writes each word line by line into a new file.

# Usage

`main.py [-h] --path PATH [--result RESULT] [--lower LOWER] [--minlength MINLENGTH]`

| Option | Short |Type | Description |
|---|---|---|---|
|--path | -p | String | Path to text file |
|--result | -r | String | Path of the result file |
| --lower | -l | Boolean | True if all output shall be lowercase, false otherwise |
| --minlength | -m | Int | The minium length of the word |

# Example

The following cmd reads text.txt, search for all words greater or equals 10 an writes each word line by line into result.txt transforming them into lowercase:

`python3 main.py -p path/to/text.txt -r path/to/result.txt -l True -m 10`

# License

MIT