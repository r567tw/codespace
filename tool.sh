case "$1" in
  local)
    docker build . -t r567tw_workspace:latest
    ;;
  run)
    docker run -itd --rm --name workspace r567tw_workspace:latest
    ;;
  rm)
    docker rm -f workspace
    ;;
  restart)
    echo "restart"
    ;;
  *)
    echo "Usage: $0 {local|run|rm}"
    ;;
esac
  
