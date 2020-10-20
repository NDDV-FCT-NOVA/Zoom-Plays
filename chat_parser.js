let last_groups_count=0;
let last_messages_count=0;
function captureChat(){
    let elements = document.getElementsByClassName("chat-item__chat-info-msg");
    if(elements.length == 0)
        return;
    let last_group = elements[elements.length-1].innerHTML.split("\n");
    if(elements.length > last_groups_count || last_group.length > last_messages_count){
        console.log(last_group[last_group.length - 1]);
    }
    last_groups_count = elements.length;
    last_messages_count=last_group.length;
    
}

setInterval(captureChat, 50);
