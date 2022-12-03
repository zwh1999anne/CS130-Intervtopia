const default_toDos = [
    {
      id: "1",
      name: "Yadi C",
      type: "interview",
      time: "Nov 7th, 10: 00"
    },
    {
      id: "2",
      name: "Haofan L",
      type: "evaluation",
      time: "Nov 1st, 9: 00"
    }
  ];

  export function getTodos(user_id){
    return default_toDos;
  }