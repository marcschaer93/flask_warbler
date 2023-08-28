# Warbler

Warbler is a Twitter clone built with Flask, SQLAlchemy, and Bootstrap.

## Features

- User authentication: Sign up, log in, and log out
- Profile customization: Edit username, email, and profile image
- Tweeting: Create, edit, and delete "warbles"
- Following: Follow and unfollow other users
- Feed: View a timeline of warbles from followed users

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/warbler.git
   ```

2. Change into the directory:

   ```bash
   cd warbler
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

5. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

6. Create the database:

   ```bash
   flask db_create warbler
   ```

7. Run the application:

   ```bash
   flask run
   ```

8. Open your web browser and go to `http://localhost:5000`

## Testing

To run the tests:

Make sure you are in the right ENV:

```bash
export FLASK_ENV=testing
```

instead of:

```bash
export FLASK_ENV=development
```

Then:

```bash
pytest
```

## Tech Stack

- Python
- Flask
- SQLAlchemy
- PostgreSQL
- HTML
- CSS
- Bootstrap

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

The code in this project is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for details.

## Acknowledgments

- Built following the best practices from Flask documentation.
- Inspired by [Twitter](https://twitter.com).
