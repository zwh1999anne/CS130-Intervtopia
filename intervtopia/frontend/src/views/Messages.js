import React from "react";

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
  OverlayTrigger,
  Tooltip,
} from "react-bootstrap";

import messages_list from "backend_data/messages_list";

function Messages() {
  return (
    <>
      <Container fluid>

      <Row>
        <Col md="12">
        <Card className="strpied-tabled-with-hover">
              <Card.Header>
                <Card.Title as="h4">Interview Invitations</Card.Title>
              </Card.Header>
              <Card.Body>
              <div className="table-full-width">
                  <Table>
                    <tbody>
                      {
                        messages_list.map((element, index) => {
                          if(element.type == "interview"){
                            return <tr key={index}>
                          <td className="text-left">
                              <div>
                              {element.name} invited you to have an interview on {element.time}!
                              </div>
                              <div className="text-secondary" width="670">
                              "{element.message}"
                              </div>
                            </td>
                            <td>
                            <Button variant="primary" className="btn-fill mr-5" size="sm">
                          Accept
                          </Button>{' '}
                          <Button variant="primary" className="mr-5" size="sm">Ignore</Button>
                            </td>
                        </tr>;
                          }
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
                <Card.Title as="h4">Friends Messages</Card.Title>
              </Card.Header>
              <Card.Body className="table-full-width table-responsive px-0">
                <Table className="table-hover table-striped">
                  <thead>
                    <tr>
                      <th className="border-0" width="670">Message</th>
                      <th className="border-0">From</th>
                      <th className="border-0">Time Received</th>
                      <th className="border-0">Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                   {
                    messages_list.map((element, index) => {
                      if(element.type == "message"){
                        return <tr key={index}>
                        <td className="text-secondary">"{element.message}"</td>
                        <td>{element.name}</td>
                        <td>{element.time}</td>
                        <td>
                        <div className="text-left">
                        <Button variant="primary" className="btn-fill mr-3" size="sm">
                        Read and Reply
                        </Button>{'     '}
                        <Button variant="primary" size="sm">Delete</Button>
                        </div>
                        </td>
                        </tr>;
                      }
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

export default Messages;
