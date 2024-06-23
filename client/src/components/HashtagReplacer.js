import React, { useState } from 'react';
import axios from 'axios';

const HashtagReplacer = () => {
  const [text, setText] = useState('');
  const [replacement, setReplacement] = useState('');
  const [result, setResult] = useState('');

  const handleReplace = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8080/api/replace-hashtags/', { text, replacement });
      setResult(response.data.replaced_text);
    } catch (error) {
      console.error('Error replacing hashtags:', error);
    }
  };

  return (
    <div>
      <h2>Replace Hashtags</h2>
      <textarea value={text} onChange={(e) => setText(e.target.value)} placeholder="Enter text" />
      <input type="text" value={replacement} onChange={(e) => setReplacement(e.target.value)} placeholder="Enter replacement text" />
      <button onClick={handleReplace}>Replace Hashtags</button>
      <p>Result: {result}</p>
    </div>
  );
};

export default HashtagReplacer;
