
class SocketManager{

  // https://socket.io/docs/client-api/#socket-on-eventName-callback
  reserved_events = [
    'connect', 
    'connect_error', 
    'connect_timeout',
    'error',
    'disconnect',
    'reconnect',
    'reconnect_attempt',
    'reconnecting',
    'reconnect_error',
    'reconnect_failed',
    'ping',
    'pong'
  ]

  constructor(url){
    this.socket = io(url, {autoConnect: false});
  }

  connect(){
    //auto connects
    console.log(this.socket);
    this.socket.on('disconnect', this.socket.connect);

    return new Promise((resolve, reject)=>{
      try{
        this.socket.on('connect', _ =>resolve(true));
        this.socket.open();
      }catch(e){
        reject(e);
      }
    });
  }

  addCustomEventHandler(event, cb){
    if(this.reserved_events.includes(event))throw 'RESERVED EVENT EXCEPTION'
    this.socket.on(event, cb);
  }

  addEventHandler(event, cb){
    if(!this.reserved_events.includes(event))throw 'UNKNOWN EVENT EXCEPTION';
    this.socket.on(event, cb)
  }

  emit(event, data){
    if(!this.socket.connected) throw 'SOCKET NOT CONNECTED EXCEPTION';
    this.socket.emit(event, data);
  }

  //https://stackoverflow.com/questions/1479319/simplest-cleanest-way-to-implement-singleton-in-javascript
  static getInstance(url){

    if(!SocketManager.instance){
      SocketManager.instance = new SocketManager(url);
    }

    return SocketManager.instance;
  }

}