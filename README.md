# Alex's Portfolio Website

A clean, responsive portfolio website built with Reflex because Python is life 🐍

## What's This?

This is my personal portfolio website built entirely in Python using [Reflex](https://reflex.dev). It's a modern, multi-page portfolio that showcases my work, skills, and blog posts. No JavaScript required!

The site features a responsive design with a collapsible sidebar navigation on desktop and a mobile-friendly layout with hamburger menu on smaller screens.

## Features

- **Responsive Layout**: Beautiful sidebar navigation on desktop, mobile-optimized hamburger menu
- **Multi-Page Portfolio**: Dedicated pages for About, Projects, Skills, Blog, and Contact
- **Blog System**: Markdown-based blog posts with automatic parsing and metadata extraction (includes sample posts)
- **Dark/Light Theme**: Automatic system preference detection with manual toggle
- **Modern UI**: Clean, professional design using Reflex's built-in components
- **SEO Friendly**: Proper page titles and meta information
- **Accessible**: Keyboard navigation and screen reader support

## Tech Stack

- **Framework**: [Reflex](https://reflex.dev) (Python web framework)
- **Content**: Markdown for blog posts with YAML frontmatter
- **Styling**: Reflex's built-in theming system with custom styles
- **State Management**: Reflex's reactive state system
- **Deployment**: Ready for deployment on any Python hosting platform

## Project Structure

```
retest/
├── retest/                  # Main application directory
│   ├── components/          # Reusable UI components
│   │   ├── header.py        # Desktop header with navigation
│   │   ├── sidebar.py       # Sidebar navigation
│   │   ├── layout.py        # Main layout wrapper
│   │   ├── page_nav.py      # Page-specific navigation
│   │   └── code.py          # Code syntax highlighting
│   ├── pages/               # Individual pages
│   │   ├── about.py         # About me page
│   │   ├── projects.py      # Projects showcase
│   │   ├── skills.py        # Skills and experience
│   │   ├── blog.py          # Blog listing page
│   │   ├── blog_post.py     # Individual blog post viewer
│   │   └── contact.py       # Contact information
│   ├── utils/               # Utility functions
│   │   └── blog.py          # Blog post loading and parsing
│   ├── public/              # Static content
│   │   └── blog_posts/      # Markdown blog posts
│   ├── state.py             # Application state management
│   ├── styles.py            # Custom styling definitions
│   └── retest.py            # Main app configuration
├── assets/                  # Static assets (images, etc.)
├── requirements.txt         # Python dependencies
└── rxconfig.py             # Reflex configuration
```

## Page Components

The site uses a component-based architecture with responsive design patterns:

- **Layout System**: Automatic sidebar/header on desktop, mobile drawer menu
- **Navigation**: Hierarchical navigation with section grouping
- **Content Pages**: Structured with page headers, sections, and responsive grids
- **Blog System**: Automatic blog post discovery and rendering from Markdown files
- **Code Blocks**: Syntax highlighting for technical content

## Content Management

- **Blog Posts**: Write posts in Markdown with YAML frontmatter
- **Projects**: Manage project data through the portfolio state
- **Skills**: Organize skills by category (Languages, Frameworks, Tools)
- **Contact**: Centralized contact information management

## Why Reflex?

After years of wrestling with HTML/CSS hell and JavaScript torture, I discovered Reflex and fell in love with the ability to build modern web applications entirely in Python. The component system is intuitive, the state management is straightforward, and I can leverage the entire Python ecosystem for backend functionality.

Plus, as someone who prefers Python's clarity and expressiveness, being able to build both frontend and backend in the same language is incredibly productive.

## Running Locally

If you want to check this out locally:

**Prerequisites:**
- Python 3.11+ 
- pip or pipenv

**Setup:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/unfortunatelyalex/retest.git
   cd retest
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the development server:**
   ```bash
   reflex run
   ```

5. **Open your browser:**
   Navigate to `http://localhost:3000`

The site will automatically reload when you make changes to the code.

## Adding Content

**Blog Posts:**
Create new `.md` files in `/retest/public/blog_posts/` with YAML frontmatter:

```markdown
---
title: "Your Post Title"
date: "2025-01-15"
excerpt: "A brief description of your post"
tags: ["python", "reflex", "web-development"]
---

# Your Blog Post

Content goes here...
```

**Projects:**
Update the projects list in `/retest/state.py` in the `PortfolioState` class.

**Skills:**
Modify the skills dictionary in `/retest/state.py` to reflect your expertise.

## Customization

- **Personal Info**: Update contact details and bio in `/retest/state.py`
- **Styling**: Modify themes and colors in `/retest/styles.py`
- **Navigation**: Adjust menu items in `/retest/components/sidebar.py`
- **Layout**: Customize page layouts in `/retest/components/layout.py`

---

*Built with ❤️ and Python*
