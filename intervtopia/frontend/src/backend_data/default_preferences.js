import React, { useEffect, useState }  from "react";
import axios from "axios";

const default_preference = {
    username: "Haofan",
    email: "coding@g.ucla.edu",
    school: "UCLA Computer Science",
    job_role: "Software Engineer",
    interview_role: "both",
    first_language: "C++",
    second_language: "Python",
    desired_difficulty: "hard",
    available_day: "Tuesday",
    available_time: "10:00 - 11:00 A.M.",
    additional_available_day: "Thursday",
    additional_available_time: "2:00 - 3:00 P.M."
}

export const current_user_id = 2;

export function getPreferenceInfo(user_id){
   /*const [pdata, setPdata] = React.useState({});
    useEffect(() => {getUserPreference();}, []);*/

    let session_url = "http://127.0.0.1:8000/users/2/"
    const getUserPreference = async () => {
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
      console.log(data)
    }

    getUserPreference();

    /* axios.get("http://127.0.0.1:8000/users/2/")
      .then((res) => {console.log(res)})
      .catch((err) => console.log(err)); */

    /* if(Object.keys(pdata).length !== 0){
        return processPreferenceInfo(pdata);
    } */


    return default_preference;
}

function processPreferenceInfo(raw_data){
    const processed_preferences = {
        username: "",
        email: "",
        school: "",
        job_role: "",
        interview_role: "",
        first_language: "",
        second_language: "",
        desired_difficulty: "",
        available_day: "",
        available_time: "",
        additional_available_day: "",
        additional_available_time: ""
    }
    processed_preferences.username = raw_data.username;
    processed_preferences.email = raw_data.email;
    processed_preferences.school = raw_data.education;
    if(raw_data.target_positions.length === 0){
        processed_preferences.job_role = "";
    }
    else{
        processed_preferences.job_role = raw_data.target_positions[0];
    }

    if(raw_data.preferred_role === "EE"){
        processed_preferences.interview_role = "interviewee";
    }
    else if(raw_data.preferred_role === "ER"){
        processed_preferences.interview_role = "interviewer";
    }
    else{
        processed_preferences.interview_role = "both";
    }

    if(raw_data.preferred_languages.length >= 2){
        processed_preferences.first_language = raw_data.preferred_languages[0];
        processed_preferences.second_language = raw_data.preferred_languages[1];
    }else if(raw_data.preferred_languages.length >= 1){
        processed_preferences.first_language = raw_data.preferred_languages[0];
        processed_preferences.second_language = "";
    }
    else{
        processed_preferences.first_language = "";
        processed_preferences.second_language = "";
    }

    if(raw_data.preferred_difficulty === "H"){
        processed_preferences.desired_difficulty = "hard";
    }
    else if(raw_data.preferred_difficulty === "E"){
        processed_preferences.interview_role = "easy";
    }
    else{
        processed_preferences.interview_role = "medium";
    }

    if(raw_data.availability.length >= 2){
        time1 = process_date_time(raw_data.availability[0]);
        time2 = process_date_time(raw_data.availability[1]);
        processed_preferences.available_day = time1[0];
        processed_preferences.available_time = time1[1];
        processed_preferences.additional_available_day = time2[0];
        processed_preferences.additional_available_time = time2[1];
    }else if(raw_data.availability.length >= 1){
        time1 = process_date_time(raw_data.availability[0]);
        processed_preferences.available_day = time1[0];
        processed_preferences.available_time = time1[1];
        processed_preferences.additional_available_day = "";
        processed_preferences.additional_available_time = "";
    }
    else{
        processed_preferences.available_day = "";
        processed_preferences.available_time = "";
        processed_preferences.additional_available_day = "";
        processed_preferences.additional_available_time = "";
    }
    return processed_preferences;
}

function process_date_time(input){
    const date_dict = {"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday", 
    "Thu": "Thursday", "Fri": "Friday", "Sat": "Saturday", "Sun": "Sunday"};
    const time_dict = {"9": "9:00 - 10:00 A.M.", "10": "10:00 - 11:00 A.M.",
    "11": "11:00 - 12:00 P.M.", "12": "12:00 - 1:00 P.M.", "13": "1:00 - 2:00 P.M.",
    "14": "2:00 - 3:00 P.M.", "15": "3:00 - 4:00 P.M.", "16": "4:00 - 5:00 P.M."};
    let date_get = false;
    let date = "";
    let first_time = "";
    let time_begin = -1;
    let time_length = 2;
    for(let i = 0; i < input.length; i++){
        if(input[i] === ':' && date_get === false){
            date = input.substring(0, i+1);
            time_begin = i + 2;
            if(input[i + 2] === '0'){
                time_begin = i + 3;
                time_length = 1;
            }
            date_get = true;
            break;
        }
    }
    first_time = input.substring(time_begin, time_length);
    var time_digit = parseInt(first_time,10);
    if(time_digit < 9){
        first_time = "9";
    }
    if(time_digit > 16){
        first_time = "16";
    }
    return [date_dict[date], time_dict[first_time]];
}
