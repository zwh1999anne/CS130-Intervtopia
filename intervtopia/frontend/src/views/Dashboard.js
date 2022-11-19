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

import toDos from "backend_data/to_do_list";
import interviews_list from "backend_data/interviews_list";
import { getMatchInfo, matchConfirmed } from "backend_data/match_list";

var current_match = "random";

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
  const match_info = getMatchInfo(current_match);
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
      <Button variant="primary" className="btn-fill" onClick={() => {props.onHide(); matchConfirmed(match_info.name, match_info.available_day, match_info.available_time)}}>
            Confirm
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

  const [addFriendModalShow, setaddFriendModalShow] = React.useState(false);
  const [FriendModalName, setFriendModalName] = React.useState(" ");
  
  const [addMatchModalShow, setaddMatchModalShow] = React.useState(false);
  const [confirmMatchModalShow, setconfirmMatchModalShow] = React.useState(false);

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
                              <Button variant="primary" className="btn-fill mr-5" size="sm">
                          Join Meeting
                          </Button>{' '}
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
                                  onClick={() => deleteTodo(element.id)}
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
                              <Button variant="primary" className="btn-fill mr-5" size="sm">
                          Evaluate
                          </Button>{' '}
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
              <ConfirmMatchModal show={confirmMatchModalShow} onHide={() => setconfirmMatchModalShow(false)}></ConfirmMatchModal>
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
                    interviews_list.map((element) => {
                      return <tr key={element.id}>
                         <td>{element.name}</td>
                        <td>{element.time}</td>
                        <td>
                        <div className="text-left">
                        <Button variant="primary" className="btn-fill mr-3" size="sm">
                        Interview Again
                        </Button>{'     '}
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
