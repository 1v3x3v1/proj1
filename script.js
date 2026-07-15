function countany(n)
{
    var count=n+1;
    while (count>1)
    {
    	count--;
    	document.getElementById("Access").innerHTML += count + "<br>";	
    	console.log("Denied!");			
    }
}
function nav()
{
	for(var prop in navigator)
    	{
    		document.write(prop + ": " +navigator[prop]+"<br>");
    	}      
}
function loadurl()
{
	window.location= 'https://www.google.com/maps/pala';
}

