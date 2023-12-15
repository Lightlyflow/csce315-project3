# Setup 
Items marked with `*` are not needed to run locally. If you do want to remotely host this, and don't know how to set this up, ask Aidan (email or message).

1. AWS* (See [hosting](./hosting/README.md) for more information)
   1. Account*
   2. Lightsail*
2. Docker*
3. psql
4. Python 3.11
   1. `python -m venv /path/to/venv` Create venv
   2. `source /path/to/venv/bin/activate` Activate venv
   3. `deactivate` Deactivate venv (do this when you are done with the project)
5. [Google Drive Files](https://drive.google.com/drive/folders/1p66yM6UohuBKKSXmvhRBMF2-yBbas-TA?usp=drive_link)
   1. `.env` Place in `/api` folder
      1. Database (if hosting locally):
         1. Set `DB_PASSWORD=[whatever your password is]` (Remove brackets)
         2. Set `DB_HOST=localhost`
      2. Google (no change, but may go down)
      3. Weather (no change, but may go down)
      4. Cloudinary (no change, but may go down)
   2. `p3db.pgsql` See [database](./hosting/database.md) for more info on setup
6. API Integrations
   1. [Google OAuth2](https://console.cloud.google.com/)
      1. I would replace the key with your own
      2. Needs email scope
   2. [OpenWeather](https://home.openweathermap.org/users/sign_in)
      1. I would replace the key with your own
   3. [Cloudinary](https://console.cloudinary.com/)
      1. I would replace the key with your own

