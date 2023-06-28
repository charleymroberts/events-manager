# Festival Events Manager

Festival Events Manager is a web-based app which enables members of a festival's organising team to enter their events information into a central database, and creates a public-facing online festival events programme using that information.

The app is displayed to users in two sections: one for staff users, and one for members of the public.

_Staff homepage on desktop and phone_
![Staff homepage laptop and phone views](doc/images/screenshot-staff-homepage.png)

_Public homepage on desktop and phone_
![Public homepage laptop and phone views](doc/images/screenshot-public-homepage.png)

A live version of the app can be accessed [on Heroku](https://festival-manager-2ef1a8933d4d.herokuapp.com/).

## Why this product is needed

Festivals are often organised by several people each working independently on their own section of the festival. For example, in the case of a folk festival, one person plans the concerts, another the workshops, another the ceilidhs/dances, another the dance teams displays, another the children's/family events.

However, they are all working to produce one single events programme for the festival as a whole. Sometimes a helping hand is needed to facilitate collaboration between several people working independently on different parts of the same project.

**Festival Events Manager** helps in two main ways:

1.  Enables event organisers to collaboratively create one central source of events information

Festival Events Manager enables each organiser to enter their events information into one central database, which can be viewed by all the organisers.  The benefits of this are:

-   _Version control_

A shared database simplifies version control as there is only one central version of the events programme, avoiding confusion about which set of information is most up to date.

-   _Facilitates information sharing between organisers_

Organisers can see each other's events during the planning process and so more easily avoid venue clashes or double booking of performers.

2.  Generates a public events programme

The Festival Events Manager takes the data entered by the organisers and, as each event is set to ‘public’ by the organisers, displays a festival events programme viewable by the public. The benefits of this are:

-   _Quicker and more flexible communication with the public_

Events are stored in ‘draft’ mode by default, and organisers can choose to add them to the public events programme as and when they are ready.

The public programme is updated in real-time, so potential attendees can get a taster of the events that will be available further in advance, increasing the likelihood that they will decide to buy a ticket and come to the festival.

This enables a more flexible way of communicating with audiences than the ‘traditional’ approach of waiting for a single, fully-completed programme document to be published in its entirety before releasing any event details to the public.

When changes need to be made (for example, if a performer calls in sick and needs to be replaced), the programme can be instantly updated, and the updates need to be made in one place only.

-   _Display information with various filters based on user need_

Using template code included in several pages, the app displays the following lists of events to the public:

 1. Full events programme (all events on all days)  
 2. Events taking place on each day (one list per day)
 3. Events featuring each performer (one list per performer)
 4. Events taking place in each venue (one list per venue)

This enables users to more easily view the information they are seeking, compared with simply reading a webpage, pdf document or paper programme listing all the events taking place. 

These lists are produced automatically without any extra action required by the organisers, saving them time and effort.

## Users of the product

### Staff users

The festival organisers. Particularly at grassroots event level, these people are often volunteers, have limited time available and have varying levels of tech knowledge. They need an interface that is quick and intuitive to use without having to make much effort to learn to use it.

### Public users

Members of the public. More specifically, this includes:

-   People deciding if they want to attend the festival, and if so, on which days they will attend
-   People who have already decided to attend, who want to find out what events there will be and make plans ahead of the festival
-   Festival attendees during the festival itself, who want to see what's on where and when and decide which event to go to next

Demographic factors such as age and experience with technology could vary widely depending on the individual festival using the software.

## Initial Planning

The following processes took place before commencing any coding.

### User Stories

The features of the app were planned by considering what the needs of a festival organiser or attendee would be in a real-life situation, thinking through what this user would therefore want to be able to do with the app, and then listing these needs as User Stories.

The User Stories used to plan this app can be viewed here: 

[User Stories as Google Sheet](https://docs.google.com/spreadsheets/d/115xDeqWRi2_llT213pvrN0uWyhkwoxC0/edit?usp=sharing&ouid=106676688339915491520&rtpof=true&sd=true) 

[User Stories as GitHub Project Board](https://github.com/users/charleymroberts/projects/2/views/1)

### Database models


### User Interface design planning

Initial wireframes were sketched on paper, based around a Bootstrap 12-column model of flexible layouts.

The main UI/UX design considerations for this app are:

| Design consideration | Reason needed |
|--|--|
| Mobile-first responsive design | Best practice |
|  | Attendees will be accessing the programme on their phones during a festival |
| Body text and layout clear to read | Lots of information being presented in the events programme, needs to be easily understood |
| Consistent layout across pages | Ease of use / Intuitiveness |
| Navigation options clearly presented on every page |  Ease of use / Intuitiveness |
| Minimalistic style with few images | Makes app quicker to load, important if large numbers of people in same place (possibly in a field with poor signal) accessing it at same time |
||Can be easily customised with customer festival's own branding. A fairly minimal style allows potential customers to imagine the app with their own branding

## Features

### Summary of functionality

Staff users can:

-   Sign up for an account
-   Log in and out of their account
-   Add new events
-   Edit events they've already added
-   Set their events to 'public' once ready to be published to the public events programme
-   View a list of all events (in draft and public form) added by all staff users
-   Add venue details (name, location, accessibility information)
-   Add performer details (name, biog, photo, web link)  
    

Public users can:

-   View the full public events programme
-   View a list of events on each day (one day per page)
-   View a list of performers
-   Click through to information about each performer, including their photo, biography and link to their website or social media, and a list of all events they are appearing in
-   View a list of venues
-   Click through to information about each venue, including location and accessibility information, and a list of all events taking place in that venue