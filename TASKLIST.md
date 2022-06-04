## ℹ️ What is this?
This is a quick archive of my current progress. It is a list of the parts of geoguessr's website that have been implemented so far
and a list of the ones remaining. 

It is structured using geoguessr's main tabs and pages as sections and hierarchically splitting it
into subsections of additional pages and functionalities.

## ✅ What does a tick represent
A green tick ✅ is given when a functionality has been implemented in the wrapper. For a functionality
to be considered as implemented, the following tasks must first be completed:
- Researching all endpoints relating to the functionality
- Examining the related HTTP requests, the inputs and the JSON outputs
- Creating dataclasses for the JSON outputs
- Adding client methods to access and use the functionality
- Testing the functionality

When all the functionalities of a subsection or section have been implemented, it will
receive ☑ tick.

# 📖 Task list
```
Geoguessr 🌍
├── Home
│   ├── Ongoing games
│   │   └── TODO
│   ├── Friends ☑
│   │   ├── Get friends list ✅
│   │   ├── Get pending friend requests ✅
│   │   ├── Check friend status of user ✅
│   │   ├── Send friend request ✅
│   │   ├── Accept friend request ✅
│   │   └── Remove friend ✅
│   ├── Activities
│   │   └── TODO
│   ├── My Maps
│   │   ├── Browse created ✅
│   │   ├── Create a map
│   │   ├── Edit a map
│   │   ├── Unpublish a created map ✅
│   │   └── Publish a created map ✅
│   ├── Liked Maps ☑
│   │   ├── Browse liked maps ✅
│   │   ├── Like a map ✅
│   │   └── Unlike a map ✅
│   └── Map browsing ☑
│       ├── Browse recommended/similar to other map ✅
│       ├── Browse official ✅
│       ├── Browse featured ✅
│       ├── Browse popular random ✅
│       ├── Browse popular montly ✅
│       ├── Browse popular all time ✅
│       ├── Browse new ✅
│       ├── Browse by author ✅
│       ├── Browse personalized ✅
│       └── Browse countries ✅
├── Competitive
│   ├── Season ✅
│   │   ├── Season Ranking ✅
│   │   ├── Previous Season ✅
│   │   ├── Current Season ✅
│   │   └── Next Season (?)
│   ├── Leaderboard ✅
│   ├── Events ✅
│   ├── Duels
│   ├── City Streak
│   ├── Battle Royal Countries
│   └── Battle Royal Distance
├── Play with friends
│   ├── Challenge a friend
│   ├── List parties
│   ├── Start new party
│   ├── Edit Party
│   └── etc... TODO
├── Classic
│   ├── Explorer mode ✅
│   ├── Streaks
│   ├── Daily Challenge
│   ├── Pro Leagues
│   ├── Explorer maps ✅
│   └── Game
│       ├── Start game from map
│       │   └── Play game
│       ├── Get game results
│       └── Challenge
│           ├── Create Challenge from map ✅
│           ├── Invite friends ✅
│           ├── Get challenge info ✅
│           └── Get challenge results
├── Search ☑
│   ├── Search maps ✅
│   ├── Search people ✅
│   └── Search all ✅
├── Profile
│   ├── Profile information ✅
│   ├── Subscription ✅
│   ├── Invoices ✅
│   ├── Trophy Case ✅
│   ├── Badges ☑
│   │   ├── Recent badges ✅
│   │   ├── All badges ✅
│   │   └── Obtained badges ✅
│   ├── Statistics ☑
│   │   ├── Simple statistics ✅
│   │   └── Advanced statistics ✅
│   ├── Competitions ✅
│   ├── Explored countries ✅
│   └── Edit Profile
├── Notifications
│   └── TODO
├── Streams
│   └── TODO
├── Mapillary Free version
│   └── TODO
└── Quiz
    ├── Join quiz
    ├── Create quiz
    └── etc... TODO
```


# 📖 Task list (RAW version)
```
Geoguessr 🌍
# Home
## Ongoing games
### TODO

## Friends ☑
### Get friends list ✅
### Get pending friend requests ✅
### Check friend status of user ✅
### Send friend request ✅
### Accept friend request ✅
### Remove friend ✅

## Activities
### TODO

## My Maps
### Browse created ✅
### Create a map
### Edit a map
### Unpublish a created map ✅
### Publish a created map ✅

## Liked Maps ☑
### Browse liked maps ✅
### Like a map ✅
### Unlike a map ✅

## Map browsing ☑
### Browse recommended/similar to other map ✅
### Browse official ✅
### Browse featured ✅
### Browse popular random ✅
### Browse popular montly ✅
### Browse popular all time ✅
### Browse new ✅
### Browse by author ✅
### Browse personalized ✅
### Browse countries ✅

# Competitive
## Season ✅
### Season Ranking ✅
### Previous Season ✅
### Current Season ✅
### Next Season (?)
## Leaderboard ✅
## Events ✅
## Duels
## City Streak
## Battle Royal Countries
## Battle Royal Distance

# Play with friends
## Challenge a friend
## List parties
## Start new party
## Edit Party
## etc... TODO

# Classic
## Explorer mode ✅
## Streaks
## Daily Challenge
## Pro Leagues
## Explorer maps ✅
## Game
### Start game from map
#### Play game
### Get game results
### Challenge
#### Create Challenge from map ✅
#### Invite friends ✅
#### Get challenge info ✅

# Search ☑
## Search maps ✅
## Search people ✅
## Search all ✅

# Profile
## Profile information ✅
## Subscription ✅
## Invoices ✅
## Trophy Case ✅
## Badges ☑
### Recent badges ✅
### All badges ✅
### Obtained badges ✅
## Statistics ☑
### Simple statistics ✅
### Advanced statistics ✅
## Competitions ✅
## Explored countries ✅
## Edit Profile

# Notifications
## TODO

# Streams
## TODO

# Mapillary Free version
## TODO

# Quiz
## Join quiz
## Create quiz
## etc... TODO

```