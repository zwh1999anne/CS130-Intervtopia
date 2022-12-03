const default_friends = [
    {
      id:"1",
      name: "Nick C",
      message: "Hi Alice, I have a recent update: I got the offer from my dream company! Thank you for helping me practice interview."
    },
    {
      id:"2",
      name: "Eddie C",
      message: "I am happy to help!"
    },
    {
       id:"3",
       name: "Alicia W",
       message: "Dear Alice, how are things going?"
    },
    {
      id:"4",
      name: "Wendy Y",
      message: "Hi Alice, It's nice to interview with you!"
    }
  ];

export function getFriends(user_id){
  return default_friends;
}
