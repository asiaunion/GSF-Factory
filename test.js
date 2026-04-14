import fs from 'fs';
const data = fs.readFileSync('src/data/blog/ko/일본-도쿄-지진에서-취약한-5곳.md', 'utf-8');
console.log(data.length);
