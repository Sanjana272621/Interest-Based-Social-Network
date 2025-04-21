# Interest-Based Social Network

## Abstract
The Interest-Based Social Network is a full-stack application that fosters community interaction through shared entertainment preferences. It enables users to follow each other, set personal preferences in genres and languages, and receive content suggestions for movies, books, and TV shows tailored to their tastes and social connections. The system aims to reduce content fatigue by filtering media recommendations in a meaningful, user-driven way.

## Introduction
In the age of abundant digital content, users often struggle to find relevant media aligned with their interests. Traditional social platforms focus on connections but lack tailored content discovery. This project bridges that gap by integrating a recommender system into a social platform, encouraging connections based on overlapping interests while delivering personalized content recommendations influenced by user preferences and the viewing/reading habits of those they follow.

## System Design
The backend database is structured with normalized tables that allow scalable and relational storage of user information, content data, and interactions. Key components include:

- USER: Contains essential user credentials and personal identifiers.

- FOLLOW: Captures the social connections between users.

- GENRES & LANGUAGES: Defines classification attributes for all content.

- MOVIES, BOOKS, TVSHOWS: Stores media details and links them to genres and languages.

-  USER_PREFERENCES: Captures individual preferences for genres and languages for each type of content.

- USER_CONSUMPTION: Logs user interactions with consumed content to prevent repeat suggestions and fine-tune recommendations.

The system uses this structured data to power a recommendation engine that considers both direct preferences and the activity of followed users.

## Features
- User signup, login, and authentication

- Follow system: follow/unfollow other users

- Browse and interact with media content (movies, books, TV shows)

- Personalized recommendations based on genre/language preferences

- Track watched movies, read books, and completed TV shows

- Multi-language support for all content
