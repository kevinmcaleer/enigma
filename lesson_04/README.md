# Lesson 4 - Cluster Bruteforce

Learn how to use DisPy, and a Cluster to perform a Bruteforce decryption.

DisPy must be running on the Cluster nodes you wish to use.

I have created a simple [docker-compose](https://www.kevsrobots.com/learn/docker/) file to enable a quick setup. Click here to download the docker-compose & associated files: <https://github.com/kevinmcaleer/ClusteredPi/tree/main/stacks/octapi>.

The easiest way to setup DisPy is:

1. By cloning https://github.com/kevinmcaleer/ClusteredPi
1. Change to the octapi folder:

    ```bash
    cd ClusteredPi/stacks/octapi
    ```

1. Bring up the container:

    ```bash
    docker-compose up -d
    ```

    The docker image will be created and the container started with this single command.

1. To stop the container, simply type:

    ```bash
    docker-compose down
    ```

---

Run `02_bruteforce_octapi.py` to decrypt the message much quicker than running it stand-alone.