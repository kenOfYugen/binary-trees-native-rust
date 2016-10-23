# binary-trees-native-rust

Rust binary trees benchmark ported from [the benchmark game](http://benchmarksgame.alioth.debian.org/u64q/program.php?test=binarytrees&lang=rust&id=1) as a node.js addon.

## Install
`npm install kenOfYugen/binary-trees-native-rust`

Tested on Arch Linux.

If it doesn't compile on your system, make sure that the dependencies specified in `binding.gyp` are met, and try again.

## Use

```javascript
var binaryTreesRust = require('binary-trees-native-rust');

binaryTreesRust.run(10);
```
