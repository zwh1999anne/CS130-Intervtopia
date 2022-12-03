import axios from "axios";
import { process_date_time } from "./default_preferences";

const default_match_info = {
    name: "Wendy Y",
    first_language: "JavaScipt",
    second_language: "Python",
    desired_difficulty: "hard",
    available_day: "Tuesday",
    available_time: "10:00 - 11:00 A.M.",
    evaluation_score: "4.7"
}

export async function getMatchInfo(matchType, username){
    let session_url = "http://127.0.0.1:8000/matching/?type=history&user="+username;

    async function getUserMatch(){
      const { data } = await axios.get(session_url, {
        auth: {
            username: 'haofan',
            password: 'asd70asd'
          },
        proxy: {
            protocol: 'http',
            host: '127.0.0.1',
            // hostname: '127.0.0.1' // Takes precedence over 'host' if both are defined
            port: 8000
          },
      });
      //console.log(data)
      let match_info = processMatchInfo(data);

      return match_info;
    }
    let processed_match_info = await getUserMatch();
    
   return processed_match_info;
}

function processMatchInfo(raw_data){
    const processed_match_info = default_match_info;

    processed_match_info.name = raw_data.name;

    if(raw_data.difficulty == "hard"){
        processed_match_info.desired_difficulty = "hard";
    }
    else if(raw_data.difficulty == "medium"){
        processed_match_info.desired_difficulty = "medium";
    }
    else{
        processed_match_info.desired_difficulty = "easy";
    }

    if(raw_data.evaluation_score > 0){
        processed_match_info.evaluation_score = raw_data.evaluation_score;
    }

    if(raw_data.languages.length >= 2){
        processed_match_info.first_language = raw_data.preferred_languages[0];
        processed_match_info.second_language = raw_data.preferred_languages[1];
    }else if(raw_data.languages.length >= 1){
        processed_match_info.first_language = raw_data.preferred_languages[0];
    }

    if(raw_data.availability.length >= 2){
        let time1 = process_date_time(raw_data.availability[0]);
        let time2 = process_date_time(raw_data.availability[1]);
        processed_match_info.available_day = time1[0];
        processed_match_info.available_time = time1[1];
        processed_match_info.additional_available_day = time2[0];
        processed_match_info.additional_available_time = time2[1];
    }
    else if(raw_data.availability.length >= 1){
        let time1 = process_date_time(raw_data.availability[0]);
        processed_match_info.available_day = time1[0];
        processed_match_info.available_time = time1[1];
    }

    return processed_match_info;
}

export function matchConfirmed(match_info){
    return 0;
}