var hello = async ()=>{
    var data = await fetch('/api/aircond/co2').then(res => { return res.json() })
    console.log(data , ' used by importing module in jscode')    
    return 'abc'
}

export  {hello}