## Chat Api Documentation

An API (Application Programming Interface) is just like a web-site that communicates raw data (like JSON) instead of well structured and designed data (like HTML/CSS). You can see an API as the poor-version of a standard website meant to be used by computers, not by human beings.

- An API is designed for communication between machines
- A standard website has a nicer human-readable interface as it's designed for humans. You can see a website as a **"AHI"** (Application Human Interface).

APIs are everywhere and proposed by all serious services. Here you'll read your first API documentation on a very simple example, the wagon-chat API!

#### Base URL

The base URL of the API is `https://wagon-chat.herokuapp.com/`. Feel free to test the API using [Postman](https://www.getpostman.com/) or in the JS console directly.

#### Get messages `GET '/general/messages'`

```json
{
  "channel": "general",
  "messages": [
    {
      "id": 1,
      "author": "Smith",
      "content": "Hey we are excited to see you here",
      "channel": "general",
      "created_at": "2023-09-11T15:11:46.104Z",
      "updated_at": "2023-09-11T15:11:46.104Z"
    },
    {
      "id": 2,
      "author": "Andrew",
      "content": "Dinner?",
      "channel": "general",
      "created_at": "2022-01-03T11:53:59.323Z",
      "updated_at": "2022-01-03T11:53:59.323Z"
    }
  ]
}
```

#### Post a comment `POST '/general/messages'`

Will post a new comment on our API's database.
In the request body, you have to send the details of the post, in the following JSON format:

```json
{
  "author": "Andrew",
  "content": "Dinner?"
}
```

The API will respond with the full details of the comment you've posted (in JSON format), e.g:

```json
{
  "id": 11,
  "author": "Andrew",
  "content": "Dinner?",
  "channel": "general",
  "created_at": "2022-01-03T11:53:59.323Z",
  "updated_at": "2022-01-03T11:53:59.323Z"
}
```


