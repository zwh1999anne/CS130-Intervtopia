import React, { useState } from "react";

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

import invitations from "backend_data/inivitation_list";
import friends from "backend_data/friends_list";
import default_preferences from "backend_data/default_preferences";

let curr_friend_id = friends.length + 1;

function SendMessageModal(props) {
  return (
    <Modal
      {...props}
      size="lg"
    >
    <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
        Sending Message to {props.name}
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
      <p>
          You could write your message to {props.name} here.
        </p>
        <Form.Group className="mb-3">
        <Form.Control
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
        {default_preferences.available_day}, {default_preferences.available_time}
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

function FriendConfirmModal(props) {
  return (
    <Modal
      {...props}
      size="lg"
    >
    <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          Friends Confirmation
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        Now you and {props.name} are friends!
      </Modal.Body>
      <Modal.Footer>
      <Button variant="primary" className="btn-fill mt-3" onClick={props.onConfirmed}>
            OK
          </Button>
      </Modal.Footer>
    </Modal>
  );
}

function Friends() {
  const [invitationlist, setinvitationList] = useState(invitations);
  const [friendslist, setfriendslist] = useState(friends)

  const deleteInvitation = (id) => {
    return setinvitationList([...invitationlist.filter((element) => element.id !== id)]);
  };

  const addfriend = (item) => {
    setfriendslist(friendslist => [...friendslist, item] );
  };

  const [sendMessageModalShow, setsendMessageModalShow] = React.useState(false);
  const [MessageModalName, setMessageModalName] = React.useState(" ");

  const [FriendConfirmModalShow, setFriendConfirmModalShow] = React.useState(false);

  const [launchInterviewShow, setlaunchinterviewShow] = React.useState(false);
  const [interviewName, setinterviewName] = React.useState(" ");


  return (
    <>
      <Container fluid>
        <Row>
        <Col md="12">
        <Card className="strpied-tabled-with-hover">
              <Card.Header>
                <Card.Title as="h4">Pending Invitations</Card.Title>
              </Card.Header>
              <Card.Body>
              <div className="table-full-width">
                  <Table>
                    <tbody>
                    {
                      invitationlist.map((element) => {
                        return <tr key={element.id}>
                          <td className="text-left">
                              <div>
                              {element.name} has sent you a friend invitation on {element.time}!
                              </div>
                              <div className="text-secondary">
                              "{element.message}"
                              </div>
                            </td>
                            <td>
                            <Button variant="primary" className="btn-fill mr-5" size="sm" 
                            onClick={() => {setFriendConfirmModalShow(true);
                            addfriend({id: {...curr_friend_id}, name: element.name, message: element.message}); curr_friend_id += 1}}>
                          Accept
                          </Button>{' '}
                          <FriendConfirmModal name={element.name} show={FriendConfirmModalShow} 
                          onHide={() => setFriendConfirmModalShow(false)}
                          onConfirmed={() => {setFriendConfirmModalShow(false); deleteInvitation(element.id)}}></FriendConfirmModal>
                          <Button variant="primary" className="mr-5" size="sm" onClick={() => deleteInvitation(element.id)}>Ignore</Button>
                            </td>
                        </tr>;
                      })
                    }
                      </tbody>
                    </Table>
              </div>
              </Card.Body>
          </Card>
          </Col>
        </Row>
        <Row>
          <Col md="12">
            <Card className="strpied-tabled-with-hover">
              <Card.Header>
                <Card.Title as="h4">Friends List</Card.Title>
              </Card.Header>
              <Card.Body className="table-full-width table-responsive px-0">
                <Table className="table-hover table-striped">
                  <thead>
                    <tr>
                      <th className="border-0">Name</th>
                      <th className="border-0" width="670">Lastest Message</th>
                      <th className="border-0">Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                  {
                    friendslist.map((element) => {
                      return <tr key={element.id}>
                         <td>{element.name}</td>
                        <td className="text-secondary">"{element.message}"</td>
                        <td>
                        <div className="text-left">
                        <Button variant="primary" className="btn-fill mr-3" size="sm" onClick={() => {setsendMessageModalShow(true); setMessageModalName(element.name)}}>
                        Send a Message
                        </Button>
                        <Button variant="primary" size="sm" onClick={() => {setlaunchinterviewShow(true); setinterviewName(element.name)}}>
                          Launch an Interview</Button>
                        <LauchInterviewModal name={interviewName} show={launchInterviewShow} onHide={() => setlaunchinterviewShow(false)}> </LauchInterviewModal>
                        <SendMessageModal name = {MessageModalName} show={sendMessageModalShow} onHide={() => setsendMessageModalShow(false)}></SendMessageModal>
                        </div>
                        </td>
                        </tr>;
                    })
                  }
                  </tbody>
                </Table>
              </Card.Body>
            </Card>
          </Col>  
        </Row>
      </Container>
    </>
  );
}

export default Friends;
