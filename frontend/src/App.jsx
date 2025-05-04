import React, { useState } from 'react';

const Header = () => (
  <div className="py-2">
    <h2 className="text-start">Universal Color Wars</h2>
  </div>
);

const ScoreDisplay = () => (
  <div className="py-3 text-center">
    <h1 className="display-4">-1,000,000</h1>
  </div>
);

const EventLog = () => (
  <div className="d-flex flex-column h-100 p-2 border rounded">
    <h5>Events</h5>
    <textarea 
      className="form-control flex-grow-1 mt-2" 
      readOnly 
      placeholder="Event log goes here..."
      style={{ resize: 'none' }} // Prevent manual resize
    ></textarea>
  </div>
);

const GameGrid = () => (
  <div className="d-flex flex-column h-100 p-2 border rounded align-items-center justify-content-center">
    <h5>Grid</h5>
    <div 
      className="border border-secondary bg-secondary-subtle mt-2"
      style={{ width: '80%', height: '80%', minHeight: '200px' }} // Basic placeholder size
    >
      (Grid Placeholder)
    </div>
  </div>
);

const InfoTabs = () => {
  const [activeTab, setActiveTab] = useState('modifiers');

  return (
    <div className="d-flex flex-column h-100 p-2 border rounded">
      <ul className="nav nav-tabs nav-fill">
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

function App() {
  return (
    // Use vh-100 and d-flex flex-column to make the container fill viewport height
    <div className="container-fluid vh-100 d-flex flex-column">
      <Header />
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
    </div>
  );
}

export default App;
