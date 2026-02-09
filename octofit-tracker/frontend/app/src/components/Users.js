import React, { useEffect, useState } from 'react';

const Users = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace 
    ? `https://${codespace}-8000.app.github.dev/api/users/`
    : 'http://localhost:8000/api/users/';
  const [users, setUsers] = useState([]);

  useEffect(() => {
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setUsers(results);
        console.log('Fetched users:', results);
      })
      .catch(err => console.error('Error fetching users:', err));
  }, [endpoint]);

  return (
    <div className="card shadow mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4 text-primary">Users</h2>
        <div className="table-responsive">
          <table className="table table-striped table-hover align-middle">
            <thead className="table-dark">
              <tr>
                <th>#</th>
                <th>User</th>
              </tr>
            </thead>
            <tbody>
              {users.length === 0 ? (
                <tr><td colSpan="2" className="text-center">No users found.</td></tr>
              ) : (
                users.map((user, idx) => (
                  <tr key={user.id || idx}>
                    <td>{user.id || idx + 1}</td>
                    <td>{typeof user === 'object' ? JSON.stringify(user) : user}</td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Users;
