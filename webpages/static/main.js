window.onload = function() {
    var links = document.querySelectorAll(".col");
    console.log(links);
    let path = window.location.href;
    console.log(path);
    for(let i =links.length - 1; i>=0; i--) {
        let link = links[i];
        let result = path.lastIndexOf(link);
        if(result >= 0) {
            var parent = link.parentElement;
            parent.className = "active";
            parent.style.backgroundColor = "red";
            break;
        }
        
    }
    let btn = document.getElementById("navButton");
    let windowWidth = window.innerWidth;
    let rightHeader = document.getElementById("rightheader");
    if(windowWidth > 700) {
        rightHeader.removeChild(btn);
    }
    if(windowWidth < 700){
        let nav = document.getElementById("nav");
        let subHead = document.getElementById('subhead');
        rightHeader.removeChild(document.querySelector(".nav"));
        let header = document.getElementById('header');
        header.removeChild(document.querySelector('.subhead'));
        header.removeChild(document.getElementById('rightheader'));
        let underhead = document.createElement('div');
        header.appendChild(underhead);
        underhead.appendChild(subHead);
        underhead.appendChild(rightHeader);
        underhead.style.display = 'flex';
        underhead.style.flexDirection = 'row';

        btn.addEventListener('click', function() {
            if(header.contains(nav)) {
                header.removeChild(nav);
                btn.className = '';
            }
            else{
                btn.className = 'tt';
                header.appendChild(nav);
                let list = document.getElementById('list');
                list.style.textTransform = 'capitalize';
                list.style.width = '95%';
                list.style.paddingLeft = '25px';
                list.style.fontSize = 'larger';
                let innerList = document.querySelectorAll('.col');
                innerList.forEach(function(dd) {
                    dd.style.paddingLeft = '20px';
                    dd.style.fontFamily = 'sans-serif';
                    dd.style.color = '#e3f2fd';
                })
            }
        })
    }
    
    
}

// links.forEach(function(link) {
//     console.log(path.lastIndexOf(link));
//     console.log(link.parentElement);
//     var result = path.lastIndexOf(link);
//     if(result >= 0) {
//         var parent = link.parentElement;
//         parent.className = "active";
//         parent.style.backgroundColor = "red";
//         break;
//     }
// })



