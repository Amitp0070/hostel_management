document.getElementById('roomForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const roomName = document.getElementById('roomName').value;
    const roomCapacity = document.getElementById('roomCapacity').value;
    addRoomToList(roomName, roomCapacity);
    document.getElementById('roomForm').reset();
  });

  function addRoomToList(name, capacity) {
    const roomsList = document.getElementById('roomsList');
    const listItem = document.createElement('li');
    listItem.textContent = `${name} - Capacity: ${capacity}`;
    roomsList.appendChild(listItem);
  }