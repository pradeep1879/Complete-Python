list2 = [3, 4, 8, 3,  8, 7, 5, 4]
result = []
seen = new Set()

for(const i of list2){
    if (!seen.has(i)){
        result.push(i);
        seen.add(i);
    }
}
console.log(result);