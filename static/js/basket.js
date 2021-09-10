let updateBtns = document.getElementsByClassName('add')
let delbtn = document.getElementsByClassName('delete')
let divclass = document.getElementsByClassName('btn-row')
//let deleteBtns = document.getElementsByClassName('delete')

let deleteBtns =document.getElementsByClassName('delete')
function deleteItem(){
    for(var i=0;i<deleteBtns.length;i++){
        deleteBtns[i].addEventListener('click',function(){
            let itemid = this.dataset.item
            
            
            let action = this.dataset.action
           
    
            if(action === 'delete'){
                del(itemid,action)
                $('.content[data-index="'+ itemid +'"]').remove();
                
            }   
        })
    }

}

 



 //let e = document.getElementsByClassName('select')
function getSelected(event){
    
        for(var i=0;i<updateBtns.length;i++){
            updateBtns[i].addEventListener('click',function(){
                let itemid = this.dataset.item
                let action = this.dataset.action
                if(action == 'add'){
                    let qty = event.target[event.target.selectedIndex].text
                    console.log('qty: ',qty)  
                    console.log('USER: ',user)
                    if(user === 'Anonymous'){
                    console.log('Nor logged in')
                    
                    }else{
                    console.log('itemid: ',itemid, 'action: ',action,'item_qty: ',qty)    
                    updateUserOrder(itemid,action, qty)
                } 

                }
               
                
                //var option = e.children[e.selectedIndex];
                //var itemqty = option.textContent;
                //data = {item_qty: $('select option:selected').text()}
                //let qty = Object.values(data)
                
                
            
                
                //let myArr = qty.split('')
                
                //console.log('data: ',data)
               
                //itemqty=e.options[e.selectedIndex].value;
                //let itemqty = e.options[e.selectedIndex].text;
                
        
                
               
            })
        }
         
        
                   
                   
         



            
        


    }

/*for(var i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        let itemid = this.dataset.item
        let action = this.dataset.action
        let qty = event.target[event.target.selectedIndex].text
        console.log('qty: ',qty)      
        
        //var option = e.children[e.selectedIndex];
        //var itemqty = option.textContent;
        //data = {item_qty: $('select option:selected').text()}
        //let qty = Object.values(data)
        
        
    
        
        //let myArr = qty.split('')
        
        //console.log('data: ',data)
       
        //itemqty=e.options[e.selectedIndex].value;
        //let itemqty = e.options[e.selectedIndex].text;
        console.log('itemid: ',itemid, 'action: ',action,'item_qty: ',qty)

        console.log('USER: ',user)
        if(user === 'Anonymous'){
            console.log('Nor logged in')
        }else if(action === 'add'){
            updateUserOrder(itemid,action, qty)
        }
        else if(action === 'delete'){
            del(itemid,action)
        }
    })
}
 }
*/
function updateUserOrder(itemid,action,itemqty){
    console.log('User is logged in, sending data..')

    let url ='/update_item/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'itemid':itemid,'action':action, 'item_qty':itemqty})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data: ', data)
        location.reload()
    })
} 

function del(itemid,action){
    
        console.log('delete data is sending...')        
            
        let url ='/delete_item/'

        fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'itemid':itemid,'action':action})
        })
        .then((response)=>{
            return response.json()
            
        })
        .then((data)=>{
            delete data
            delbtn.parentNode.removeChild('.delete');
            location.reload()
        })
    
}

