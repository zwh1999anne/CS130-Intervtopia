import React, { useState }  from "react";
import ChartistGraph from "react-chartist";
// react-bootstrap components
import {
  Badge,
  Button,
  Card,
  Navbar,
  Nav,
  Table,
  Container,
  Row,
  Col,
  Form,
  Modal,
  OverlayTrigger,
  Tooltip,
} from "react-bootstrap";

import { getTodos } from "backend_data/to_do_list";
import { getInterviews } from "backend_data/interviews_list";
import { getMatchInfo, matchConfirmed } from "backend_data/match_list";
import { getServiceLink} from "backend_data/external_service_link";
import { getEvalForm, evalConfirmed } from "backend_data/evaluation_form";
import {getPreferenceInfo, current_user_id} from "backend_data/default_preferences";

const toDos = getTodos(current_user_id);
const interviews_list = getInterviews(current_user_id);
let current_match = "random";
let curr_info={id: "-1", name: " ", type: " ", time: " "}
let curr_todo_id = toDos.length + 1;
let curr_interview_id = interviews_list.length + 1;

function AddFriendModal(props) {
  return (
    <Modal
      {...props}
      size="lg"
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          Sending Friend Invitation to {props.name}
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <p>
          You could add a message to {props.name} here.
        </p>
        <Form.Group className="mb-3">
        <Form.Control
          defaultValue="Let's practice together, as friends!"
          placeholder="Enter your message here."
          as="textarea" rows={3}></Form.Control>
        </Form.Group>
      </Modal.Body>
      <Modal.Footer>
      <Button variant="primary" className="btn-fill" onClick={props.onHide}>
            Send
          </Button>
        <Button variant="secondary" className="btn-fill" onClick={props.onHide}>Cancel</Button>
      </Modal.Footer>
    </Modal>
  );
}

function LauchInterviewModal(props) {
  return (
    <Modal
      {...props}
      size="lg"
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          Sending Interview Invitation to {props.name}
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <p>
          Please confirm if you want to interview with {props.name} at the following time:
        </p>
        <p>
        {props.day}, {props.time}
        </p>
      </Modal.Body>
      <Modal.Footer>
      <Button variant="primary" className="btn-fill" onClick={props.onHide}>
          Confirm
          </Button>
        <Button variant="secondary" className="btn-fill" onClick={props.onHide}>Cancel</Button>
      </Modal.Footer>
    </Modal>
  );
}

function AddMatchModal(props){
  const [matchType, setmatchType] = React.useState("random");
  return (
    <Modal
      {...props}
      size="lg"
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          Matching you with an awesome peer!
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <p>
          Please select a matching type below.
        </p>
        <Form.Group className="mb-3">
        <Form.Select
          defaultValue={matchType}
          onChange={(e) => {setmatchType(e.currentTarget.value); current_match=matchType}}
          className="w-100 form-control">
          <option value="random">Random Matching</option>
          <option value="history">History Matching</option>
          <option value="friend">Invite a Friend</option>
        </Form.Select>
        </Form.Group>
      </Modal.Body>
      <Modal.Footer>
      <Button variant="primary" className="btn-fill" onClick={props.confirmed}>
            Confirm
          </Button>
        <Button variant="secondary" className="btn-fill" onClick={props.onHide}>Cancel</Button>
      </Modal.Footer>
    </Modal>
  );
}

function ConfirmMatchModal(props){
  const [match_info, setmatchInfo] = React.useState({});
  getMatchInfo(current_match, props.name).then((value) => setmatchInfo(value));
  curr_info.name = match_info.name
  curr_info.id = {...curr_todo_id}
  curr_info.name = match_info.name
  curr_info.type = "interview"
  curr_info.time = match_info.available_day + " " + match_info.available_time
  return (
    <Modal
      {...props}
      size="lg"
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          We have found an excellent match for you!
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <p>
          Please confirm if you hope to interview with this matched user:
        </p>
        <p>
          {match_info.name}, good at {match_info.first_language} and {match_info.second_language}, with desired difficulty at {match_info.desired_difficulty} level
        </p>
        <p>
           {match_info.name} got {match_info.evaluation_score} in the previous interview evaluations.
        </p>
        <p>
          You could meet {match_info.name} on {match_info.available_day} at {match_info.available_time}.
        </p>
        
      </Modal.Body>
      <Modal.Footer>
      <Button variant="primary" className="btn-fill" onClick={() => {props.confirmed(); matchConfirmed(match_info)}}>
            Confirm
          </Button>
        <Button variant="secondary" className="btn-fill" onClick={props.onHide}>Cancel</Button>
      </Modal.Footer>
    </Modal>
  );
}

function EvaluationModal(props){
  const eval_questions = getEvalForm();
  var res_dict = {};
  return (
    <Modal
      {...props}
      size="lg"
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          Please fill in the evaluation form for {props.name}
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
      <Table>
        <tbody>
          {
          eval_questions.map((element) => {
            if(element.type === "rating"){
              res_dict[element.dimension] = 5;
              return <tr key={element.dimension}>
              <Form.Group>
              <Form.Label>Please rate the {element.dimension}</Form.Label>
              <Form.Select defaultValue={5}  className="form-control" onChange={(e) => {res_dict[element.dimension] = e.currentTarget.value;}}>
                <option value={5}>5</option>
                <option value={4}>4</option>
                <option value={3}>3</option>
                <option value={2}>2</option>
                <option value={1}>1</option>
              </Form.Select>
              </Form.Group>
              </tr>
            }
            else if(element.type === "text"){
              res_dict[element.dimension] = "";
              return <tr key={element.dimension}>
              <Form.Group className="mb-3">
              <Form.Label>(Optional) Please leave a comment for {props.name}</Form.Label>
              <Form.Control
              defaultValue=""
              placeholder="Enter your comment here."
              as="textarea" rows={3} 
              onChange={(e) => {res_dict[element.dimension] = e.currentTarget.value}}></Form.Control>
              </Form.Group>
              </tr>
            }
          } )
        }
         </tbody>
      </Table>
      </Modal.Body>
      <Modal.Footer>
      <Button variant="primary" className="btn-fill" onClick={() => {props.submitted();evalConfirmed(props.name, res_dict)}}>
           Submit
      </Button>
      <Button variant="secondary" className="btn-fill" onClick={props.onHide}>Cancel</Button>
      </Modal.Footer>
    </Modal>
  );
}

function JoinMeetingModal(props) {
  var service_link = getServiceLink();
  return (
    <Modal
      {...props}
      size="lg"
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          Meeting room links with {props.name}
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>Service</th>
              <th>Link</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Question</td>
              <td><a href={service_link.question}  target="_blank">{service_link.question}</a></td>
            </tr>
            <tr>
              <td>Chatting</td>
              <td><a href={service_link.chatting}  target="_blank">{service_link.chatting}</a></td>
            </tr>
            <tr>
              <td>IDE</td>
              <td><a href={service_link.IDE}  target="_blank">{service_link.IDE}</a></td>
            </tr>
          </tbody>
        </Table>
      </Modal.Body>
      <Modal.Footer>
        <Button variant="primary" className="btn-fill" onClick={props.completed}>
          Meeting completed
        </Button>
        <Button variant="secondary" className="btn-fill" onClick={props.onHide}>Cancel</Button>
      </Modal.Footer>
    </Modal>
  );
}


function Dashboard() {
  const [todolist, settodoList] = useState(toDos);

  const deleteTodo = (id) => {
    return settodoList([...todolist.filter((element) => element.id !== id)]);
  };

  const addTodo = (item) => {
    settodoList(todolist => [...todolist, item] );
  };

  const [interviewlist, setinterviewList] = useState(interviews_list);

  const addinterview = (item) => {
    setinterviewList(interviewlist => [...interviewlist, item] );
  };

  const [addFriendModalShow, setaddFriendModalShow] = React.useState(false);
  const [FriendModalName, setFriendModalName] = React.useState(" ");

  const [evalModalShow, setevalModalShow] = React.useState(false);
  const [EvalModalName, setEvalModalName] = React.useState(" ");
  
  const [addMatchModalShow, setaddMatchModalShow] = React.useState(false);
  const [confirmMatchModalShow, setconfirmMatchModalShow] = React.useState(false);

  const [joinMeetingShow, setjoinMeetingShow] = React.useState(false);
  const [meetingParName, setMeetingParName] = React.useState(" ");

  const [launchInterviewShow, setlaunchinterviewShow] = React.useState(false);
  const [interviewName, setinterviewName] = React.useState(" ");

  const [preferences, setPreferences] = useState({});
  getPreferenceInfo(current_user_id).then((value) => setPreferences(value));
  var default_preferences = preferences;
  

  return (
    <>
      <Container fluid>
        <Row>
          <Col md="8">
          <Card className="card-tasks">
              <Card.Header>
                <Card.Title as="h4">To-do List</Card.Title>
              </Card.Header>
              <Card.Body>
                <div className="table-full-width">
                  <Table>
                    <tbody>
                    {
                      todolist.map((element) => {
                          if(element.type === "interview"){
                            return <tr key={element.id}>
                            <td>
                              <Form.Check className="mb-1 pl-0">
                                <Form.Check.Label>
                                  <Form.Check.Input
                                    defaultValue=""
                                    type="checkbox"
                                  ></Form.Check.Input>
                                  <span className="form-check-sign"></span>
                                </Form.Check.Label>
                              </Form.Check>
                            </td>
                            <td className="text-left">
                              <div>
                              You have an upcoming interview with {element.name} on {element.time}!
                              </div>
                              <div className="text-left">
                                  <Button variant="primary" className="btn-fill mr-5" size="sm" onClick={() => { setjoinMeetingShow(true); setMeetingParName(element.name) }}>Join Meeting</Button>{' '}
                                  <JoinMeetingModal name={meetingParName} show={joinMeetingShow} time = {element.time} 
                                  onHide={() => setjoinMeetingShow(false)}
                                  completed = {() => {deleteTodo(element.id); addTodo({id: {...curr_todo_id}, name: element.name, type: "evaluation", time: element.time}); 
                                  addinterview({id: {...curr_interview_id}, name: element.name, time: element.time, evaluated: "No"}); 
                                  setjoinMeetingShow(false); curr_todo_id += 1; curr_interview_id += 1}}>
                                  </JoinMeetingModal>
                          <Button variant="primary" className="mr-5" size="sm">Reschedule</Button>{' '}
                          <Button variant="outline-secondary" size="sm">View Profile</Button>
                              </div>
                            </td>
                            <td className="td-actions text-right">
                              <OverlayTrigger
                                overlay={
                                  <Tooltip id="tooltip-506045838">Remove this task!</Tooltip>
                                }
                              >
                                <Button
                                  className="btn-simple btn-link p-1"
                                  type="button"
                                  variant="danger"
                                  onClick={() => {deleteTodo(element.id)}}
                                >
                                  <i className="fas fa-times"></i>
                                </Button>
                              </OverlayTrigger>
                            </td>
                          </tr>;
                          }
                          else{
                            return <tr key={element.id}>
                            <td>
                              <Form.Check className="mb-1 pl-0">
                                <Form.Check.Label>
                                  <Form.Check.Input
                                    defaultValue=""
                                    type="checkbox"
                                  ></Form.Check.Input>
                                  <span className="form-check-sign"></span>
                                </Form.Check.Label>
                              </Form.Check>
                            </td>
                            <td className="text-left">
                            You have an evaluation form for {element.name} that you interviewed with on {element.time}. 
                            <div className="text-left">
                              <Button variant="primary" className="btn-fill mr-5" size="sm" onClick={() => {setevalModalShow(true); setEvalModalName(element.name)}}>
                          Evaluate
                          </Button>{' '}
                          <EvaluationModal name = {EvalModalName} show={evalModalShow} onHide={() => setevalModalShow(false)}
                          submitted={() => {setevalModalShow(false); deleteTodo(element.id)}}></EvaluationModal>
                          <Button variant="primary" className="mr-5" size="sm" onClick={() => {setaddFriendModalShow(true); setFriendModalName(element.name)}}>Add Friend</Button>{' '}
                          <AddFriendModal name = {FriendModalName} show={addFriendModalShow} onHide={() => setaddFriendModalShow(false)}></AddFriendModal>
                          <Button variant="outline-secondary" size="sm">View Profile</Button>
                              </div>
                            </td>
                            <td className="td-actions text-right">
                              <OverlayTrigger
                                overlay={
                                  <Tooltip id="tooltip-21130535">Remove this task!</Tooltip>
                                }
                              >
                                <Button
                                  className="btn-simple btn-link p-1"
                                  type="button"
                                  variant="danger"
                                  onClick={() => deleteTodo(element.id)}
                                >
                                  <i className="fas fa-times"></i>
                                </Button>
                              </OverlayTrigger>
                            </td>
                          </tr>
                          }
                      })
                    }
                    </tbody>
                  </Table>
                </div>
              </Card.Body>
            </Card>
          </Col>
          <Col md="4">
            <Card className="text-center">
              <Card.Header>
                <Card.Title as="h4">Do you want to launch a new interview?</Card.Title>
              </Card.Header>
              <Card.Body>
              <p className="description text-center">
               You could choose to be randomly matched with a peer, <br></br>
               matched within your history, 
               or invite a friend!
              </p>
              <Button variant="primary" className="btn-fill" onClick={() => {setaddMatchModalShow(true)}}>
              Add New Match
              </Button>
              <AddMatchModal show={addMatchModalShow} 
              onHide={() => setaddMatchModalShow(false)} 
              confirmed={() => {setaddMatchModalShow(false); setconfirmMatchModalShow(true)}}></AddMatchModal>
              <ConfirmMatchModal show={confirmMatchModalShow} name={default_preferences.username}
              onHide={() => setconfirmMatchModalShow(false)}
              confirmed = {() => {setconfirmMatchModalShow(false); addTodo(curr_info);curr_todo_id += 1}} ></ConfirmMatchModal>
              </Card.Body>
            </Card>
          </Col>
        </Row>
        <Row>
          <Col md="12">
            <Card className="card-tasks">
              <Card.Header>
                <Card.Title as="h4">Recent Interviews</Card.Title>
              </Card.Header>
              <Card.Body>
              <Table className="table-hover table-striped">
                  <thead>
                    <tr>
                      <th className="border-0">Match Name</th>
                      <th className="border-0">Interview Time</th>
                      <th className="border-0">Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                  {
                    interviewlist.map((element) => {
                      return <tr key={element.id}>
                         <td>{element.name}</td>
                        <td>{element.time}</td>
                        <td>
                        <div className="text-left">
                        <Button variant="primary" className="btn-fill mr-3" size="sm" onClick={() => {setlaunchinterviewShow(true); setinterviewName(element.name)}}>
                        Interview Again
                        </Button>
                        <LauchInterviewModal name={interviewName} show={launchInterviewShow} 
                        day = {default_preferences.available_day} time = {default_preferences.available_time}
                        onHide={() => setlaunchinterviewShow(false)}></LauchInterviewModal>
                        <Button variant="primary" size="sm"  onClick={() => {setaddFriendModalShow(true); setFriendModalName(element.name)}}>Add Friend</Button>
                        <AddFriendModal name = {FriendModalName} show={addFriendModalShow} onHide={() => setaddFriendModalShow(false)}></AddFriendModal>
                        </div>
                        </td>
                        </tr>;
                    })
                  }
                  </tbody>
                </Table>
              </Card.Body>
              <Card.Footer>
              </Card.Footer>
            </Card>
          </Col>
        </Row>
      </Container>
    </>
  );
}

export default Dashboard;
