import React from 'react';
import HashtagRemover from './components/HashtagRemover';
import HashtagGetter from './components/HashtagGetter';
import HashtagReplacer from './components/HashtagReplacer';
import HashtagCounter from './components/HashtagCounter';

const App = () => {
  return (
    <div>
      <h1>Hashtag Management</h1>
      <HashtagRemover />
      <HashtagGetter />
      <HashtagReplacer />
      <HashtagCounter />
    </div>
  );
};

export default App;
