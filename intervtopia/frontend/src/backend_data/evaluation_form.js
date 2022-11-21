const eval_form_questions = [
  {
    type: "rating",
    dimension: "Problem Solving Skills"
  },
  {
    type: "rating",
    dimension: "Coding Skills"
  },
  {
    type: "rating",
    dimension: "Communication Skills"
  },
  {
    type: "rating",
    dimension: "Helpfulness"
  },
  {
    type: "text",
    dimension: "comment"
  }
];

export function evalConfirmed(matchName, evalResult){
    return 0;
}
export function getEvalForm(){
   return eval_form_questions;
}