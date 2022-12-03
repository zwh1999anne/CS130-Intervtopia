const default_messages_list = [
    {
      id: "1",
      name: "Nick C",
      message: "Hi Alice, I have a recent update: I got the offer from my dream company! Thank you for helping me practice interview.",
      time: "Nov 8th 11:31",
      type: "message"
    },
    {
      id: "2",
      name: "Eddie C",
      message: "I am happy to help!",
      time: "Nov 6th 13:12",
      type: "message"
    },
    {
       id: "3",
       name: "Alicia W",
       message: "Dear Alice, how are things going?",
       time: "Nov 5th 14:45",
       type: "message"
    },
    {
        id: "4",
        name: "Dicky C",
        message: "Hi Alice, Nice to meet you! Do you want to have an coding interview with me using C++?",
        time: "Nov 11th 15:00",
        type: "interview"
     }

  ];

  export function getMessages(user_id){
    return default_messages_list;
  };
