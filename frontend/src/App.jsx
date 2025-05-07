import React, { useState, useEffect } from 'react';

const Header = () => (
  <div className="d-flex justify-content-between align-items-center py-2 ps-3 mb-2">
    <h2 className="text-start mb-0">Idle Number Wars</h2>
    <small className="text-end pe-3 d-inline-flex align-items-center">
        Keep the servers running:
        <form action="https://www.paypal.com/donate" className="d-inline ms-2" method="post" target="_top">
        <input type="hidden" name="business" value="QHWPTYWNNPL5G" />
        <input type="hidden" name="no_recurring" value="1" />
        <input type="hidden" name="item_name" value="Thanks for helping with the hosting bill for Idle Number Wars" />
        <input type="hidden" name="currency_code" value="USD" />
        <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
        <img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" />
      </form>
      </small>
  </div>
);

const ScoreDisplay = () => (
  <div className="py-2 text-center">
    <h1 className="display-4 fw-bold">-1,000,000</h1>
  </div>
);

const EventLog = () => (
  <div className="d-flex flex-column h-100 p-2 border rounded">
    <div className="p-2 mb-1 border-bottom">
      <h5>Events</h5>
    </div>
    <textarea 
      className="form-control flex-grow-1"
      readOnly 
      placeholder="Event log goes here..."
      style={{ resize: 'none' }} // Prevent manual resize
    ></textarea>
  </div>
);

const GameGrid = () => (
  <div className="d-flex flex-column h-100 p-2 border rounded">
    <div className="p-2 mb-1 border-bottom">
      <h5>Grid</h5>
    </div>
    <div 
      className="border border-secondary bg-secondary-subtle flex-grow-1 d-flex align-items-center justify-content-center"
      style={{ width: '100%', minHeight: '200px' }}
    >
      (Grid Placeholder)
    </div>
  </div>
);

const InfoTabs = () => {
  const [activeTab, setActiveTab] = useState('modifiers');

  return (
    <div className="d-flex flex-column h-100 p-2 border rounded">
      <div className="p-2 mb-1 border-bottom">
        <h5>Info</h5>
      </div>
      <ul className="nav nav-pills nav-fill">
        <li className="nav-item">
          <button 
            className={`nav-link ${activeTab === 'modifiers' ? 'active' : ''}`}
            onClick={() => setActiveTab('modifiers')}
          >
            Modifiers
          </button>
        </li>
        <li className="nav-item">
          <button 
            className={`nav-link ${activeTab === 'playersNow' ? 'active' : ''}`}
            onClick={() => setActiveTab('playersNow')}
          >
            Players Now
          </button>
        </li>
        <li className="nav-item">
          <button 
            className={`nav-link ${activeTab === 'playerHistory' ? 'active' : ''}`}
            onClick={() => setActiveTab('playerHistory')}
          >
            Player History
          </button>
        </li>
        <li className="nav-item">
          <button 
            className={`nav-link ${activeTab === 'warsHistory' ? 'active' : ''}`}
            onClick={() => setActiveTab('warsHistory')}
          >
            Wars History
          </button>
        </li>
        <li className="nav-item">
          <button 
            className={`nav-link ${activeTab === 'feedback' ? 'active' : ''}`}
            onClick={() => setActiveTab('feedback')}
          >
            Feedback
          </button>
        </li>
      </ul>
      <div className="tab-content flex-grow-1 mt-2 p-2 border-top">
        {activeTab === 'modifiers' && <div>Modifiers Content...</div>}
        {activeTab === 'playersNow' && <div>Players Now Content...</div>}
        {activeTab === 'playerHistory' && <div>Player History Content...</div>}
        {activeTab === 'warsHistory' && <div>Wars History Content...</div>}
        {activeTab === 'feedback' && <div>Feedback Content...</div>}
      </div>
    </div>
  );
};

const Login = () => (
  <div className="p-3 border rounded mb-3">
    <h5>If you have an account, log in:</h5>
    <form>
      <div className="mb-2">
        <label htmlFor="loginUsername" className="form-label">Username</label>
        <input type="text" className="form-control" id="loginUsername" />
      </div>
      <div className="mb-2">
        <label htmlFor="loginPassword" className="form-label">Password</label>
        <input type="password" className="form-control" id="loginPassword" />
      </div>
      <button type="submit" className="btn btn-primary">Submit</button>
    </form>
  </div>
);

const Register = () => {
  const [uuid, setUuid] = useState('');
  const [copyButtonText, setCopyButtonText] = useState('Copy');
  const [username, setUsername] = useState('');

  useEffect(() => {
    const baseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'; // Fallback for Vite
    fetch(`${baseUrl}/api/v1/generate-uuid`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setUuid(data.uuid);
      })
      .catch(error => {
        console.error('Error fetching UUID:', error);
      });
  }, []);

  const handleCopy = () => {
    navigator.clipboard.writeText(uuid)
      .then(() => {
        setCopyButtonText('Copied!');
        setTimeout(() => setCopyButtonText('Copy'), 2000); // Reset after 2 seconds
      })
      .catch(err => {
        console.error('Failed to copy text: ', err);
      });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const baseUrl = import.meta.env.VITE_API_BASE_URL;
    try {
      const response = await fetch(`${baseUrl}/api/v1/register`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: username, password: uuid }),
      });

      const data = await response.json();
      console.log('Registration response:', data);

      if (response.ok) {
        console.log('Registration successful:', data.message, 'User ID:', data.user_id);
      } else {
        console.error('Registration failed:', data.detail || 'Unknown error');
      }
    } catch (error) {
      console.error('Registration request failed due to network or other error:', error);
    }
  };

  return (
  <div className="p-3 border rounded">
    <h5>If you do not have an account, register:</h5>
    <form onSubmit={handleSubmit}>
      <div className="mb-2">
        <label htmlFor="registerUsername" className="form-label">Username</label>
        <input
          type="text"
          className="form-control"
          id="registerUsername"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
      </div>
      <div className="mb-2">
        <label htmlFor="registerPassword" className="form-label">Auto-generated Password</label>
        <div className="input-group">
          <input
            type="text"
            className="form-control"
            id="registerPassword"
            value={uuid}
            readOnly
          />
          <button
            className="btn btn-outline-secondary"
            type="button"
            onClick={handleCopy}
          >
            {copyButtonText}
          </button>
        </div>
      </div>
      <div className="alert alert-danger" role="alert">
        Password cannot be reset or retreived later; store it in a password manager.
      </div>
      <div className="mb-2">
        You've been assigned to: [Team Name Placeholder]
      </div>
      <button type="submit" className="btn btn-primary">Submit</button>
    </form>
  </div>
  );
};

const isLoggedIn = () => {
  return false; 
};

function App() {
  return (
    <div 
      className="container-fluid vh-100 d-flex flex-column px-0"
      style={{ overflow: 'hidden' }}
    >
      <Header />
      {isLoggedIn() ? (
        <>
          <ScoreDisplay />
          <div className="row flex-grow-1 gx-3">
            <div className="col-md-4 d-flex flex-column pb-3">
              <EventLog />
            </div>
            <div className="col-md-4 d-flex flex-column pb-3">
              <GameGrid />
            </div>
            <div className="col-md-4 d-flex flex-column pb-3">
              <InfoTabs />
            </div>
          </div>
        </>
      ) : (
        <div className="flex-grow-1 d-flex flex-column align-items-center justify-content-center">
          <div className="col-md-6 col-lg-4">
            <Login />
            <Register />
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
