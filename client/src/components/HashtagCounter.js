import React, { useState } from 'react';
import axios from 'axios';

const HashtagCounter = () => {
  const [text, setText] = useState('');
  const [count, setCount] = useState(0);

  const handleCount = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8080/api/count-hashtags/', { text });
      setCount(response.data.count);
    } catch (error) {
      console.error('Error counting hashtags:', error);
    }
  };

  return (
    <div>
      <h2>Count Hashtags</h2>
      <textarea value={text} onChange={(e) => setText(e.target.value)} />
      <button onClick={handleCount}>Count Hashtags</button>
      <p>Hashtags Count: {count}</p>
    </div>
  );
};

export default HashtagCounter;
