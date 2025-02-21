// array ================================================================================
class DataInArray{
    constructor(){
        this.data=[];
    }
    add(value){
        this.data.push(value);
    }
    contains(value){
        for(let i=0; i<this.data.length; i++){
            if(this.data[i]===value){
                return true;
            }
        }
        return false;
    }
}

// binary search tree ================================================================================
class Node{
    constructor(value, left, right){
        this.value=value;
        this.left=left;
        this.right=right;
    }
}
class DataInBST{
    constructor(){
        this.root=null;
    }
    add(value){
        if(this.root===null){
            this.root=new Node(value,null,null);
            return;
        }
        let currentNode=this.root;
        while(true){
            if(value>currentNode.value){
                if(currentNode.right===null){
                    this.root=new Node(value,null,null);
                    break;
                }else{
                    currentNode=currentNode.right;
                }
            }else if(value<currentNode.value){
                if(currentNode.left===null){
                    this.root=new Node(value,null,null);
                    break;
                }else{
                    currentNode=currentNode.left;
                }
            }
        }
    }
    contains(value){
        if(this.root===null){
            return false;
        }
        let currentNode=this.root;
        while(currentNode!==null){
            if(value===currentNode.value){
                return true;
            }else if(value>currentNode.value){
                currentNode=currentNode.right;
            }else{
                currentNode=currentNode.left;
            }
        }
    }
}


// let bst=new DataInBST();
// bst.add(5);
// bst.add(3);
// bst.add(-3);
// bst.add(0);
// console.log(bst.contains(2));
// console.log(bst.contains(-1));
// console.log(bst.contains(5));
// console.log(bst.contains(-3));

let arr = new DataInArray();
console.time("Array 插入筆資料");
for(let i=0;i<1000;i++){
    arr.add(Math.random()*300000000-150000000); //-150000000~150000000
}
console.timeEnd("Array 插入筆資料");

console.time("Array 搜尋資料");
arr.contains(30000000);
console.timeEnd("Array 搜尋資料");

let bst = new DataInBTS();
console.time("BST 插入筆資料");
for(let i=0;i<1000;i++){
    bst.add(Math.random()*300000000-15000000); //-150000000~150000000
}
console.timeEnd("BST 插入筆資料");

console.time("BST 搜尋資料");
bst.contains(30000000);
console.timeEnd("BST 搜尋資料");