# Reddit Subreddit Transfer

A tool I quickly whipped up to transfer subreddits between my two accounts.

## Installation

1. Clone the repository
2. Install the dependencies

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. The tool uses PRAW. You must have a **'script' app set up in _both_ your accounts** to get OAuth2.0 access tokens.
   See: https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps

2. Create `praw.ini` using the `praw.ini.example` as template. This file will contain the OAuth2.0 credentials and other info required for account access. A sample `praw.ini` will look like this:

   ```ini
   [snoo1]
   client_id=7m4y3rqvipzdzp
   client_secret=mfejcywdnkfaw_em7s4xqxjvikz-qi
   password=verygoodpassword
   username=avgcopypasta
   bot_version=0.1
   user_agent=script:SubTransfer:v%(bot_version)s (by u/%(username)s)

   [snoo2]
   client_id=3viydrmzqp47pz
   client_secret=ix_znjimwfakveqyqwfdx4m7sej-kc
   password=verygoodpassword2
   username=avgcopypaste2
   bot_version=0.1
   user_agent=script:SubTransfer:v%(bot_version)s (by u/%(username)s)
   ```

3. Run the script with your bot names as argument. Argument 1 is the source account and argument 2 is the destination account

   ```bash
   python script.py snoo1 snoo2
   ```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
