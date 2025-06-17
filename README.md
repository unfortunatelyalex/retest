# Alex's Portfolio Dashboard

Just a personal portfolio site built with Reflex because why not 🤷‍♂️

## What's This?

This is basically my attempt at building a modern portfolio dashboard that actually looks decent. It's an app or website that shows off my portfolio that I've ever dreamed of and connects to various APIs to display real-time data.

The whole thing is built in Python using [Reflex](https://reflex.dev) - which is pretty cool because I don't have to deal with JS/TS (thank god).

## Features

- **Dashboard Layout**: Clean 2x2 grid on desktop and 1x4 on mobile
- **GitHub Integration**: Shows my actual contribution graph pulled from GitHub's API
- **Spotify Integration**: Displays what I'm currently listening to (if anything)
- **Discord Avatar**: Automatically pulls my Discord profile picture from a specific server
- **Live Clock**: Because why not show the current time
- **Blog Section**: No posts in this repo, but you can add your own Markdown files in the `public/blog_posts` directory and it will automatically show up
- **Dark/Light Theme**: System preference support

## Tech Stack

- **Framework**: Reflex (Python web framework)
- **APIs**: GitHub GraphQL, Spotify Web API, Discord API
- **Styling**: Built-in Reflex components with custom CSS
- **Deployment**: TBD (probably on my own server or something)

## Project Structure

```
retest/
├── site/
│   ├── components/        # Individual dashboard widgets
│   │   ├── github_widget.py
│   │   ├── spotify_widget.py
│   │   ├── blog_widget.py
│   │   └── ...
│   ├── pages/            # Main pages
│   │   ├── index.py      # Dashboard page
│   │   ├── blog.py       # Blog listing
│   │   └── blog_post.py  # Individual blog posts
│   └── state.py          # All the state management logic
├── public/
│   └── blog_posts/       # Markdown blog posts
└── assets/               # Static files
```

## Components

Each widget is its own component that handles its own state and API calls:

- **GitHub Widget**: Fetches and displays contribution data in the regular contribution graph style like you see on GitHub
- **Spotify Widget**: Shows what I'm currently listening to, if anything and displays the album cover
- **About Section**: Basic info and contact links
- **Blog Widget**: Preview of latest blog posts
- **Stats Widget**: Random coding stats (might be fake, might not be)

## APIs Used

- **GitHub GraphQL API**: For contribution data and profile info
- **Spotify Web API**: For current playing track
- **Discord API**: For profile avatar

All API keys are stored in environment variables (obviously).

## Why Reflex?

Honestly, I was never really a fan of HTML/CSS or JavaScript. My first website can be found [here](https://alexdot.me) but I 

  was tired of dealing with React/Next.js and wanted to try something different. Reflex lets me build the entire frontend and backend in Python, which is pretty neat. Plus, the component system is actually quite nice once you get used to it.

The state management is straightforward, and I can integrate with any Python library I want for the backend stuff.

## Running Locally

If you want to run this for some reason:

(This assumes you have Python 3.12+ and pip installed)

```bash
git clone https://github.com/unfortunatelyalex/retest.git
cd retest
```

Configure your environment variables in `.env.example` and rename it to `.env`.
```bash
cp .env.example .env
```

Then set up a virtual environment and install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
reflex run
```

The site should now be running at `http://localhost:3000`.

You'll need to set up your own API keys in a `.env` file, but honestly this is just my personal site so probably not worth it.

---

*Built with ☕ and questionable life choices*
