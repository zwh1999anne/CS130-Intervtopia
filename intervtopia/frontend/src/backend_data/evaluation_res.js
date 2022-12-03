const default_evaluation = 
[
    {
        dimension: "problem_solving",
        value: 4.5,
        other: ""
      },
      {
        dimension: "coding_skills",
        value: 4.7,
        other: ""
      },
      {
        dimension: "communication",
        value: 4,
        other: ""
      },
      {
        dimension: "helpfulness",
        value: 5,
        other: ""
      },
      {
        dimension: "comment",
        value: 0,
        other: "She is good at analyzing and simplifying problems. His coding skills are also impressive, with high speed and keep bugs at a minimum level. It's very nice to interview with him!"
      }
];

export function getEvalRes(user_id){
  return default_evaluation;
};