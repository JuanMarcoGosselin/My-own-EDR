fetch("http://127.0.0.1:8000/events")
    .then(response => response.json())
    .then(data => {
        cuerpo = document.getElementById("Data")
        for(const event of data){
            const fila = document.createElement("tr")

            const id = document.createElement("td")
            id.textContent = event.id
            fila.appendChild(id)

            const host = document.createElement("td")
            host.textContent = event.hostname
            fila.appendChild(host)

            const timestamp = document.createElement("td")
            timestamp.textContent = event.timestamp
            fila.appendChild(timestamp)

            
            const name = document.createElement("td")
            name.textContent = event.name
            fila.appendChild(name)

            const pid = document.createElement("td")
            pid.textContent = event.pid
            fila.appendChild(pid)

            const ppid = document.createElement("td")
            ppid.textContent = event.ppid
            fila.appendChild(ppid)

            cuerpo.appendChild(fila)
        }
        
    })