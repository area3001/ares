Last login: Thu Nov 17 17:16:01 on ttys000
paularmandsmbp.rto.be 05:37:39 ~$ cd dev
dev/         dev_habitat/ 
paularmandsmbp.rto.be 05:37:39 ~$ cd dev_habitat
paularmandsmbp.rto.be 05:37:44 ~/dev_habitat$ ll
total 16
 0 drwxr-xr-x@ 10 paularmand  staff   340B Nov 16 10:42 .
 0 drwxr-xr-x@  8 paularmand  staff   272B Aug 19 09:51 ..
16 -rw-r--r--@  1 paularmand  staff   6.0K Oct 21 10:26 .DS_Store
 0 drwxr-xr-x@ 15 paularmand  staff   510B Nov 15 08:22 baldrick
 0 drwxr-xr-x@  4 paularmand  staff   136B Nov 16 10:43 de_slimste_mens_tensorflow
 0 drwxr-xr-x@  8 paularmand  staff   272B Nov 15 09:06 habitat-deploy
 0 drwxr-xr-x@  8 paularmand  staff   272B Oct 20 15:20 habitat-doc
 0 drwxr-xr-x@ 10 paularmand  staff   340B Oct 19 14:37 habitat-kafka
 0 drwxr-xr-x@  3 paularmand  staff   102B Nov 15 08:19 pio-kafka
 0 drwxr-xr-x@  7 paularmand  staff   238B Nov 22 16:54 radioplus_site
paularmandsmbp.rto.be 05:37:46 ~/dev_habitat$ git clone git@gitlab.com:vrtoeni/data_nginx.git
Cloning into 'data_nginx'...
warning: You appear to have cloned an empty repository.
Checking connectivity... done.
paularmandsmbp.rto.be 05:38:02 ~/dev_habitat$ cd data_nginx/
paularmandsmbp.rto.be 05:38:23 (master) ~/dev_habitat/data_nginx$ ll
total 0
0 drwxr-xr-x@  3 paularmand  staff   102B Nov 22 17:38 .
0 drwxr-xr-x@ 11 paularmand  staff   374B Nov 22 17:38 ..
0 drwxr-xr-x@ 10 paularmand  staff   340B Nov 22 17:38 .git
paularmandsmbp.rto.be 05:38:24 (master) ~/dev_habitat/data_nginx$ touch README.md
paularmandsmbp.rto.be 05:38:36 (master) ~/dev_habitat/data_nginx$ ll
total 0
0 drwxr-xr-x@  4 paularmand  staff   136B Nov 22 17:38 .
0 drwxr-xr-x@ 11 paularmand  staff   374B Nov 22 17:38 ..
0 drwxr-xr-x@ 10 paularmand  staff   340B Nov 22 17:38 .git
0 -rw-r--r--   1 paularmand  staff     0B Nov 22 17:38 README.md
paularmandsmbp.rto.be 05:38:37 (master) ~/dev_habitat/data_nginx$ git add README.md
paularmandsmbp.rto.be 05:38:44 (master) ~/dev_habitat/data_nginx$ git commit -m "add README"
[master (root-commit) f29e7b9] add README
 Committer: Paul-Armand Verhaegen <paularmand@paularmandsmbp.rto.be>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
paularmandsmbp.rto.be 05:38:57 (master) ~/dev_habitat/data_nginx$ git config user.name "Paul-Armand Verhaegen"
paularmandsmbp.rto.be 05:39:15 (master) ~/dev_habitat/data_nginx$ git config user.email "paul-armand.verhaegen@innovatie.vrt.be"
paularmandsmbp.rto.be 05:39:25 (master) ~/dev_habitat/data_nginx$ git commit -m "add README"
On branch master
Your branch is based on 'origin/master', but the upstream is gone.
  (use "git branch --unset-upstream" to fixup)
nothing to commit, working directory clean
paularmandsmbp.rto.be 05:39:28 (master) ~/dev_habitat/data_nginx$ git push -u origin master
Counting objects: 3, done.
Writing objects: 100% (3/3), 229 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To git@gitlab.com:vrtoeni/data_nginx.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
paularmandsmbp.rto.be 05:39:41 (master) ~/dev_habitat/data_nginx$ ssh vrt_mastermind
Welcome to Ubuntu 14.04.5 LTS (GNU/Linux 3.13.0-92-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Thu Nov 17 12:27:11 UTC 2016

  System load:  0.0               Processes:           115
  Usage of /:   19.3% of 7.74GB   Users logged in:     1
  Memory usage: 37%               IP address for eth0: 172.18.0.34
  Swap usage:   0%

  Graph this data and manage this system at:
    https://landscape.canonical.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

7 packages can be updated.
7 updates are security updates.

New release '16.04.1 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


*** System restart required ***
Last login: Thu Nov 17 12:27:41 2016 from ip-172-18-0-34.eu-west-1.compute.internal
ubuntu@mastermind:~$ cd /data/
logs/     programs/ projects/ 
ubuntu@mastermind:~$ cd /data/projects/habitat-deploy/
ubuntu@mastermind:/data/projects/habitat-deploy$ ll
total 52
drwxrwsr-x  6 ubuntu ubuntu 4096 Nov 15 08:08 ./
drwxr-sr-x  3 ubuntu ubuntu 4096 Oct  7 07:38 ../
drwxrwsr-x  8 ubuntu ubuntu 4096 Nov 17 12:27 .git/
-rw-rw-r--  1 ubuntu ubuntu    5 Oct  7 07:38 .gitignore
-rw-rw-r--  1 ubuntu ubuntu  183 Nov 15 08:08 README.md
drwxrwsr-x  8 ubuntu ubuntu 4096 Nov 15 12:31 ansible/
drwxrwsr-x 12 ubuntu ubuntu 4096 Oct 14 14:59 ansible-elasticsearch/
-rw-rw-r--  1 ubuntu ubuntu   28 Oct 27 07:56 apps.retry
-rw-rw-r--  1 ubuntu ubuntu   16 Oct 17 16:18 elasticsearch.retry
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov 15 08:05 essm/
-rw-rw-r--  1 ubuntu ubuntu   38 Oct 27 07:44 openresty.retry
-rw-rw-r--  1 ubuntu ubuntu   17 Oct 17 13:45 pio.retry
-rw-rw-r--  1 ubuntu ubuntu   48 Oct 27 08:54 zookeeper.retry
ubuntu@mastermind:/data/projects/habitat-deploy$ git pull
remote: Counting objects: 8, done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 8 (delta 5), reused 0 (delta 0)
Unpacking objects: 100% (8/8), done.
From gitlab.com:vrtoeni/habitat-deploy
   d492a4b..f25181d  master     -> origin/master
Updating d492a4b..f25181d
Fast-forward
 ansible/files/nginx.conf               | 118 ----------------------------------------------------------------------------------------------------------------------
 ansible/roles/openresty/tasks/main.yml |  19 +++++++++++++++----
 2 files changed, 15 insertions(+), 122 deletions(-)
 delete mode 100644 ansible/files/nginx.conf
ubuntu@mastermind:/data/projects/habitat-deploy$ ansible-p
ansible-playbook  ansible-pull      
ubuntu@mastermind:/data/projects/habitat-deploy$ cd ansible
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -i etc/hosts openresty.yml 

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : install_language-pack-en-base] **********************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : install git] ****************************************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : Allow limits to be read from /etc/security/limits.conf] *********
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Set nofile limits] **********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nofile 65532)

TASK [common : Set nproc limits] ***********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nproc 65532)

TASK [common : Set swappiness to 1] ********************************************
ok: [nginx2.oeni.vrt.be]
ok: [nginx1.oeni.vrt.be]

TASK [common : Include partitioning.yml] ***************************************
included: /data/projects/habitat-deploy/ansible/roles/common/tasks/partitioning.yml for nginx1.oeni.vrt.be, nginx2.oeni.vrt.be

TASK [common : Create the filesystem on disk sdb] ******************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Disable periodic fsck on sdb] ***********************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Mount datanode disks under /data/{0..n}] ************************
skipping: [nginx1.oeni.vrt.be] => (item=(0, u'sdb')) 
skipping: [nginx2.oeni.vrt.be] => (item=(0, u'sdb')) 

TASK [common-ssh : add ssh keys for the different accounts] ********************
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
changed: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})
changed: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})

TASK [openresty : info about extra vars] ***************************************
ok: [nginx1.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}
ok: [nginx2.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}

TASK [openresty : install prerequisites] ***************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for openresty] ******************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : unpack openresty directly] ***********************************
ok: [nginx2.oeni.vrt.be]
changed: [nginx1.oeni.vrt.be]

TASK [openresty : create directory for logs] ***********************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [openresty : git clone our openresty] *************************************
fatal: [nginx2.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "fatal: could not create work tree dir '/data/programs/data_nginx_conf'.: Permission denied", "rc": 128, "stderr": "fatal: could not create work tree dir '/data/programs/data_nginx_conf'.: Permission denied\n", "stdout": "", "stdout_lines": []}
fatal: [nginx1.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "fatal: could not create work tree dir '/data/programs/data_nginx_conf'.: Permission denied", "rc": 128, "stderr": "fatal: could not create work tree dir '/data/programs/data_nginx_conf'.: Permission denied\n", "stdout": "", "stdout_lines": []}

RUNNING HANDLER [common : rebuild locales] *************************************
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=14   changed=5    unreachable=0    failed=1   
nginx2.oeni.vrt.be         : ok=14   changed=4    unreachable=0    failed=1   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ locate .ssh
/home/ubuntu/.ssh
/home/ubuntu/.ssh/authorized_keys
/home/ubuntu/.ssh/config
/home/ubuntu/.ssh/id_rsa
/home/ubuntu/.ssh/id_rsa.pub
/home/ubuntu/.ssh/known_hosts
/home/ubuntu/.ssh/known_hosts.old
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git pull
remote: Counting objects: 7, done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 7 (delta 4), reused 0 (delta 0)
Unpacking objects: 100% (7/7), done.
From gitlab.com:vrtoeni/habitat-deploy
   f25181d..04237fb  master     -> origin/master
Updating f25181d..04237fb
Fast-forward
 ansible/roles/openresty/tasks/main.yml | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -i etc/hosts openresty.yml 

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : install_language-pack-en-base] **********************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : install git] ****************************************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : Allow limits to be read from /etc/security/limits.conf] *********
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Set nofile limits] **********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nofile 65532)

TASK [common : Set nproc limits] ***********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nproc 65532)

TASK [common : Set swappiness to 1] ********************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Include partitioning.yml] ***************************************
included: /data/projects/habitat-deploy/ansible/roles/common/tasks/partitioning.yml for nginx1.oeni.vrt.be, nginx2.oeni.vrt.be

TASK [common : Create the filesystem on disk sdb] ******************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Disable periodic fsck on sdb] ***********************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Mount datanode disks under /data/{0..n}] ************************
skipping: [nginx1.oeni.vrt.be] => (item=(0, u'sdb')) 
skipping: [nginx2.oeni.vrt.be] => (item=(0, u'sdb')) 

TASK [common-ssh : add ssh keys for the different accounts] ********************
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})

TASK [openresty : info about extra vars] ***************************************
ok: [nginx1.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}
ok: [nginx2.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}

TASK [openresty : install prerequisites] ***************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for openresty] ******************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : unpack openresty directly] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for logs] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : git clone our openresty] *************************************
fatal: [nginx1.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "Cloning into '/data/programs/data_nginx_conf'...\nWarning: Identity file /home/ubuntu/.ssh/id_rsa.pub not accessible: No such file or directory.\nWarning: Permanently added the RSA host key for IP address '104.210.2.228' to the list of known hosts.\r\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nWarning: Identity file /home/ubuntu/.ssh/id_rsa.pub not accessible: No such file or directory.\nWarning: Permanently added the RSA host key for IP address '104.210.2.228' to the list of known hosts.\r\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stdout": "", "stdout_lines": []}
fatal: [nginx2.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "Cloning into '/data/programs/data_nginx_conf'...\nWarning: Identity file /home/ubuntu/.ssh/id_rsa.pub not accessible: No such file or directory.\nWarning: Permanently added the RSA host key for IP address '104.210.2.228' to the list of known hosts.\r\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nWarning: Identity file /home/ubuntu/.ssh/id_rsa.pub not accessible: No such file or directory.\nWarning: Permanently added the RSA host key for IP address '104.210.2.228' to the list of known hosts.\r\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stdout": "", "stdout_lines": []}

RUNNING HANDLER [common : rebuild locales] *************************************
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=14   changed=2    unreachable=0    failed=1   
nginx2.oeni.vrt.be         : ok=14   changed=2    unreachable=0    failed=1   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git pull
remote: Counting objects: 7, done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 7 (delta 4), reused 0 (delta 0)
Unpacking objects: 100% (7/7), done.
From gitlab.com:vrtoeni/habitat-deploy
   04237fb..e0f14cf  master     -> origin/master
Updating 04237fb..e0f14cf
Fast-forward
 ansible/roles/openresty/tasks/main.yml | 11 +++++++++--
 1 file changed, 9 insertions(+), 2 deletions(-)
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -i etc/hosts openresty.yml 

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : install_language-pack-en-base] **********************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : install git] ****************************************************
changed: [nginx2.oeni.vrt.be]
changed: [nginx1.oeni.vrt.be]

TASK [common : Allow limits to be read from /etc/security/limits.conf] *********
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Set nofile limits] **********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nofile 65532)

TASK [common : Set nproc limits] ***********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nproc 65532)

TASK [common : Set swappiness to 1] ********************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Include partitioning.yml] ***************************************
included: /data/projects/habitat-deploy/ansible/roles/common/tasks/partitioning.yml for nginx2.oeni.vrt.be, nginx1.oeni.vrt.be

TASK [common : Create the filesystem on disk sdb] ******************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Disable periodic fsck on sdb] ***********************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Mount datanode disks under /data/{0..n}] ************************
skipping: [nginx1.oeni.vrt.be] => (item=(0, u'sdb')) 
skipping: [nginx2.oeni.vrt.be] => (item=(0, u'sdb')) 

TASK [common-ssh : add ssh keys for the different accounts] ********************
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})

TASK [openresty : info about extra vars] ***************************************
ok: [nginx1.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}
ok: [nginx2.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}

TASK [openresty : install prerequisites] ***************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for openresty] ******************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : unpack openresty directly] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for logs] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for nginx conf] *****************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [openresty : git clone our openresty] *************************************
fatal: [nginx1.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "Cloning into '/data/programs/data_nginx_conf'...\nWarning: Permanently added the RSA host key for IP address '104.210.2.228' to the list of known hosts.\r\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nWarning: Permanently added the RSA host key for IP address '104.210.2.228' to the list of known hosts.\r\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stdout": "", "stdout_lines": []}
fatal: [nginx2.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "Cloning into '/data/programs/data_nginx_conf'...\nWarning: Permanently added the RSA host key for IP address '104.210.2.228' to the list of known hosts.\r\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nWarning: Permanently added the RSA host key for IP address '104.210.2.228' to the list of known hosts.\r\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stdout": "", "stdout_lines": []}

RUNNING HANDLER [common : rebuild locales] *************************************
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=15   changed=3    unreachable=0    failed=1   
nginx2.oeni.vrt.be         : ok=15   changed=3    unreachable=0    failed=1   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ifconfig
eth0      Link encap:Ethernet  HWaddr 06:2f:ad:3c:43:21  
          inet addr:172.18.0.34  Bcast:172.18.0.255  Mask:255.255.255.0
          inet6 addr: fe80::42f:adff:fe3c:4321/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
          RX packets:2033090 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1991966 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:759899415 (759.8 MB)  TX bytes:1692641599 (1.6 GB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:321931 errors:0 dropped:0 overruns:0 frame:0
          TX packets:321931 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:55341082 (55.3 MB)  TX bytes:55341082 (55.3 MB)

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ packet_write_wait: Connection to 54.194.37.69: Broken pipe
paularmandsmbp.rto.be 06:20:14 (master) ~/dev_habitat/data_nginx$ ssh vrt_mastermind
^C
paularmandsmbp.rto.be 08:53:56 (master) ~/dev_habitat/data_nginx$ ssh vrt_mastermind
Welcome to Ubuntu 14.04.5 LTS (GNU/Linux 3.13.0-92-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Tue Nov 22 17:05:28 UTC 2016

  System load:  0.0               Processes:           105
  Usage of /:   19.3% of 7.74GB   Users logged in:     0
  Memory usage: 28%               IP address for eth0: 172.18.0.34
  Swap usage:   0%

  Graph this data and manage this system at:
    https://landscape.canonical.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

10 packages can be updated.
8 updates are security updates.


*** System restart required ***
Last login: Tue Nov 22 17:05:30 2016 from 95.130.40.188
ubuntu@mastermind:~$ cd /data
bin/        data/       etc/        lib/        lost+found/ mnt/        proc/       run/        srv/        tmp/        var/
boot/       dev/        home/       lib64/      media/      opt/        root/       sbin/       sys/        usr/        
ubuntu@mastermind:~$ cd /data
ubuntu@mastermind:/data$ cd 
logs/     programs/ projects/ 
ubuntu@mastermind:/data$ cd projects/
ubuntu@mastermind:/data/projects$ cd habitat-deploy/
ansible/               ansible-elasticsearch/ essm/                  .git/                  
ubuntu@mastermind:/data/projects$ cd habitat-deploy/ansible
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ll
total 72
drwxrwsr-x  8 ubuntu ubuntu 4096 Nov 22 17:06 ./
drwxrwsr-x  6 ubuntu ubuntu 4096 Nov 15 08:08 ../
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov  8 14:56 ansible-elasticsearch/
-rw-rw-r--  1 ubuntu ubuntu  206 Nov  8 14:56 apps.yml
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov 15 08:05 etc/
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov 22 17:05 files/
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov 17 12:27 group_vars/
-rw-rw-r--  1 ubuntu ubuntu  122 Nov  8 14:56 hadoop.yml
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov  8 14:56 host_vars/
-rw-rw-r--  1 ubuntu ubuntu   24 Nov 17 09:12 hubot.retry
-rw-rw-r--  1 ubuntu ubuntu   99 Nov 15 08:05 hubot.yml
-rw-rw-r--  1 ubuntu ubuntu  156 Nov  8 14:56 kafka.yml
-rw-rw-r--  1 ubuntu ubuntu   38 Nov 22 17:15 openresty.retry
-rw-rw-r--  1 ubuntu ubuntu  107 Nov  8 14:56 openresty.yml
-rw-rw-r--  1 ubuntu ubuntu  389 Nov  8 14:56 pio.yml
-rw-rw-r--  1 ubuntu ubuntu  932 Nov  8 14:56 pio_elasticsearch.yml
drwxrwsr-x 13 ubuntu ubuntu 4096 Nov 15 08:05 roles/
-rw-rw-r--  1 ubuntu ubuntu  118 Nov  8 14:56 zookeeper.yml
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ll
total 72
drwxrwsr-x  8 ubuntu ubuntu 4096 Nov 22 17:06 ./
drwxrwsr-x  6 ubuntu ubuntu 4096 Nov 15 08:08 ../
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov  8 14:56 ansible-elasticsearch/
-rw-rw-r--  1 ubuntu ubuntu  206 Nov  8 14:56 apps.yml
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov 15 08:05 etc/
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov 22 17:05 files/
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov 17 12:27 group_vars/
-rw-rw-r--  1 ubuntu ubuntu  122 Nov  8 14:56 hadoop.yml
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov  8 14:56 host_vars/
-rw-rw-r--  1 ubuntu ubuntu   24 Nov 17 09:12 hubot.retry
-rw-rw-r--  1 ubuntu ubuntu   99 Nov 15 08:05 hubot.yml
-rw-rw-r--  1 ubuntu ubuntu  156 Nov  8 14:56 kafka.yml
-rw-rw-r--  1 ubuntu ubuntu   38 Nov 22 17:15 openresty.retry
-rw-rw-r--  1 ubuntu ubuntu  107 Nov  8 14:56 openresty.yml
-rw-rw-r--  1 ubuntu ubuntu  389 Nov  8 14:56 pio.yml
-rw-rw-r--  1 ubuntu ubuntu  932 Nov  8 14:56 pio_elasticsearch.yml
drwxrwsr-x 13 ubuntu ubuntu 4096 Nov 15 08:05 roles/
-rw-rw-r--  1 ubuntu ubuntu  118 Nov  8 14:56 zookeeper.yml
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -i etc/hosts openresty.yml 

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : install_language-pack-en-base] **********************************
changed: [nginx2.oeni.vrt.be]
changed: [nginx1.oeni.vrt.be]

TASK [common : install git] ****************************************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : Allow limits to be read from /etc/security/limits.conf] *********
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Set nofile limits] **********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nofile 65532)

TASK [common : Set nproc limits] ***********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nproc 65532)

TASK [common : Set swappiness to 1] ********************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Include partitioning.yml] ***************************************
included: /data/projects/habitat-deploy/ansible/roles/common/tasks/partitioning.yml for nginx1.oeni.vrt.be, nginx2.oeni.vrt.be

TASK [common : Create the filesystem on disk sdb] ******************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Disable periodic fsck on sdb] ***********************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Mount datanode disks under /data/{0..n}] ************************
skipping: [nginx1.oeni.vrt.be] => (item=(0, u'sdb')) 
skipping: [nginx2.oeni.vrt.be] => (item=(0, u'sdb')) 

TASK [common-ssh : add ssh keys for the different accounts] ********************
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})

TASK [openresty : info about extra vars] ***************************************
ok: [nginx1.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}
ok: [nginx2.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}

TASK [openresty : install prerequisites] ***************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for openresty] ******************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : unpack openresty directly] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for logs] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for nginx conf] *****************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : git clone our openresty] *************************************
fatal: [nginx1.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stdout": "", "stdout_lines": []}
fatal: [nginx2.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stdout": "", "stdout_lines": []}

RUNNING HANDLER [common : rebuild locales] *************************************
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=15   changed=2    unreachable=0    failed=1   
nginx2.oeni.vrt.be         : ok=15   changed=2    unreachable=0    failed=1   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ cd ..
ubuntu@mastermind:/data/projects/habitat-deploy$ cd ..
ubuntu@mastermind:/data/projects$ cd ../programs/
ubuntu@mastermind:/data/programs$ git clone git@gitlab.com:vrtoeni/data_nginx_conf.git
Cloning into 'data_nginx_conf'...
remote: Counting objects: 3, done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (3/3), done.
Checking connectivity... done.
ubuntu@mastermind:/data/programs$ ll
total 16
drwxr-xr-x 4 ubuntu root   4096 Nov 23 09:25 ./
drwxr-xr-x 5 root   root   4096 Nov 17 09:08 ../
drwxrwxr-x 8 ubuntu ubuntu 4096 Nov 17 12:31 baldrick/
drwxrwxr-x 3 ubuntu ubuntu 4096 Nov 23 09:25 data_nginx_conf/
ubuntu@mastermind:/data/programs$ cd ../projects/habitat-deploy/ansible
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -i etc/hosts openresty.yml 

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
ok: [nginx2.oeni.vrt.be]
ok: [nginx1.oeni.vrt.be]

TASK [common : install_language-pack-en-base] **********************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : install git] ****************************************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : Allow limits to be read from /etc/security/limits.conf] *********
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Set nofile limits] **********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nofile 65532)

TASK [common : Set nproc limits] ***********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nproc 65532)

TASK [common : Set swappiness to 1] ********************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Include partitioning.yml] ***************************************
included: /data/projects/habitat-deploy/ansible/roles/common/tasks/partitioning.yml for nginx2.oeni.vrt.be, nginx1.oeni.vrt.be

TASK [common : Create the filesystem on disk sdb] ******************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Disable periodic fsck on sdb] ***********************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Mount datanode disks under /data/{0..n}] ************************
skipping: [nginx1.oeni.vrt.be] => (item=(0, u'sdb')) 
skipping: [nginx2.oeni.vrt.be] => (item=(0, u'sdb')) 

TASK [common-ssh : add ssh keys for the different accounts] ********************
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})

TASK [openresty : info about extra vars] ***************************************
ok: [nginx1.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}
ok: [nginx2.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}

TASK [openresty : install prerequisites] ***************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for openresty] ******************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : unpack openresty directly] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for logs] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for nginx conf] *****************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : git clone our openresty] *************************************
fatal: [nginx2.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stdout": "", "stdout_lines": []}
fatal: [nginx1.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stdout": "", "stdout_lines": []}

RUNNING HANDLER [common : rebuild locales] *************************************
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=15   changed=2    unreachable=0    failed=1   
nginx2.oeni.vrt.be         : ok=15   changed=2    unreachable=0    failed=1   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git pull
remote: Counting objects: 7, done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 7 (delta 4), reused 0 (delta 0)
Unpacking objects: 100% (7/7), done.
From gitlab.com:vrtoeni/habitat-deploy
   e0f14cf..f30525b  master     -> origin/master
Updating e0f14cf..f30525b
Fast-forward
 ansible/roles/openresty/tasks/main.yml | 9 +++++++++
 1 file changed, 9 insertions(+)
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -i etc/hosts openresty.yml 

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : install_language-pack-en-base] **********************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : install git] ****************************************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : Allow limits to be read from /etc/security/limits.conf] *********
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Set nofile limits] **********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nofile 65532)

TASK [common : Set nproc limits] ***********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nproc 65532)

TASK [common : Set swappiness to 1] ********************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Include partitioning.yml] ***************************************
included: /data/projects/habitat-deploy/ansible/roles/common/tasks/partitioning.yml for nginx1.oeni.vrt.be, nginx2.oeni.vrt.be

TASK [common : Create the filesystem on disk sdb] ******************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Disable periodic fsck on sdb] ***********************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Mount datanode disks under /data/{0..n}] ************************
skipping: [nginx1.oeni.vrt.be] => (item=(0, u'sdb')) 
skipping: [nginx2.oeni.vrt.be] => (item=(0, u'sdb')) 

TASK [common-ssh : add ssh keys for the different accounts] ********************
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})

TASK [openresty : info about extra vars] ***************************************
ok: [nginx1.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}
ok: [nginx2.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}

TASK [openresty : install prerequisites] ***************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for openresty] ******************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : unpack openresty directly] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for logs] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for nginx conf] *****************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : git clone our openresty] *************************************
fatal: [nginx1.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stdout": "", "stdout_lines": []}
fatal: [nginx2.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stdout": "", "stdout_lines": []}

RUNNING HANDLER [common : rebuild locales] *************************************
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=15   changed=2    unreachable=0    failed=1   
nginx2.oeni.vrt.be         : ok=15   changed=2    unreachable=0    failed=1   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ Timeout, server 54.194.37.69 not responding.
paularmandsmbp.rto.be 10:38:11 (master) ~/dev_habitat/data_nginx$ ll /data/programs
ls: /data/programs: No such file or directory
paularmandsmbp.rto.be 10:49:07 (master) ~/dev_habitat/data_nginx$ ssh vrt_mastermind
^C
paularmandsmbp.rto.be 10:49:33 (master) ~/dev_habitat/data_nginx$ ssh vrt_mastermind
Welcome to Ubuntu 14.04.5 LTS (GNU/Linux 3.13.0-92-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Wed Nov 23 07:55:26 UTC 2016

  System load:  0.0               Processes:           105
  Usage of /:   19.3% of 7.74GB   Users logged in:     0
  Memory usage: 28%               IP address for eth0: 172.18.0.34
  Swap usage:   0%

  Graph this data and manage this system at:
    https://landscape.canonical.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

19 packages can be updated.
17 updates are security updates.

New release '16.04.1 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


*** System restart required ***
Last login: Wed Nov 23 07:55:28 2016 from vpn.lab.vrt.be
ubuntu@mastermind:~$ cd /data/programs
ubuntu@mastermind:/data/programs$ ll
total 16
drwxr-xr-x 4 ubuntu root   4096 Nov 23 09:25 ./
drwxr-xr-x 5 root   root   4096 Nov 17 09:08 ../
drwxrwxr-x 8 ubuntu ubuntu 4096 Nov 17 12:31 baldrick/
drwxrwxr-x 3 ubuntu ubuntu 4096 Nov 23 09:25 data_nginx_conf/
ubuntu@mastermind:/data/programs$ cd data_nginx_conf/
ubuntu@mastermind:/data/programs/data_nginx_conf$ ll
total 12
drwxrwxr-x 3 ubuntu ubuntu 4096 Nov 23 09:25 ./
drwxr-xr-x 4 ubuntu root   4096 Nov 23 09:25 ../
drwxrwxr-x 8 ubuntu ubuntu 4096 Nov 23 09:25 .git/
-rw-rw-r-- 1 ubuntu ubuntu    0 Nov 23 09:25 README.md
ubuntu@mastermind:/data/programs/data_nginx_conf$ vi .git/
branches/    description  hooks/       info/        objects/     refs/        
config       HEAD         index        logs/        packed-refs  
ubuntu@mastermind:/data/programs/data_nginx_conf$ vi .git/
branches/    description  hooks/       info/        objects/     refs/        
config       HEAD         index        logs/        packed-refs  
ubuntu@mastermind:/data/programs/data_nginx_conf$ vi .git/config 
ubuntu@mastermind:/data/programs/data_nginx_conf$ cd ..
ubuntu@mastermind:/data/programs$ ll
total 16
drwxr-xr-x 4 ubuntu root   4096 Nov 23 09:25 ./
drwxr-xr-x 5 root   root   4096 Nov 17 09:08 ../
drwxrwxr-x 8 ubuntu ubuntu 4096 Nov 17 12:31 baldrick/
drwxrwxr-x 3 ubuntu ubuntu 4096 Nov 23 09:25 data_nginx_conf/
ubuntu@mastermind:/data/programs$ cd ../projects/habitat-deploy/ansible
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -i etc/hosts openresty.yml 

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : install_language-pack-en-base] **********************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : install git] ****************************************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : Allow limits to be read from /etc/security/limits.conf] *********
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Set nofile limits] **********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nofile 65532)

TASK [common : Set nproc limits] ***********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nproc 65532)

TASK [common : Set swappiness to 1] ********************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Include partitioning.yml] ***************************************
included: /data/projects/habitat-deploy/ansible/roles/common/tasks/partitioning.yml for nginx1.oeni.vrt.be, nginx2.oeni.vrt.be

TASK [common : Create the filesystem on disk sdb] ******************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Disable periodic fsck on sdb] ***********************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Mount datanode disks under /data/{0..n}] ************************
skipping: [nginx2.oeni.vrt.be] => (item=(0, u'sdb')) 
skipping: [nginx1.oeni.vrt.be] => (item=(0, u'sdb')) 

TASK [common-ssh : add ssh keys for the different accounts] ********************
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})

TASK [openresty : info about extra vars] ***************************************
ok: [nginx1.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}
ok: [nginx2.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}

TASK [openresty : install prerequisites] ***************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for openresty] ******************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : unpack openresty directly] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for logs] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for nginx conf] *****************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [openresty : git clone our openresty] *************************************
fatal: [nginx1.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stdout": "", "stdout_lines": []}
fatal: [nginx2.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stdout": "", "stdout_lines": []}

RUNNING HANDLER [common : rebuild locales] *************************************
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=15   changed=3    unreachable=0    failed=1   
nginx2.oeni.vrt.be         : ok=15   changed=3    unreachable=0    failed=1   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ll /data/programs/data_nginx_conf
total 12
drwxrwxr-x 3 ubuntu ubuntu 4096 Nov 23 09:25 ./
drwxr-xr-x 4 ubuntu root   4096 Nov 23 09:25 ../
drwxrwxr-x 8 ubuntu ubuntu 4096 Nov 23 09:51 .git/
-rw-rw-r-- 1 ubuntu ubuntu    0 Nov 23 09:25 README.md
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ cat /home/ubuntu/.ssh/
authorized_keys  config           id_rsa           id_rsa.pub       known_hosts      known_hosts.old  
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ cat /home/ubuntu/.ssh/id_rsa.pub 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDD5CutdZdUmeKda2in9SGsl4JtC/fjX5OXr3AFZz4/nr0hv178NinnX734pZU46PGpNzg/RG1yWosQeoEhjz7KYzlFnsVXUpS41FFnYh1g+VtZC2CDgIljNbQGMXDJrdDmGbFNWZicdj1MtLEl3f88L6YxOf7aa37wxmShWz9kc8BjZgbop+tZTZoL+DHYAz4/Z6Jn0QgY+Omhii5nGiIrMAIr+sd7RhBnfLPD9/smHyCmQLNmeOzse+E0RymQqD7fa6ufCXkrg/NajQqQ3OerVjBu2tJ4axSKU0iQ9nZJjER1WR2ygeoFF+iY77hrYdv+wwU5tjWuGNgH/gMSwouH gitlab+janitor@innovatie.vrt.be
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ll /home/ubuntu/.ssh/id_rsa.pub 
-rw-r--r-- 1 ubuntu ubuntu 413 Oct  7 07:35 /home/ubuntu/.ssh/id_rsa.pub
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git pull
remote: Counting objects: 7, done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 7 (delta 4), reused 0 (delta 0)
Unpacking objects: 100% (7/7), done.
From gitlab.com:vrtoeni/habitat-deploy
   f30525b..caf39d9  master     -> origin/master
Updating f30525b..caf39d9
Fast-forward
 ansible/roles/openresty/tasks/main.yml | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -i etc/hosts openresty.yml 

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : install_language-pack-en-base] **********************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : install git] ****************************************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : Allow limits to be read from /etc/security/limits.conf] *********
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Set nofile limits] **********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nofile 65532)

TASK [common : Set nproc limits] ***********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nproc 65532)

TASK [common : Set swappiness to 1] ********************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Include partitioning.yml] ***************************************
included: /data/projects/habitat-deploy/ansible/roles/common/tasks/partitioning.yml for nginx1.oeni.vrt.be, nginx2.oeni.vrt.be

TASK [common : Create the filesystem on disk sdb] ******************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Disable periodic fsck on sdb] ***********************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Mount datanode disks under /data/{0..n}] ************************
skipping: [nginx1.oeni.vrt.be] => (item=(0, u'sdb')) 
skipping: [nginx2.oeni.vrt.be] => (item=(0, u'sdb')) 

TASK [common-ssh : add ssh keys for the different accounts] ********************
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})

TASK [openresty : info about extra vars] ***************************************
ok: [nginx1.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}
ok: [nginx2.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}

TASK [openresty : install prerequisites] ***************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for openresty] ******************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : unpack openresty directly] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for logs] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for nginx conf] *****************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [openresty : git clone our openresty] *************************************
fatal: [nginx1.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stdout": "", "stdout_lines": []}
fatal: [nginx2.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stdout": "", "stdout_lines": []}

RUNNING HANDLER [common : rebuild locales] *************************************
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=15   changed=3    unreachable=0    failed=1   
nginx2.oeni.vrt.be         : ok=15   changed=3    unreachable=0    failed=1   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -vvv ^C etc/hosts openresty.yml 
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ vi openresty.yml 
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ vi openresty.yml 
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -vvv -i etc/hosts openresty.yml 
Using /etc/ansible/ansible.cfg as config file

PLAYBOOK: openresty.yml ********************************************************
1 plays in openresty.yml

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/system/setup.py
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895385.36-179388925000861 `" && echo ansible-tmp-1479895385.36-179388925000861="` echo $HOME/.ansible/tmp/ansible-tmp-1479895385.36-179388925000861 `" ) && sleep 0'"'"''
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/system/setup.py
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895385.36-237548065176415 `" && echo ansible-tmp-1479895385.36-237548065176415="` echo $HOME/.ansible/tmp/ansible-tmp-1479895385.36-237548065176415 `" ) && sleep 0'"'"''
fatal: [nginx2.oeni.vrt.be]: UNREACHABLE! => {
    "changed": false, 
    "msg": "Failed to connect to the host via ssh: mux_client_hello_exchange: write packet: Broken pipe\r\n", 
    "unreachable": true
}
fatal: [nginx1.oeni.vrt.be]: UNREACHABLE! => {
    "changed": false, 
    "msg": "Failed to connect to the host via ssh: mux_client_hello_exchange: write packet: Broken pipe\r\n", 
    "unreachable": true
}
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=0    changed=0    unreachable=1    failed=0   
nginx2.oeni.vrt.be         : ok=0    changed=0    unreachable=1    failed=0   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -vvv -i etc/hosts openresty.yml 
Using /etc/ansible/ansible.cfg as config file

PLAYBOOK: openresty.yml ********************************************************
1 plays in openresty.yml

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/system/setup.py
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895406.29-11764854849435 `" && echo ansible-tmp-1479895406.29-11764854849435="` echo $HOME/.ansible/tmp/ansible-tmp-1479895406.29-11764854849435 `" ) && sleep 0'"'"''
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/system/setup.py
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895406.29-124005142299983 `" && echo ansible-tmp-1479895406.29-124005142299983="` echo $HOME/.ansible/tmp/ansible-tmp-1479895406.29-124005142299983 `" ) && sleep 0'"'"''
<nginx1.oeni.vrt.be> PUT /tmp/tmpo4EQ7a TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895406.29-124005142299983/setup.py
<nginx1.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx1.oeni.vrt.be]'
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895406.29-124005142299983/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895406.29-124005142299983/setup.py && sleep 0'"'"''
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r -tt nginx1.oeni.vrt.be '/bin/sh -c '"'"'sudo -H -S -n -u root /bin/sh -c '"'"'"'"'"'"'"'"'echo BECOME-SUCCESS-xkcftdjfwnkncrfxagingvweqlilpupu; /usr/bin/python /home/ubuntu/.ansible/tmp/ansible-tmp-1479895406.29-124005142299983/setup.py; rm -rf "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895406.29-124005142299983/" > /dev/null 2>&1'"'"'"'"'"'"'"'"' && sleep 0'"'"''
<nginx2.oeni.vrt.be> PUT /tmp/tmpk5F0d5 TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895406.29-11764854849435/setup.py
<nginx2.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx2.oeni.vrt.be]'
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895406.29-11764854849435/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895406.29-11764854849435/setup.py && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r -tt nginx2.oeni.vrt.be '/bin/sh -c '"'"'sudo -H -S -n -u root /bin/sh -c '"'"'"'"'"'"'"'"'echo BECOME-SUCCESS-erwczycasmvuxymwehpqynfgocuxpaam; /usr/bin/python /home/ubuntu/.ansible/tmp/ansible-tmp-1479895406.29-11764854849435/setup.py; rm -rf "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895406.29-11764854849435/" > /dev/null 2>&1'"'"'"'"'"'"'"'"' && sleep 0'"'"''
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : info about extra vars] ***************************************
task path: /data/projects/habitat-deploy/ansible/roles/openresty/tasks/main.yml:1
ok: [nginx1.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}
ok: [nginx2.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}

TASK [openresty : install prerequisites] ***************************************
task path: /data/projects/habitat-deploy/ansible/roles/openresty/tasks/main.yml:4
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/packaging/os/apt.py
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895407.36-163230785422034 `" && echo ansible-tmp-1479895407.36-163230785422034="` echo $HOME/.ansible/tmp/ansible-tmp-1479895407.36-163230785422034 `" ) && sleep 0'"'"''
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/packaging/os/apt.py
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895407.36-84302775156328 `" && echo ansible-tmp-1479895407.36-84302775156328="` echo $HOME/.ansible/tmp/ansible-tmp-1479895407.36-84302775156328 `" ) && sleep 0'"'"''
<nginx2.oeni.vrt.be> PUT /tmp/tmpYJkywb TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.36-163230785422034/apt.py
<nginx2.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx2.oeni.vrt.be]'
<nginx1.oeni.vrt.be> PUT /tmp/tmpY5PIeV TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.36-84302775156328/apt.py
<nginx1.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx1.oeni.vrt.be]'
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.36-84302775156328/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.36-84302775156328/apt.py && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.36-163230785422034/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.36-163230785422034/apt.py && sleep 0'"'"''
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r -tt nginx1.oeni.vrt.be '/bin/sh -c '"'"'sudo -H -S -n -u root /bin/sh -c '"'"'"'"'"'"'"'"'echo BECOME-SUCCESS-jubagxlawlvfnmxuukhjflitymltrexb; /usr/bin/python /home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.36-84302775156328/apt.py; rm -rf "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.36-84302775156328/" > /dev/null 2>&1'"'"'"'"'"'"'"'"' && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r -tt nginx2.oeni.vrt.be '/bin/sh -c '"'"'sudo -H -S -n -u root /bin/sh -c '"'"'"'"'"'"'"'"'echo BECOME-SUCCESS-mutqapsxgctxksnlctzayytaakaqbfjb; /usr/bin/python /home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.36-163230785422034/apt.py; rm -rf "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.36-163230785422034/" > /dev/null 2>&1'"'"'"'"'"'"'"'"' && sleep 0'"'"''
ok: [nginx1.oeni.vrt.be] => {
    "cache_update_time": 1479895315, 
    "cache_updated": false, 
    "changed": false, 
    "invocation": {
        "module_args": {
            "allow_unauthenticated": false, 
            "autoremove": false, 
            "cache_valid_time": 86400, 
            "deb": null, 
            "default_release": null, 
            "dpkg_options": "force-confdef,force-confold", 
            "force": false, 
            "install_recommends": null, 
            "name": "libreadline-dev,libncurses5-dev,libpcre3-dev,libssl-dev,perl,make,build-essential", 
            "only_upgrade": false, 
            "package": [
                "libreadline-dev", 
                "libncurses5-dev", 
                "libpcre3-dev", 
                "libssl-dev", 
                "perl", 
                "make", 
                "build-essential"
            ], 
            "purge": false, 
            "state": "present", 
            "update_cache": true, 
            "upgrade": null
        }, 
        "module_name": "apt"
    }
}
ok: [nginx2.oeni.vrt.be] => {
    "cache_update_time": 1479895312, 
    "cache_updated": false, 
    "changed": false, 
    "invocation": {
        "module_args": {
            "allow_unauthenticated": false, 
            "autoremove": false, 
            "cache_valid_time": 86400, 
            "deb": null, 
            "default_release": null, 
            "dpkg_options": "force-confdef,force-confold", 
            "force": false, 
            "install_recommends": null, 
            "name": "libreadline-dev,libncurses5-dev,libpcre3-dev,libssl-dev,perl,make,build-essential", 
            "only_upgrade": false, 
            "package": [
                "libreadline-dev", 
                "libncurses5-dev", 
                "libpcre3-dev", 
                "libssl-dev", 
                "perl", 
                "make", 
                "build-essential"
            ], 
            "purge": false, 
            "state": "present", 
            "update_cache": true, 
            "upgrade": null
        }, 
        "module_name": "apt"
    }
}

TASK [openresty : create directory for openresty] ******************************
task path: /data/projects/habitat-deploy/ansible/roles/openresty/tasks/main.yml:10
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/files/file.py
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895407.91-115155570700171 `" && echo ansible-tmp-1479895407.91-115155570700171="` echo $HOME/.ansible/tmp/ansible-tmp-1479895407.91-115155570700171 `" ) && sleep 0'"'"''
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/files/file.py
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895407.91-203181513875251 `" && echo ansible-tmp-1479895407.91-203181513875251="` echo $HOME/.ansible/tmp/ansible-tmp-1479895407.91-203181513875251 `" ) && sleep 0'"'"''
<nginx2.oeni.vrt.be> PUT /tmp/tmpWTJPCV TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.91-115155570700171/file.py
<nginx2.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx2.oeni.vrt.be]'
<nginx1.oeni.vrt.be> PUT /tmp/tmpfVpKdq TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.91-203181513875251/file.py
<nginx1.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx1.oeni.vrt.be]'
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.91-203181513875251/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.91-203181513875251/file.py && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.91-115155570700171/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.91-115155570700171/file.py && sleep 0'"'"''
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r -tt nginx1.oeni.vrt.be '/bin/sh -c '"'"'sudo -H -S -n -u root /bin/sh -c '"'"'"'"'"'"'"'"'echo BECOME-SUCCESS-bjtmsgyeganvmvkcufjgjaiqwljkvzie; /usr/bin/python /home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.91-203181513875251/file.py; rm -rf "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.91-203181513875251/" > /dev/null 2>&1'"'"'"'"'"'"'"'"' && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r -tt nginx2.oeni.vrt.be '/bin/sh -c '"'"'sudo -H -S -n -u root /bin/sh -c '"'"'"'"'"'"'"'"'echo BECOME-SUCCESS-wxgvhovrtcmkoqhthfdyevlyifsflfhk; /usr/bin/python /home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.91-115155570700171/file.py; rm -rf "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895407.91-115155570700171/" > /dev/null 2>&1'"'"'"'"'"'"'"'"' && sleep 0'"'"''
ok: [nginx1.oeni.vrt.be] => {
    "changed": false, 
    "diff": {
        "after": {
            "path": "/data/programs"
        }, 
        "before": {
            "path": "/data/programs"
        }
    }, 
    "gid": 0, 
    "group": "root", 
    "invocation": {
        "module_args": {
            "backup": null, 
            "content": null, 
            "delimiter": null, 
            "diff_peek": null, 
            "directory_mode": null, 
            "follow": false, 
            "force": false, 
            "group": null, 
            "mode": null, 
            "original_basename": null, 
            "owner": null, 
            "path": "/data/programs", 
            "recurse": true, 
            "regexp": null, 
            "remote_src": null, 
            "selevel": null, 
            "serole": null, 
            "setype": null, 
            "seuser": null, 
            "src": null, 
            "state": "directory", 
            "unsafe_writes": null, 
            "validate": null
        }, 
        "module_name": "file"
    }, 
    "mode": "0755", 
    "owner": "root", 
    "path": "/data/programs", 
    "size": 4096, 
    "state": "directory", 
    "uid": 0
}
ok: [nginx2.oeni.vrt.be] => {
    "changed": false, 
    "diff": {
        "after": {
            "path": "/data/programs"
        }, 
        "before": {
            "path": "/data/programs"
        }
    }, 
    "gid": 0, 
    "group": "root", 
    "invocation": {
        "module_args": {
            "backup": null, 
            "content": null, 
            "delimiter": null, 
            "diff_peek": null, 
            "directory_mode": null, 
            "follow": false, 
            "force": false, 
            "group": null, 
            "mode": null, 
            "original_basename": null, 
            "owner": null, 
            "path": "/data/programs", 
            "recurse": true, 
            "regexp": null, 
            "remote_src": null, 
            "selevel": null, 
            "serole": null, 
            "setype": null, 
            "seuser": null, 
            "src": null, 
            "state": "directory", 
            "unsafe_writes": null, 
            "validate": null
        }, 
        "module_name": "file"
    }, 
    "mode": "0755", 
    "owner": "root", 
    "path": "/data/programs", 
    "size": 4096, 
    "state": "directory", 
    "uid": 0
}

TASK [openresty : unpack openresty directly] ***********************************
task path: /data/projects/habitat-deploy/ansible/roles/openresty/tasks/main.yml:16
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895408.1-85237097349884 `" && echo ansible-tmp-1479895408.1-85237097349884="` echo $HOME/.ansible/tmp/ansible-tmp-1479895408.1-85237097349884 `" ) && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895408.1-166938303598731 `" && echo ansible-tmp-1479895408.1-166938303598731="` echo $HOME/.ansible/tmp/ansible-tmp-1479895408.1-166938303598731 `" ) && sleep 0'"'"''
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/files/stat.py
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895408.21-225555537601235 `" && echo ansible-tmp-1479895408.21-225555537601235="` echo $HOME/.ansible/tmp/ansible-tmp-1479895408.21-225555537601235 `" ) && sleep 0'"'"''
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/files/stat.py
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895408.21-181658923211972 `" && echo ansible-tmp-1479895408.21-181658923211972="` echo $HOME/.ansible/tmp/ansible-tmp-1479895408.21-181658923211972 `" ) && sleep 0'"'"''
<nginx1.oeni.vrt.be> PUT /tmp/tmpL3e7hi TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.21-225555537601235/stat.py
<nginx1.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx1.oeni.vrt.be]'
<nginx2.oeni.vrt.be> PUT /tmp/tmphxvz4H TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.21-181658923211972/stat.py
<nginx2.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx2.oeni.vrt.be]'
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.21-225555537601235/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.21-225555537601235/stat.py && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.21-181658923211972/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.21-181658923211972/stat.py && sleep 0'"'"''
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r -tt nginx1.oeni.vrt.be '/bin/sh -c '"'"'sudo -H -S -n -u root /bin/sh -c '"'"'"'"'"'"'"'"'echo BECOME-SUCCESS-ftkfrrgkhcnwqrtaxmnyuxwhheqibmnz; /usr/bin/python /home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.21-225555537601235/stat.py; rm -rf "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.21-225555537601235/" > /dev/null 2>&1'"'"'"'"'"'"'"'"' && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r -tt nginx2.oeni.vrt.be '/bin/sh -c '"'"'sudo -H -S -n -u root /bin/sh -c '"'"'"'"'"'"'"'"'echo BECOME-SUCCESS-vnlxdsczhudwujfowbsblnpxnhsbyqbo; /usr/bin/python /home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.21-181658923211972/stat.py; rm -rf "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.21-181658923211972/" > /dev/null 2>&1'"'"'"'"'"'"'"'"' && sleep 0'"'"''
<nginx1.oeni.vrt.be> PUT /data/projects/habitat-deploy/ansible/files/vrt_openresty-1.11.2.1_with_kafka TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.1-85237097349884/source
<nginx1.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx1.oeni.vrt.be]'
<nginx2.oeni.vrt.be> PUT /data/projects/habitat-deploy/ansible/files/vrt_openresty-1.11.2.1_with_kafka TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.1-166938303598731/source
<nginx2.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx2.oeni.vrt.be]'
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.1-85237097349884/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.1-85237097349884/source && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.1-166938303598731/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.1-166938303598731/source && sleep 0'"'"''
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/files/unarchive.py
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895409.39-269418840383217 `" && echo ansible-tmp-1479895409.39-269418840383217="` echo $HOME/.ansible/tmp/ansible-tmp-1479895409.39-269418840383217 `" ) && sleep 0'"'"''
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/files/unarchive.py
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895409.39-133345589761925 `" && echo ansible-tmp-1479895409.39-133345589761925="` echo $HOME/.ansible/tmp/ansible-tmp-1479895409.39-133345589761925 `" ) && sleep 0'"'"''
<nginx2.oeni.vrt.be> PUT /tmp/tmpgzX5UX TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895409.39-269418840383217/unarchive.py
<nginx2.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx2.oeni.vrt.be]'
<nginx1.oeni.vrt.be> PUT /tmp/tmpUu3_pT TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895409.39-133345589761925/unarchive.py
<nginx1.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx1.oeni.vrt.be]'
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895409.39-133345589761925/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895409.39-133345589761925/unarchive.py && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895409.39-269418840383217/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895409.39-269418840383217/unarchive.py && sleep 0'"'"''
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r -tt nginx1.oeni.vrt.be '/bin/sh -c '"'"'sudo -H -S -n -u root /bin/sh -c '"'"'"'"'"'"'"'"'echo BECOME-SUCCESS-bvisjjlffxpznsbfswpqkrmymaskelky; /usr/bin/python /home/ubuntu/.ansible/tmp/ansible-tmp-1479895409.39-133345589761925/unarchive.py; rm -rf "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895409.39-133345589761925/" > /dev/null 2>&1'"'"'"'"'"'"'"'"' && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r -tt nginx2.oeni.vrt.be '/bin/sh -c '"'"'sudo -H -S -n -u root /bin/sh -c '"'"'"'"'"'"'"'"'echo BECOME-SUCCESS-mjebgvvuwsnnenslafxvyshkebvbppzd; /usr/bin/python /home/ubuntu/.ansible/tmp/ansible-tmp-1479895409.39-269418840383217/unarchive.py; rm -rf "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895409.39-269418840383217/" > /dev/null 2>&1'"'"'"'"'"'"'"'"' && sleep 0'"'"''
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'rm -f -r /home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.1-85237097349884/ > /dev/null 2>&1 && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'rm -f -r /home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.1-166938303598731/ > /dev/null 2>&1 && sleep 0'"'"''
ok: [nginx1.oeni.vrt.be] => {
    "changed": false, 
    "dest": "/data/programs/", 
    "gid": 0, 
    "group": "root", 
    "handler": "TgzArchive", 
    "invocation": {
        "module_args": {
            "backup": null, 
            "content": null, 
            "copy": true, 
            "creates": null, 
            "delimiter": null, 
            "dest": "/data/programs/", 
            "directory_mode": null, 
            "exclude": [], 
            "extra_opts": [], 
            "follow": false, 
            "force": "False", 
            "group": null, 
            "keep_newer": false, 
            "list_files": false, 
            "mode": null, 
            "original_basename": "vrt_openresty-1.11.2.1_with_kafka", 
            "owner": null, 
            "regexp": null, 
            "remote_src": false, 
            "selevel": null, 
            "serole": null, 
            "setype": null, 
            "seuser": null, 
            "src": "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.1-85237097349884/source", 
            "unsafe_writes": null, 
            "validate_certs": true
        }
    }, 
    "mode": "0755", 
    "owner": "root", 
    "size": 4096, 
    "src": "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.1-85237097349884/source", 
    "state": "directory", 
    "uid": 0
}
ok: [nginx2.oeni.vrt.be] => {
    "changed": false, 
    "dest": "/data/programs/", 
    "gid": 0, 
    "group": "root", 
    "handler": "TgzArchive", 
    "invocation": {
        "module_args": {
            "backup": null, 
            "content": null, 
            "copy": true, 
            "creates": null, 
            "delimiter": null, 
            "dest": "/data/programs/", 
            "directory_mode": null, 
            "exclude": [], 
            "extra_opts": [], 
            "follow": false, 
            "force": "False", 
            "group": null, 
            "keep_newer": false, 
            "list_files": false, 
            "mode": null, 
            "original_basename": "vrt_openresty-1.11.2.1_with_kafka", 
            "owner": null, 
            "regexp": null, 
            "remote_src": false, 
            "selevel": null, 
            "serole": null, 
            "setype": null, 
            "seuser": null, 
            "src": "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.1-166938303598731/source", 
            "unsafe_writes": null, 
            "validate_certs": true
        }
    }, 
    "mode": "0755", 
    "owner": "root", 
    "size": 4096, 
    "src": "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895408.1-166938303598731/source", 
    "state": "directory", 
    "uid": 0
}

TASK [openresty : create directory for logs] ***********************************
task path: /data/projects/habitat-deploy/ansible/roles/openresty/tasks/main.yml:28
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/files/file.py
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/files/file.py
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895410.13-53764328283312 `" && echo ansible-tmp-1479895410.13-53764328283312="` echo $HOME/.ansible/tmp/ansible-tmp-1479895410.13-53764328283312 `" ) && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895410.13-111850644862985 `" && echo ansible-tmp-1479895410.13-111850644862985="` echo $HOME/.ansible/tmp/ansible-tmp-1479895410.13-111850644862985 `" ) && sleep 0'"'"''
<nginx1.oeni.vrt.be> PUT /tmp/tmpQcm4ph TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.13-53764328283312/file.py
<nginx1.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx1.oeni.vrt.be]'
<nginx2.oeni.vrt.be> PUT /tmp/tmpnG46Wi TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.13-111850644862985/file.py
<nginx2.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx2.oeni.vrt.be]'
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.13-53764328283312/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.13-53764328283312/file.py && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.13-111850644862985/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.13-111850644862985/file.py && sleep 0'"'"''
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r -tt nginx1.oeni.vrt.be '/bin/sh -c '"'"'sudo -H -S -n -u root /bin/sh -c '"'"'"'"'"'"'"'"'echo BECOME-SUCCESS-vsqdcipqhoqfhjgvtvktwxskmnboaaju; /usr/bin/python /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.13-53764328283312/file.py; rm -rf "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.13-53764328283312/" > /dev/null 2>&1'"'"'"'"'"'"'"'"' && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r -tt nginx2.oeni.vrt.be '/bin/sh -c '"'"'sudo -H -S -n -u root /bin/sh -c '"'"'"'"'"'"'"'"'echo BECOME-SUCCESS-obelutaestoonywjlrvixnfhdiupuuuw; /usr/bin/python /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.13-111850644862985/file.py; rm -rf "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.13-111850644862985/" > /dev/null 2>&1'"'"'"'"'"'"'"'"' && sleep 0'"'"''
ok: [nginx1.oeni.vrt.be] => {
    "changed": false, 
    "diff": {
        "after": {
            "path": "/data/www/logs"
        }, 
        "before": {
            "path": "/data/www/logs"
        }
    }, 
    "gid": 65534, 
    "group": "nogroup", 
    "invocation": {
        "module_args": {
            "backup": null, 
            "content": null, 
            "delimiter": null, 
            "diff_peek": null, 
            "directory_mode": null, 
            "follow": false, 
            "force": false, 
            "group": "nogroup", 
            "mode": null, 
            "original_basename": null, 
            "owner": "nobody", 
            "path": "/data/www/logs", 
            "recurse": true, 
            "regexp": null, 
            "remote_src": null, 
            "selevel": null, 
            "serole": null, 
            "setype": null, 
            "seuser": null, 
            "src": null, 
            "state": "directory", 
            "unsafe_writes": null, 
            "validate": null
        }, 
        "module_name": "file"
    }, 
    "mode": "0755", 
    "owner": "nobody", 
    "path": "/data/www/logs", 
    "size": 4096, 
    "state": "directory", 
    "uid": 65534
}
ok: [nginx2.oeni.vrt.be] => {
    "changed": false, 
    "diff": {
        "after": {
            "path": "/data/www/logs"
        }, 
        "before": {
            "path": "/data/www/logs"
        }
    }, 
    "gid": 65534, 
    "group": "nogroup", 
    "invocation": {
        "module_args": {
            "backup": null, 
            "content": null, 
            "delimiter": null, 
            "diff_peek": null, 
            "directory_mode": null, 
            "follow": false, 
            "force": false, 
            "group": "nogroup", 
            "mode": null, 
            "original_basename": null, 
            "owner": "nobody", 
            "path": "/data/www/logs", 
            "recurse": true, 
            "regexp": null, 
            "remote_src": null, 
            "selevel": null, 
            "serole": null, 
            "setype": null, 
            "seuser": null, 
            "src": null, 
            "state": "directory", 
            "unsafe_writes": null, 
            "validate": null
        }, 
        "module_name": "file"
    }, 
    "mode": "0755", 
    "owner": "nobody", 
    "path": "/data/www/logs", 
    "size": 4096, 
    "state": "directory", 
    "uid": 65534
}

TASK [openresty : create directory for nginx conf] *****************************
task path: /data/projects/habitat-deploy/ansible/roles/openresty/tasks/main.yml:36
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/files/file.py
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895410.31-7348865312508 `" && echo ansible-tmp-1479895410.31-7348865312508="` echo $HOME/.ansible/tmp/ansible-tmp-1479895410.31-7348865312508 `" ) && sleep 0'"'"''
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/files/file.py
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895410.31-148893839336798 `" && echo ansible-tmp-1479895410.31-148893839336798="` echo $HOME/.ansible/tmp/ansible-tmp-1479895410.31-148893839336798 `" ) && sleep 0'"'"''
<nginx1.oeni.vrt.be> PUT /tmp/tmpL_xobP TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.31-7348865312508/file.py
<nginx1.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx1.oeni.vrt.be]'
<nginx2.oeni.vrt.be> PUT /tmp/tmpaYvfsv TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.31-148893839336798/file.py
<nginx2.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx2.oeni.vrt.be]'
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.31-7348865312508/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.31-7348865312508/file.py && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.31-148893839336798/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.31-148893839336798/file.py && sleep 0'"'"''
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r -tt nginx1.oeni.vrt.be '/bin/sh -c '"'"'sudo -H -S -n -u root /bin/sh -c '"'"'"'"'"'"'"'"'echo BECOME-SUCCESS-obdsrlrhlxocatnwnfxcwmfrbdlkrxrf; /usr/bin/python /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.31-7348865312508/file.py; rm -rf "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.31-7348865312508/" > /dev/null 2>&1'"'"'"'"'"'"'"'"' && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r -tt nginx2.oeni.vrt.be '/bin/sh -c '"'"'sudo -H -S -n -u root /bin/sh -c '"'"'"'"'"'"'"'"'echo BECOME-SUCCESS-ykyacnprhrylrydhtyugrgstvcfjidhm; /usr/bin/python /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.31-148893839336798/file.py; rm -rf "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.31-148893839336798/" > /dev/null 2>&1'"'"'"'"'"'"'"'"' && sleep 0'"'"''
changed: [nginx1.oeni.vrt.be] => {
    "changed": true, 
    "diff": {
        "after": {
            "group": 1000, 
            "owner": 1000, 
            "path": "/data/programs/data_nginx_conf", 
            "state": "directory"
        }, 
        "before": {
            "group": 0, 
            "owner": 0, 
            "path": "/data/programs/data_nginx_conf", 
            "state": "absent"
        }
    }, 
    "gid": 1000, 
    "group": "ubuntu", 
    "invocation": {
        "module_args": {
            "backup": null, 
            "content": null, 
            "delimiter": null, 
            "diff_peek": null, 
            "directory_mode": null, 
            "follow": false, 
            "force": false, 
            "group": "ubuntu", 
            "mode": null, 
            "original_basename": null, 
            "owner": "ubuntu", 
            "path": "/data/programs/data_nginx_conf", 
            "recurse": false, 
            "regexp": null, 
            "remote_src": null, 
            "selevel": null, 
            "serole": null, 
            "setype": null, 
            "seuser": null, 
            "src": null, 
            "state": "directory", 
            "unsafe_writes": null, 
            "validate": null
        }, 
        "module_name": "file"
    }, 
    "mode": "0755", 
    "owner": "ubuntu", 
    "path": "/data/programs/data_nginx_conf", 
    "size": 4096, 
    "state": "directory", 
    "uid": 1000
}
changed: [nginx2.oeni.vrt.be] => {
    "changed": true, 
    "diff": {
        "after": {
            "group": 1000, 
            "owner": 1000, 
            "path": "/data/programs/data_nginx_conf", 
            "state": "directory"
        }, 
        "before": {
            "group": 0, 
            "owner": 0, 
            "path": "/data/programs/data_nginx_conf", 
            "state": "absent"
        }
    }, 
    "gid": 1000, 
    "group": "ubuntu", 
    "invocation": {
        "module_args": {
            "backup": null, 
            "content": null, 
            "delimiter": null, 
            "diff_peek": null, 
            "directory_mode": null, 
            "follow": false, 
            "force": false, 
            "group": "ubuntu", 
            "mode": null, 
            "original_basename": null, 
            "owner": "ubuntu", 
            "path": "/data/programs/data_nginx_conf", 
            "recurse": false, 
            "regexp": null, 
            "remote_src": null, 
            "selevel": null, 
            "serole": null, 
            "setype": null, 
            "seuser": null, 
            "src": null, 
            "state": "directory", 
            "unsafe_writes": null, 
            "validate": null
        }, 
        "module_name": "file"
    }, 
    "mode": "0755", 
    "owner": "ubuntu", 
    "path": "/data/programs/data_nginx_conf", 
    "size": 4096, 
    "state": "directory", 
    "uid": 1000
}

TASK [openresty : git clone our openresty] *************************************
task path: /data/projects/habitat-deploy/ansible/roles/openresty/tasks/main.yml:44
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/source_control/git.py
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895410.59-116865482469959 `" && echo ansible-tmp-1479895410.59-116865482469959="` echo $HOME/.ansible/tmp/ansible-tmp-1479895410.59-116865482469959 `" ) && sleep 0'"'"''
Using module file /usr/lib/python2.7/dist-packages/ansible/modules/core/source_control/git.py
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo $HOME/.ansible/tmp/ansible-tmp-1479895410.59-78168056486094 `" && echo ansible-tmp-1479895410.59-78168056486094="` echo $HOME/.ansible/tmp/ansible-tmp-1479895410.59-78168056486094 `" ) && sleep 0'"'"''
<nginx2.oeni.vrt.be> PUT /tmp/tmp41HrR9 TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.59-116865482469959/git.py
<nginx2.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx2.oeni.vrt.be]'
<nginx1.oeni.vrt.be> PUT /tmp/tmpjsYG1j TO /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.59-78168056486094/git.py
<nginx1.oeni.vrt.be> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r '[nginx1.oeni.vrt.be]'
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx1.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.59-78168056486094/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.59-78168056486094/git.py && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r nginx2.oeni.vrt.be '/bin/sh -c '"'"'chmod u+x /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.59-116865482469959/ /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.59-116865482469959/git.py && sleep 0'"'"''
<nginx1.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx1.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r -tt nginx1.oeni.vrt.be '/bin/sh -c '"'"'sudo -H -S -n -u root /bin/sh -c '"'"'"'"'"'"'"'"'echo BECOME-SUCCESS-mhehkaanqhscaclycqkmcfagifmuoegg; /usr/bin/python /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.59-78168056486094/git.py; rm -rf "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.59-78168056486094/" > /dev/null 2>&1'"'"'"'"'"'"'"'"' && sleep 0'"'"''
<nginx2.oeni.vrt.be> ESTABLISH SSH CONNECTION FOR USER: ubuntu
<nginx2.oeni.vrt.be> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o Port=22 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o User=ubuntu -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r -tt nginx2.oeni.vrt.be '/bin/sh -c '"'"'sudo -H -S -n -u root /bin/sh -c '"'"'"'"'"'"'"'"'echo BECOME-SUCCESS-gdrgllikrljuydpmuawnewpiedylkigl; /usr/bin/python /home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.59-116865482469959/git.py; rm -rf "/home/ubuntu/.ansible/tmp/ansible-tmp-1479895410.59-116865482469959/" > /dev/null 2>&1'"'"'"'"'"'"'"'"' && sleep 0'"'"''
fatal: [nginx2.oeni.vrt.be]: FAILED! => {
    "changed": false, 
    "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", 
    "failed": true, 
    "invocation": {
        "module_args": {
            "accept_hostkey": true, 
            "bare": false, 
            "clone": true, 
            "depth": null, 
            "dest": "/data/programs/data_nginx_conf", 
            "executable": null, 
            "force": false, 
            "key_file": null, 
            "recursive": true, 
            "reference": null, 
            "refspec": null, 
            "remote": "origin", 
            "repo": "git@gitlab.com:vrtoeni/data_nginx_conf.git", 
            "ssh_opts": null, 
            "track_submodules": false, 
            "umask": null, 
            "update": true, 
            "verify_commit": false, 
            "version": "HEAD"
        }, 
        "module_name": "git"
    }, 
    "msg": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", 
    "rc": 128, 
    "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", 
    "stdout": "", 
    "stdout_lines": []
}
fatal: [nginx1.oeni.vrt.be]: FAILED! => {
    "changed": false, 
    "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", 
    "failed": true, 
    "invocation": {
        "module_args": {
            "accept_hostkey": true, 
            "bare": false, 
            "clone": true, 
            "depth": null, 
            "dest": "/data/programs/data_nginx_conf", 
            "executable": null, 
            "force": false, 
            "key_file": null, 
            "recursive": true, 
            "reference": null, 
            "refspec": null, 
            "remote": "origin", 
            "repo": "git@gitlab.com:vrtoeni/data_nginx_conf.git", 
            "ssh_opts": null, 
            "track_submodules": false, 
            "umask": null, 
            "update": true, 
            "verify_commit": false, 
            "version": "HEAD"
        }, 
        "module_name": "git"
    }, 
    "msg": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", 
    "rc": 128, 
    "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", 
    "stdout": "", 
    "stdout_lines": []
}
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=7    changed=1    unreachable=0    failed=1   
nginx2.oeni.vrt.be         : ok=7    changed=1    unreachable=0    failed=1   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git pull
Already up-to-date.
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ cat ~/.ssh/
authorized_keys  config           id_rsa           id_rsa.pub       known_hosts      known_hosts.old  
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ cat ~/.ssh/id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAw+QrrXWXVJninWtop/UhrJeCbQv341+Tl69wBWc+P569Ib9e
/DYp51+9+KWVOOjxqTc4P0RtclqLEHqBIY8+ymM5RZ7FV1KUuNRRZ2IdYPlbWQtg
g4CJYzW0BjFwya3Q5hmxTVmYnHY9TLSxJd3/PC+mMTn+2mt+8MZkoVs/ZHPAY2YG
6KfrWU2aC/gx2AM+P2eiZ9EIGPjpoYouZxoiKzACK/rHe0YQZ3yzw/f7Jh8gpkCz
Znjs7HvhNEcpkKg+32urnwl5K4PzWo0KkNznq1YwbtrSeGsUilNIkPZ2SYxEdVkd
soHqBRfomO+4a2Hb/sMFObY1rhjYB/4DEsKLhwIDAQABAoIBAQCrJ3gWJZEkZRQA
MPGPFnnmn7Zgar2a105QkQOSZQOZeKuNifSG7xgrxZZpYtt/juBe1hV6CeKKsJui
uTaMSOk20f0fXDrWMhwpZbD+YFaE/ToYEf2wyCTCHxD8/EOsowbLlRU6HRdfVVv3
4kSJbm7sekF970tCMfwGiYExDlXUAFnia11g/y5hSAQE1pVNhvtJyyoYUoTtxe36
8STQDLedxfCmXy9Bimcvz01Vcvs2LmQwA+l1KBiAY/RAsvCCDDSNUe0jLj0SLb2y
QqnBTsnCmiXNmjkC86EC2+7hPpdJ3Tpv52m9hv3Rj0lrQF00fKeuEEQScaTmlPy1
90ickL8BAoGBAPUhxLgtLzR/5ptkKl30GZ5qXCHdN5BRzDeL3RHlZ18WxCnsGoSL
OkzCDbvxWyf65NZDQXNWxENJt/VZ4xrV52Vc/MgGzTEfxaAQNVVJHRZFnYRZpWEx
XsMJPJdMTYN3vIOULS5kqEcql7uxY7N7mK5/6HbePEdhBdR7N1dgJiwHAoGBAMyT
hjl/wxexVEPxpRJXf450k8+/ZFPM8CLIuZlqC62NBsEqZQ//xWi+79v9J6gkPd64
WjE313k1+xePjdKKLglIGwP+Z2xQtKojqhvLe2/7dx7CRYn3/3Az598TJOuTLatV
m9JPvzeGrGwuYMxmb5Zk5rdHit54F6c4VRoZZ8SBAoGBAIOfjDew22X/P1403KLy
TUdIqQvt8sXlhhhVW3EekvD2EoLIKjz9XWKV2DYQlPfUukdqeZxq/Jt82/A8QbvJ
G6TL11e4fzlfbAhUa67NwXaSDtBgKnMTxWRIc2ZyLDTpeCnWyKPenJUKA8tepsBb
H1Kjj7kz/338VNsRBlg+YoDFAoGAYYEexGEEl1JJm2idCLTzcu5VVPsf0mEnQyzw
aRKGJl3FDmQqbwm1CUuX/v4V3KoJYxHyyuqWpIr59izRp7t8XagkWC71FEcTFNSS
y1ScrK7qA5sMkcnF0bCrn0L8odswNS1Ea2Te+pQRsi4YrNNV9BR7cneC1K3geC79
QMdDEgECgYBiiCRsni3adLvvDm12pPBTaOSEcNLYEkcSZ9uMJyV3zHCJAn/tIfIK
hZhKdI+XfLYtpp1yqH1uSN94x5D96nhZFX8GiMXrlAufAjLS+V4whouB9lGYCfSm
H5KwDXBdEACxSPluWkzQMqS3H7oNu6K4IqyXeVK+T/x8zOu/szjwkA==
-----END RSA PRIVATE KEY-----
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ openssl rsa -in id_rsa -modulus -noout
Error opening Private Key id_rsa
140006498903712:error:02001002:system library:fopen:No such file or directory:bss_file.c:398:fopen('id_rsa','r')
140006498903712:error:20074002:BIO routines:FILE_CTRL:system lib:bss_file.c:400:
unable to load Private Key
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ openssl rsa -in ~/.ssh/id_rsa -modulus -noout
Modulus=C3E42BAD75975499E29D6B68A7F521AC97826D0BF7E35F9397AF7005673E3F9EBD21BF5EFC3629E75FBDF8A59538E8F1A937383F446D725A8B107A81218F3ECA6339459EC5575294B8D45167621D60F95B590B608380896335B4063170C9ADD0E619B14D59989C763D4CB4B125DDFF3C2FA63139FEDA6B7EF0C664A15B3F6473C0636606E8A7EB594D9A0BF831D8033E3F67A267D10818F8E9A18A2E671A222B30022BFAC77B4610677CB3C3F7FB261F20A640B36678ECEC7BE134472990A83EDF6BAB9F09792B83F35A8D0A90DCE7AB56306EDAD2786B148A534890F676498C4475591DB281EA0517E898EFB86B61DBFEC30539B635AE18D807FE0312C28B87
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ cat ~/.ssh/id_rsa.pub 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDD5CutdZdUmeKda2in9SGsl4JtC/fjX5OXr3AFZz4/nr0hv178NinnX734pZU46PGpNzg/RG1yWosQeoEhjz7KYzlFnsVXUpS41FFnYh1g+VtZC2CDgIljNbQGMXDJrdDmGbFNWZicdj1MtLEl3f88L6YxOf7aa37wxmShWz9kc8BjZgbop+tZTZoL+DHYAz4/Z6Jn0QgY+Omhii5nGiIrMAIr+sd7RhBnfLPD9/smHyCmQLNmeOzse+E0RymQqD7fa6ufCXkrg/NajQqQ3OerVjBu2tJ4axSKU0iQ9nZJjER1WR2ygeoFF+iY77hrYdv+wwU5tjWuGNgH/gMSwouH gitlab+janitor@innovatie.vrt.be
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ openssl rsa -in ~/.ssh/id_rsa  -noout
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ openssl rsa -in ~/.ssh/id_rsa -modulus -noout
Modulus=C3E42BAD75975499E29D6B68A7F521AC97826D0BF7E35F9397AF7005673E3F9EBD21BF5EFC3629E75FBDF8A59538E8F1A937383F446D725A8B107A81218F3ECA6339459EC5575294B8D45167621D60F95B590B608380896335B4063170C9ADD0E619B14D59989C763D4CB4B125DDFF3C2FA63139FEDA6B7EF0C664A15B3F6473C0636606E8A7EB594D9A0BF831D8033E3F67A267D10818F8E9A18A2E671A222B30022BFAC77B4610677CB3C3F7FB261F20A640B36678ECEC7BE134472990A83EDF6BAB9F09792B83F35A8D0A90DCE7AB56306EDAD2786B148A534890F676498C4475591DB281EA0517E898EFB86B61DBFEC30539B635AE18D807FE0312C28B87
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ cp ~/.ssh/id_rsa.pub id_rsa_janitor.pub
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ll ~/.ssh/
total 44
drwx------ 2 ubuntu ubuntu 4096 Nov 15 09:33 ./
drwxr-xr-x 8 ubuntu ubuntu 4096 Nov 23 10:02 ../
-rw------- 1 ubuntu ubuntu 1549 Nov 14 12:06 authorized_keys
-rw-rw-r-- 1 ubuntu ubuntu   32 Oct 24 08:05 config
-rw------- 1 ubuntu ubuntu 1679 Oct  7 07:35 id_rsa
-rw-r--r-- 1 ubuntu ubuntu  413 Oct  7 07:35 id_rsa.pub
-rw------- 1 ubuntu ubuntu 9324 Nov 15 08:09 known_hosts
-rw------- 1 ubuntu ubuntu 7548 Oct 21 12:45 known_hosts.old
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ cp ~/.ssh/id_rsa id_rsa_janitor
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ openssl rsa -pubin ~/.ssh/id_rsa
id_rsa      id_rsa.pub  
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ openssl rsa -pubin ~/.ssh/
authorized_keys  config           id_rsa           id_rsa.pub       known_hosts      known_hosts.old  
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ openssl rsa -pubin id_rsa_janitor.pub -modulus -noout
unknown option id_rsa_janitor.pub
rsa [options] <infile >outfile
where options are
 -inform arg     input format - one of DER NET PEM
 -outform arg    output format - one of DER NET PEM
 -in arg         input file
 -sgckey         Use IIS SGC key format
 -passin arg     input file pass phrase source
 -out arg        output file
 -passout arg    output file pass phrase source
 -des            encrypt PEM output with cbc des
 -des3           encrypt PEM output with ede cbc des using 168 bit key
 -seed           encrypt PEM output with cbc seed
 -aes128, -aes192, -aes256
                 encrypt PEM output with cbc aes
 -camellia128, -camellia192, -camellia256
                 encrypt PEM output with cbc camellia
 -text           print the key in text
 -noout          don't print key out
 -modulus        print the RSA key modulus
 -check          verify key consistency
 -pubin          expect a public key in input file
 -pubout         output a public key
 -engine e       use engine e, possibly a hardware device.
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ openssl rsa -pubin -in id_rsa_janitor.pub -modulus -noout
unable to load Public Key
139819279074976:error:0906D06C:PEM routines:PEM_read_bio:no start line:pem_lib.c:703:Expecting: PUBLIC KEY
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ll
total 80
drwxrwsr-x  8 ubuntu ubuntu 4096 Nov 23 10:26 ./
drwxrwsr-x  6 ubuntu ubuntu 4096 Nov 15 08:08 ../
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov  8 14:56 ansible-elasticsearch/
-rw-rw-r--  1 ubuntu ubuntu  206 Nov  8 14:56 apps.yml
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov 15 08:05 etc/
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov 22 17:05 files/
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov 17 12:27 group_vars/
-rw-rw-r--  1 ubuntu ubuntu  122 Nov  8 14:56 hadoop.yml
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov  8 14:56 host_vars/
-rw-rw-r--  1 ubuntu ubuntu   24 Nov 17 09:12 hubot.retry
-rw-rw-r--  1 ubuntu ubuntu   99 Nov 15 08:05 hubot.yml
-rw-------  1 ubuntu ubuntu 1679 Nov 23 10:26 id_rsa_janitor
-rw-r--r--  1 ubuntu ubuntu  413 Nov 23 10:24 id_rsa_janitor.pub
-rw-rw-r--  1 ubuntu ubuntu  156 Nov  8 14:56 kafka.yml
-rw-rw-r--  1 ubuntu ubuntu   38 Nov 23 10:03 openresty.retry
-rw-rw-r--  1 ubuntu ubuntu   78 Nov 23 10:02 openresty.yml
-rw-rw-r--  1 ubuntu ubuntu  389 Nov  8 14:56 pio.yml
-rw-rw-r--  1 ubuntu ubuntu  932 Nov  8 14:56 pio_elasticsearch.yml
drwxrwsr-x 13 ubuntu ubuntu 4096 Nov 15 08:05 roles/
-rw-rw-r--  1 ubuntu ubuntu  118 Nov  8 14:56 zookeeper.yml
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ll ~/.ssh/
total 44
drwx------ 2 ubuntu ubuntu 4096 Nov 15 09:33 ./
drwxr-xr-x 8 ubuntu ubuntu 4096 Nov 23 10:02 ../
-rw------- 1 ubuntu ubuntu 1549 Nov 14 12:06 authorized_keys
-rw-rw-r-- 1 ubuntu ubuntu   32 Oct 24 08:05 config
-rw------- 1 ubuntu ubuntu 1679 Oct  7 07:35 id_rsa
-rw-r--r-- 1 ubuntu ubuntu  413 Oct  7 07:35 id_rsa.pub
-rw------- 1 ubuntu ubuntu 9324 Nov 15 08:09 known_hosts
-rw------- 1 ubuntu ubuntu 7548 Oct 21 12:45 known_hosts.old
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ cat ~/.ssh/id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAw+QrrXWXVJninWtop/UhrJeCbQv341+Tl69wBWc+P569Ib9e
/DYp51+9+KWVOOjxqTc4P0RtclqLEHqBIY8+ymM5RZ7FV1KUuNRRZ2IdYPlbWQtg
g4CJYzW0BjFwya3Q5hmxTVmYnHY9TLSxJd3/PC+mMTn+2mt+8MZkoVs/ZHPAY2YG
6KfrWU2aC/gx2AM+P2eiZ9EIGPjpoYouZxoiKzACK/rHe0YQZ3yzw/f7Jh8gpkCz
Znjs7HvhNEcpkKg+32urnwl5K4PzWo0KkNznq1YwbtrSeGsUilNIkPZ2SYxEdVkd
soHqBRfomO+4a2Hb/sMFObY1rhjYB/4DEsKLhwIDAQABAoIBAQCrJ3gWJZEkZRQA
MPGPFnnmn7Zgar2a105QkQOSZQOZeKuNifSG7xgrxZZpYtt/juBe1hV6CeKKsJui
uTaMSOk20f0fXDrWMhwpZbD+YFaE/ToYEf2wyCTCHxD8/EOsowbLlRU6HRdfVVv3
4kSJbm7sekF970tCMfwGiYExDlXUAFnia11g/y5hSAQE1pVNhvtJyyoYUoTtxe36
8STQDLedxfCmXy9Bimcvz01Vcvs2LmQwA+l1KBiAY/RAsvCCDDSNUe0jLj0SLb2y
QqnBTsnCmiXNmjkC86EC2+7hPpdJ3Tpv52m9hv3Rj0lrQF00fKeuEEQScaTmlPy1
90ickL8BAoGBAPUhxLgtLzR/5ptkKl30GZ5qXCHdN5BRzDeL3RHlZ18WxCnsGoSL
OkzCDbvxWyf65NZDQXNWxENJt/VZ4xrV52Vc/MgGzTEfxaAQNVVJHRZFnYRZpWEx
XsMJPJdMTYN3vIOULS5kqEcql7uxY7N7mK5/6HbePEdhBdR7N1dgJiwHAoGBAMyT
hjl/wxexVEPxpRJXf450k8+/ZFPM8CLIuZlqC62NBsEqZQ//xWi+79v9J6gkPd64
WjE313k1+xePjdKKLglIGwP+Z2xQtKojqhvLe2/7dx7CRYn3/3Az598TJOuTLatV
m9JPvzeGrGwuYMxmb5Zk5rdHit54F6c4VRoZZ8SBAoGBAIOfjDew22X/P1403KLy
TUdIqQvt8sXlhhhVW3EekvD2EoLIKjz9XWKV2DYQlPfUukdqeZxq/Jt82/A8QbvJ
G6TL11e4fzlfbAhUa67NwXaSDtBgKnMTxWRIc2ZyLDTpeCnWyKPenJUKA8tepsBb
H1Kjj7kz/338VNsRBlg+YoDFAoGAYYEexGEEl1JJm2idCLTzcu5VVPsf0mEnQyzw
aRKGJl3FDmQqbwm1CUuX/v4V3KoJYxHyyuqWpIr59izRp7t8XagkWC71FEcTFNSS
y1ScrK7qA5sMkcnF0bCrn0L8odswNS1Ea2Te+pQRsi4YrNNV9BR7cneC1K3geC79
QMdDEgECgYBiiCRsni3adLvvDm12pPBTaOSEcNLYEkcSZ9uMJyV3zHCJAn/tIfIK
hZhKdI+XfLYtpp1yqH1uSN94x5D96nhZFX8GiMXrlAufAjLS+V4whouB9lGYCfSm
H5KwDXBdEACxSPluWkzQMqS3H7oNu6K4IqyXeVK+T/x8zOu/szjwkA==
-----END RSA PRIVATE KEY-----
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ cat ~/.ssh/id_rsa.pub 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDD5CutdZdUmeKda2in9SGsl4JtC/fjX5OXr3AFZz4/nr0hv178NinnX734pZU46PGpNzg/RG1yWosQeoEhjz7KYzlFnsVXUpS41FFnYh1g+VtZC2CDgIljNbQGMXDJrdDmGbFNWZicdj1MtLEl3f88L6YxOf7aa37wxmShWz9kc8BjZgbop+tZTZoL+DHYAz4/Z6Jn0QgY+Omhii5nGiIrMAIr+sd7RhBnfLPD9/smHyCmQLNmeOzse+E0RymQqD7fa6ufCXkrg/NajQqQ3OerVjBu2tJ4axSKU0iQ9nZJjER1WR2ygeoFF+iY77hrYdv+wwU5tjWuGNgH/gMSwouH gitlab+janitor@innovatie.vrt.be
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ssh-keygen -y -f id_rsa_janitor
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDD5CutdZdUmeKda2in9SGsl4JtC/fjX5OXr3AFZz4/nr0hv178NinnX734pZU46PGpNzg/RG1yWosQeoEhjz7KYzlFnsVXUpS41FFnYh1g+VtZC2CDgIljNbQGMXDJrdDmGbFNWZicdj1MtLEl3f88L6YxOf7aa37wxmShWz9kc8BjZgbop+tZTZoL+DHYAz4/Z6Jn0QgY+Omhii5nGiIrMAIr+sd7RhBnfLPD9/smHyCmQLNmeOzse+E0RymQqD7fa6ufCXkrg/NajQqQ3OerVjBu2tJ4axSKU0iQ9nZJjER1WR2ygeoFF+iY77hrYdv+wwU5tjWuGNgH/gMSwouH
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ man ssh-keygen
man: can't set the locale; make sure $LC_* and $LANG are correct
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ man ssh-keygen
man: can't set the locale; make sure $LC_* and $LANG are correct
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git stadus
git: 'stadus' is not a git command. See 'git --help'.

Did you mean this?
	status
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   openresty.yml

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	../ansible-elasticsearch/
	hubot.retry
	id_rsa_janitor
	id_rsa_janitor.pub
	openresty.retry
	../apps.retry
	../elasticsearch.retry
	../openresty.retry
	../pio.retry
	../zookeeper.retry

no changes added to commit (use "git add" and/or "git commit -a")
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ mv ~/.ssh/id_rsa ~/.ssh/id_rsa_janitor
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ mv ~/.ssh/id_rsa.pub ~/.ssh/id_rsa_janitor.pub
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git stash
Saved working directory and index state WIP on master: caf39d9 moved nginx to its own repo
HEAD is now at caf39d9 moved nginx to its own repo
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git pull
remote: Counting objects: 14, done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 14 (delta 8), reused 0 (delta 0)
Unpacking objects: 100% (14/14), done.
From gitlab.com:vrtoeni/habitat-deploy
   caf39d9..9083eb8  master     -> origin/master
Updating caf39d9..9083eb8
Fast-forward
 ansible/roles/openresty/tasks/main.yml | 13 ++-----------
 1 file changed, 2 insertions(+), 11 deletions(-)
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -i etc/hosts openresty.yml 

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
ok: [nginx2.oeni.vrt.be]
ok: [nginx1.oeni.vrt.be]

TASK [common : install_language-pack-en-base] **********************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : install git] ****************************************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : Allow limits to be read from /etc/security/limits.conf] *********
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Set nofile limits] **********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nofile 65532)

TASK [common : Set nproc limits] ***********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nproc 65532)

TASK [common : Set swappiness to 1] ********************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Include partitioning.yml] ***************************************
included: /data/projects/habitat-deploy/ansible/roles/common/tasks/partitioning.yml for nginx1.oeni.vrt.be, nginx2.oeni.vrt.be

TASK [common : Create the filesystem on disk sdb] ******************************
skipping: [nginx2.oeni.vrt.be]
skipping: [nginx1.oeni.vrt.be]

TASK [common : Disable periodic fsck on sdb] ***********************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Mount datanode disks under /data/{0..n}] ************************
skipping: [nginx1.oeni.vrt.be] => (item=(0, u'sdb')) 
skipping: [nginx2.oeni.vrt.be] => (item=(0, u'sdb')) 

TASK [common-ssh : add ssh keys for the different accounts] ********************
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})

TASK [openresty : info about extra vars] ***************************************
ok: [nginx1.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}
ok: [nginx2.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}

TASK [openresty : install prerequisites] ***************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for openresty] ******************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : unpack openresty directly] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for logs] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for nginx conf repo] ************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [openresty : git clone our openresty] *************************************
fatal: [nginx1.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "Cloning into '/data/programs/data_nginx_conf'...\nWarning: Identity file /home/ubuntu/.ssh/id_rsa_janitor not accessible: No such file or directory.\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nWarning: Identity file /home/ubuntu/.ssh/id_rsa_janitor not accessible: No such file or directory.\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stdout": "", "stdout_lines": []}
fatal: [nginx2.oeni.vrt.be]: FAILED! => {"changed": false, "cmd": "/usr/bin/git clone --origin origin '' /data/programs/data_nginx_conf", "failed": true, "msg": "Cloning into '/data/programs/data_nginx_conf'...\nWarning: Identity file /home/ubuntu/.ssh/id_rsa_janitor not accessible: No such file or directory.\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.", "rc": 128, "stderr": "Cloning into '/data/programs/data_nginx_conf'...\nWarning: Identity file /home/ubuntu/.ssh/id_rsa_janitor not accessible: No such file or directory.\nPermission denied (publickey).\r\nfatal: Could not read from remote repository.\n\nPlease make sure you have the correct access rights\nand the repository exists.\n", "stdout": "", "stdout_lines": []}

RUNNING HANDLER [common : rebuild locales] *************************************
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=15   changed=3    unreachable=0    failed=1   
nginx2.oeni.vrt.be         : ok=15   changed=3    unreachable=0    failed=1   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ll /home/ubuntu/.ssh/id_rsa_janitor
-rw------- 1 ubuntu ubuntu 1679 Oct  7 07:35 /home/ubuntu/.ssh/id_rsa_janitor
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ll ~
total 104
drwxr-xr-x   8 ubuntu ubuntu  4096 Nov 23 10:02 ./
drwxr-xr-x   3 root   root    4096 Oct  6 11:25 ../
drwxrwxr-x   4 ubuntu ubuntu  4096 Oct  7 13:03 .ansible/
-rw-------   1 ubuntu ubuntu 19323 Nov 17 13:31 .bash_history
-rw-r--r--   1 ubuntu ubuntu   220 Apr  9  2014 .bash_logout
-rw-r--r--   1 ubuntu ubuntu  3637 Apr  9  2014 .bashrc
drwx------   2 ubuntu ubuntu  4096 Oct  6 11:29 .cache/
-rw-rw-r--   1 ubuntu ubuntu     0 Oct  6 11:29 .cloud-locale-test.skip
-rw-rw-r--   1 ubuntu ubuntu    76 Nov 15 12:20 .gitconfig
-rw-------   1 ubuntu ubuntu    47 Nov 23 10:33 .lesshst
drwxrwxr-x 316 ubuntu ubuntu 20480 Nov 17 08:03 .npm/
-rw-r--r--   1 ubuntu ubuntu   675 Apr  9  2014 .profile
drwx------   2 ubuntu ubuntu  4096 Nov 23 10:38 .ssh/
drwxr-xr-x   2 ubuntu ubuntu  4096 Oct 10 18:56 .vim/
-rw-------   1 ubuntu ubuntu  8339 Nov 23 10:02 .viminfo
drwxrwxr-x   4 ubuntu ubuntu  4096 Nov 15 13:32 tmp/
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ packet_write_wait: Connection to 54.194.37.69: Broken pipe
paularmandsmbp.rto.be 01:37:40 (master) ~/dev_habitat/data_nginx$ ssh vrt_mastermind
Welcome to Ubuntu 14.04.5 LTS (GNU/Linux 3.13.0-92-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Wed Nov 23 10:46:14 UTC 2016

  System load:  0.0               Processes:           111
  Usage of /:   19.3% of 7.74GB   Users logged in:     1
  Memory usage: 30%               IP address for eth0: 172.18.0.34
  Swap usage:   0%

  Graph this data and manage this system at:
    https://landscape.canonical.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

19 packages can be updated.
17 updates are security updates.

New release '16.04.1 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


*** System restart required ***
Last login: Wed Nov 23 09:50:42 2016 from vpn.lab.vrt.be
ubuntu@mastermind:~$ cd /data/
logs/     programs/ projects/ 
ubuntu@mastermind:~$ cd /data/projects/
ubuntu@mastermind:/data/projects$ ll
total 12
drwxr-sr-x 3 ubuntu ubuntu 4096 Oct  7 07:38 ./
drwxr-xr-x 5 root   root   4096 Nov 17 09:08 ../
drwxrwsr-x 6 ubuntu ubuntu 4096 Nov 15 08:08 habitat-deploy/
ubuntu@mastermind:/data/projects$ cd habitat-deploy/
ubuntu@mastermind:/data/projects/habitat-deploy$ cd ansible
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git pull
remote: Counting objects: 9, done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 9 (delta 4), reused 5 (delta 0)
Unpacking objects: 100% (9/9), done.
From gitlab.com:vrtoeni/habitat-deploy
   9083eb8..c17836f  master     -> origin/master
Updating 9083eb8..c17836f
Fast-forward
 ansible/group_vars/vault                | 94 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 ansible/roles/common-ssh/tasks/main.yml | 18 ++++++++++++++++++
 2 files changed, 112 insertions(+)
 create mode 100644 ansible/group_vars/vault
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -i etc/hosts openresty.
ERROR! the playbook: openresty. could not be found
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -i etc/hosts openresty.yml 

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
ok: [nginx2.oeni.vrt.be]
ok: [nginx1.oeni.vrt.be]

TASK [common : install_language-pack-en-base] **********************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : install git] ****************************************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : Allow limits to be read from /etc/security/limits.conf] *********
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Set nofile limits] **********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nofile 65532)

TASK [common : Set nproc limits] ***********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nproc 65532)

TASK [common : Set swappiness to 1] ********************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Include partitioning.yml] ***************************************
included: /data/projects/habitat-deploy/ansible/roles/common/tasks/partitioning.yml for nginx2.oeni.vrt.be, nginx1.oeni.vrt.be

TASK [common : Create the filesystem on disk sdb] ******************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Disable periodic fsck on sdb] ***********************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Mount datanode disks under /data/{0..n}] ************************
skipping: [nginx1.oeni.vrt.be] => (item=(0, u'sdb')) 
skipping: [nginx2.oeni.vrt.be] => (item=(0, u'sdb')) 

TASK [common-ssh : Ensure .ssh directory exists.] ******************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common-ssh : add ssh keys for the different accounts] ********************
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})

TASK [common-ssh : load the vault vars] ****************************************
fatal: [nginx1.oeni.vrt.be]: FAILED! => {"failed": true, "msg": "Unable to find 'vault' in expected paths."}
fatal: [nginx2.oeni.vrt.be]: FAILED! => {"failed": true, "msg": "Unable to find 'vault' in expected paths."}

RUNNING HANDLER [common : rebuild locales] *************************************
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=10   changed=2    unreachable=0    failed=1   
nginx2.oeni.vrt.be         : ok=10   changed=2    unreachable=0    failed=1   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ vi openresty.yml 
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ vi roles/
common/           common-confluent/ common-ssh/       hubot/            kafka-streams/    pio/              
common-aws/       common-java/      elasticsearch/    kafka/            openresty/        zookeeper/        
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ vi roles/openresty/tasks/main.yml 
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ vi roles/common-ssh/tasks/main.yml 
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -i etc/hosts openresty.yml 

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : install_language-pack-en-base] **********************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : install git] ****************************************************
changed: [nginx2.oeni.vrt.be]
changed: [nginx1.oeni.vrt.be]

TASK [common : Allow limits to be read from /etc/security/limits.conf] *********
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Set nofile limits] **********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nofile 65532)

TASK [common : Set nproc limits] ***********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nproc 65532)

TASK [common : Set swappiness to 1] ********************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Include partitioning.yml] ***************************************
included: /data/projects/habitat-deploy/ansible/roles/common/tasks/partitioning.yml for nginx1.oeni.vrt.be, nginx2.oeni.vrt.be

TASK [common : Create the filesystem on disk sdb] ******************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Disable periodic fsck on sdb] ***********************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Mount datanode disks under /data/{0..n}] ************************
skipping: [nginx1.oeni.vrt.be] => (item=(0, u'sdb')) 
skipping: [nginx2.oeni.vrt.be] => (item=(0, u'sdb')) 

TASK [common-ssh : Ensure .ssh directory exists.] ******************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common-ssh : add ssh keys for the different accounts] ********************
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})

TASK [common-ssh : load the vault vars] ****************************************
fatal: [nginx1.oeni.vrt.be]: FAILED! => {"ansible_facts": {}, "changed": false, "failed": true, "message": "/data/projects/habitat-deploy/ansible/group_vars/vault does not have a valid extension: yaml, yml, json"}
fatal: [nginx2.oeni.vrt.be]: FAILED! => {"ansible_facts": {}, "changed": false, "failed": true, "message": "/data/projects/habitat-deploy/ansible/group_vars/vault does not have a valid extension: yaml, yml, json"}

RUNNING HANDLER [common : rebuild locales] *************************************
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=10   changed=2    unreachable=0    failed=1   
nginx2.oeni.vrt.be         : ok=10   changed=2    unreachable=0    failed=1   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git pull
remote: Counting objects: 8, done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 8 (delta 5), reused 0 (delta 0)
Unpacking objects: 100% (8/8), done.
From gitlab.com:vrtoeni/habitat-deploy
   c17836f..b75ad27  master     -> origin/master
Updating c17836f..b75ad27
error: Your local changes to the following files would be overwritten by merge:
	ansible/roles/common-ssh/tasks/main.yml
Please, commit your changes or stash them before you can merge.
Aborting
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -i etc/hosts openresty.yml 

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : install_language-pack-en-base] **********************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : install git] ****************************************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : Allow limits to be read from /etc/security/limits.conf] *********
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Set nofile limits] **********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nofile 65532)

TASK [common : Set nproc limits] ***********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nproc 65532)

TASK [common : Set swappiness to 1] ********************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Include partitioning.yml] ***************************************
included: /data/projects/habitat-deploy/ansible/roles/common/tasks/partitioning.yml for nginx1.oeni.vrt.be, nginx2.oeni.vrt.be

TASK [common : Create the filesystem on disk sdb] ******************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Disable periodic fsck on sdb] ***********************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Mount datanode disks under /data/{0..n}] ************************
skipping: [nginx1.oeni.vrt.be] => (item=(0, u'sdb')) 
skipping: [nginx2.oeni.vrt.be] => (item=(0, u'sdb')) 

TASK [common-ssh : Ensure .ssh directory exists.] ******************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common-ssh : add ssh keys for the different accounts] ********************
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})

TASK [common-ssh : load the vault vars] ****************************************
fatal: [nginx1.oeni.vrt.be]: FAILED! => {"ansible_facts": {}, "changed": false, "failed": true, "message": "/data/projects/habitat-deploy/ansible/group_vars/vault does not have a valid extension: yaml, yml, json"}
fatal: [nginx2.oeni.vrt.be]: FAILED! => {"ansible_facts": {}, "changed": false, "failed": true, "message": "/data/projects/habitat-deploy/ansible/group_vars/vault does not have a valid extension: yaml, yml, json"}

RUNNING HANDLER [common : rebuild locales] *************************************
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=10   changed=2    unreachable=0    failed=1   
nginx2.oeni.vrt.be         : ok=10   changed=2    unreachable=0    failed=1   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ll /data/projects/habitat-deploy/ansible/group_vars/vault*
-rw-rw-r-- 1 ubuntu ubuntu 7483 Nov 23 14:47 /data/projects/habitat-deploy/ansible/group_vars/vault
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ pit pull^C
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git pull
Updating c17836f..b75ad27
error: Your local changes to the following files would be overwritten by merge:
	ansible/roles/common-ssh/tasks/main.yml
Please, commit your changes or stash them before you can merge.
Aborting
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ vi ansible/roles/common-ssh/tasks/main.yml
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git stash
Saved working directory and index state WIP on master: c17836f using ansible vault for the private key
HEAD is now at c17836f using ansible vault for the private key
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git pull
Updating c17836f..b75ad27
Fast-forward
 ansible/group_vars/{vault => vault.yml} | 0
 ansible/roles/common-ssh/tasks/main.yml | 2 +-
 2 files changed, 1 insertion(+), 1 deletion(-)
 rename ansible/group_vars/{vault => vault.yml} (100%)
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -i etc/hosts openresty.yml 

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : install_language-pack-en-base] **********************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : install git] ****************************************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : Allow limits to be read from /etc/security/limits.conf] *********
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Set nofile limits] **********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nofile 65532)

TASK [common : Set nproc limits] ***********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nproc 65532)

TASK [common : Set swappiness to 1] ********************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Include partitioning.yml] ***************************************
included: /data/projects/habitat-deploy/ansible/roles/common/tasks/partitioning.yml for nginx1.oeni.vrt.be, nginx2.oeni.vrt.be

TASK [common : Create the filesystem on disk sdb] ******************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Disable periodic fsck on sdb] ***********************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Mount datanode disks under /data/{0..n}] ************************
skipping: [nginx1.oeni.vrt.be] => (item=(0, u'sdb')) 
skipping: [nginx2.oeni.vrt.be] => (item=(0, u'sdb')) 

TASK [common-ssh : Ensure .ssh directory exists.] ******************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common-ssh : add ssh keys for the different accounts] ********************
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})

TASK [common-ssh : load the vault vars] ****************************************
fatal: [nginx1.oeni.vrt.be]: FAILED! => {"failed": true, "msg": "Decryption failed on /data/projects/habitat-deploy/ansible/group_vars/vault.yml"}
fatal: [nginx2.oeni.vrt.be]: FAILED! => {"failed": true, "msg": "Decryption failed on /data/projects/habitat-deploy/ansible/group_vars/vault.yml"}

RUNNING HANDLER [common : rebuild locales] *************************************
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=10   changed=2    unreachable=0    failed=1   
nginx2.oeni.vrt.be         : ok=10   changed=2    unreachable=0    failed=1   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -i etc/hosts openresty.yml  --ask-vault-pass
Vault password: 

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
ok: [nginx2.oeni.vrt.be]
ok: [nginx1.oeni.vrt.be]

TASK [common : install_language-pack-en-base] **********************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : install git] ****************************************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : Allow limits to be read from /etc/security/limits.conf] *********
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Set nofile limits] **********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nofile 65532)

TASK [common : Set nproc limits] ***********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nproc 65532)

TASK [common : Set swappiness to 1] ********************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Include partitioning.yml] ***************************************
included: /data/projects/habitat-deploy/ansible/roles/common/tasks/partitioning.yml for nginx1.oeni.vrt.be, nginx2.oeni.vrt.be

TASK [common : Create the filesystem on disk sdb] ******************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Disable periodic fsck on sdb] ***********************************
skipping: [nginx2.oeni.vrt.be]
skipping: [nginx1.oeni.vrt.be]

TASK [common : Mount datanode disks under /data/{0..n}] ************************
skipping: [nginx1.oeni.vrt.be] => (item=(0, u'sdb')) 
skipping: [nginx2.oeni.vrt.be] => (item=(0, u'sdb')) 

TASK [common-ssh : Ensure .ssh directory exists.] ******************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common-ssh : add ssh keys for the different accounts] ********************
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})

TASK [common-ssh : load the vault vars] ****************************************
fatal: [nginx2.oeni.vrt.be]: FAILED! => {"failed": true, "msg": "Syntax Error while loading YAML.\n\n\nThe error appears to have been in 'False': line 2, column 1, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\n(could not open file to display line)"}
fatal: [nginx1.oeni.vrt.be]: FAILED! => {"failed": true, "msg": "Syntax Error while loading YAML.\n\n\nThe error appears to have been in 'False': line 2, column 1, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\n(could not open file to display line)"}

RUNNING HANDLER [common : rebuild locales] *************************************
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=10   changed=2    unreachable=0    failed=1   
nginx2.oeni.vrt.be         : ok=10   changed=2    unreachable=0    failed=1   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-vault decrypt group_vars/vault.yml u
Vault password:  [ERROR]: User interrupted execution

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-vault decrypt group_vars/vault.yml 
Vault password: 
Decryption successful
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ll
total 80
drwxrwsr-x  8 ubuntu ubuntu 4096 Nov 23 14:48 ./
drwxrwsr-x  6 ubuntu ubuntu 4096 Nov 15 08:08 ../
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov  8 14:56 ansible-elasticsearch/
-rw-rw-r--  1 ubuntu ubuntu  206 Nov  8 14:56 apps.yml
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov 15 08:05 etc/
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov 22 17:05 files/
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov 23 15:13 group_vars/
-rw-rw-r--  1 ubuntu ubuntu  122 Nov  8 14:56 hadoop.yml
drwxrwsr-x  2 ubuntu ubuntu 4096 Nov  8 14:56 host_vars/
-rw-rw-r--  1 ubuntu ubuntu   24 Nov 17 09:12 hubot.retry
-rw-rw-r--  1 ubuntu ubuntu   99 Nov 15 08:05 hubot.yml
-rw-------  1 ubuntu ubuntu 1679 Nov 23 10:26 id_rsa_janitor
-rw-r--r--  1 ubuntu ubuntu  413 Nov 23 10:24 id_rsa_janitor.pub
-rw-rw-r--  1 ubuntu ubuntu  156 Nov  8 14:56 kafka.yml
-rw-rw-r--  1 ubuntu ubuntu   38 Nov 23 15:12 openresty.retry
-rw-rw-r--  1 ubuntu ubuntu  107 Nov 23 10:40 openresty.yml
-rw-rw-r--  1 ubuntu ubuntu  389 Nov  8 14:56 pio.yml
-rw-rw-r--  1 ubuntu ubuntu  932 Nov  8 14:56 pio_elasticsearch.yml
drwxrwsr-x 13 ubuntu ubuntu 4096 Nov 15 08:05 roles/
-rw-rw-r--  1 ubuntu ubuntu  118 Nov  8 14:56 zookeeper.yml
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ cd group_vars/
ubuntu@mastermind:/data/projects/habitat-deploy/ansible/group_vars$ ll
total 44
drwxrwsr-x 2 ubuntu ubuntu 4096 Nov 23 15:13 ./
drwxrwsr-x 8 ubuntu ubuntu 4096 Nov 23 14:48 ../
-rw-rw-r-- 1 ubuntu ubuntu 1710 Nov 15 08:19 all
-rw-rw-r-- 1 ubuntu ubuntu  879 Nov  8 14:56 hadoop
-rw-rw-r-- 1 ubuntu ubuntu  195 Nov 17 12:27 hubot
-rw-rw-r-- 1 ubuntu ubuntu  141 Nov  8 14:56 kafka
-rw-rw-r-- 1 ubuntu ubuntu  985 Nov  8 15:10 kafka_processing
-rw-rw-r-- 1 ubuntu ubuntu  140 Nov  8 14:56 openresty
-rw-rw-r-- 1 ubuntu ubuntu  187 Nov  8 14:56 pio
-rw------- 1 ubuntu ubuntu 1762 Nov 23 15:13 vault.yml
-rw-rw-r-- 1 ubuntu ubuntu   37 Nov  8 14:56 zookeeper
ubuntu@mastermind:/data/projects/habitat-deploy/ansible/group_vars$ vi vault.yml 
ubuntu@mastermind:/data/projects/habitat-deploy/ansible/group_vars$ ansible-vault encrypt vault.yml 
New Vault password: 
Confirm New Vault password: 
Encryption successful
ubuntu@mastermind:/data/projects/habitat-deploy/ansible/group_vars$ cd ..
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ gid pull
The program 'gid' is currently not installed. You can install it by typing:
sudo apt-get install id-utils
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git pull
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 5 (delta 3), reused 0 (delta 0)
Unpacking objects: 100% (5/5), done.
From gitlab.com:vrtoeni/habitat-deploy
   b75ad27..af0e77b  master     -> origin/master
Updating b75ad27..af0e77b
error: Your local changes to the following files would be overwritten by merge:
	ansible/group_vars/vault.yml
Please, commit your changes or stash them before you can merge.
Aborting
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git stash
Saved working directory and index state WIP on master: b75ad27 vault file needs an filename extension
HEAD is now at b75ad27 vault file needs an filename extension
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git pull
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ git pull
Updating b75ad27..af0e77b
Fast-forward
 ansible/group_vars/vault.yml | 188 +++++++++++++++++++++++++++++++++++++++++++++++++++++---------------------------------------------------
 1 file changed, 95 insertions(+), 93 deletions(-)
ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ ansible-playbook -i etc/hosts openresty.yml  --ask-vault-pass
Vault password: 

PLAY [openresty] ***************************************************************

TASK [setup] *******************************************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : install_language-pack-en-base] **********************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : install git] ****************************************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [common : Allow limits to be read from /etc/security/limits.conf] *********
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Set nofile limits] **********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nofile 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nofile 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nofile 65532)

TASK [common : Set nproc limits] ***********************************************
ok: [nginx1.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* soft nproc 65532)
ok: [nginx1.oeni.vrt.be] => (item=* hard nproc 65532)
ok: [nginx2.oeni.vrt.be] => (item=* hard nproc 65532)

TASK [common : Set swappiness to 1] ********************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common : Include partitioning.yml] ***************************************
included: /data/projects/habitat-deploy/ansible/roles/common/tasks/partitioning.yml for nginx1.oeni.vrt.be, nginx2.oeni.vrt.be

TASK [common : Create the filesystem on disk sdb] ******************************
skipping: [nginx1.oeni.vrt.be]
skipping: [nginx2.oeni.vrt.be]

TASK [common : Disable periodic fsck on sdb] ***********************************
skipping: [nginx2.oeni.vrt.be]
skipping: [nginx1.oeni.vrt.be]

TASK [common : Mount datanode disks under /data/{0..n}] ************************
skipping: [nginx1.oeni.vrt.be] => (item=(0, u'sdb')) 
skipping: [nginx2.oeni.vrt.be] => (item=(0, u'sdb')) 

TASK [common-ssh : Ensure .ssh directory exists.] ******************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common-ssh : add ssh keys for the different accounts] ********************
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCBcGtdLrg4xSaa4t+fG9YAB8hMcLDLqmNLKtSHVxGIKKkLIOdIDTwyCkBufINT2gwYPBrGjmZS7jhKu1E2uPc5SaUQ4JR/XTlKDTI1PrFdTi0iZLy7QYEeh4lsuN/UL+szVFLG+KmuawLLmXtKms6oo+WFLNcX2bPDIn6zAjWbWIIVtYphLRxrPZ8xGUzINOt4TKqYXKYzkAEOOm2mz2IKvwHLuwgD9tV1YUdijDsMmfdlCy496uofk4elsIizdtdOd8GO1LRX37YfdIl2kzJO9S8HvfmJX9pgpUAJ2Izz9IJ9+kj7gbmJNajFXM9GlY+L68/2+v39VxVphWXWY1pv vrt_paul_armand_verhaegen '})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfyfnlvNDz2c1/HWNPekZObIt/CGmtJ4Q6pXEs+47mFO9Qk98tdbv6ET452catRzwiqxU6EvXk1QU0ILPeB3IkaXjz3/73yaydVmeHc/LxCPbYfZZHYKhooTn8EuQopzg81FDaydR31F4Of0dlyq5u+nevcIbu1b26ZYURRT+noqBiLnO0kO8cQYFAbSkR4Aq69+90MgsljCkZ43t6SRv2YHGlBociHBpHs68Wo4XDd/Kj/Z3wK1jpWa7IZ9kVR49nxDGZbnzuOpWfpAFLtskFP4/L78xUmb/4n5p9f6xyVFO+Xc6AIzMaYtn4tpmHU2JLzvYMDEEFOhtzTDEkqEnT daan_gerits'})
ok: [nginx1.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})
ok: [nginx2.oeni.vrt.be] => (item={u'user': u'ubuntu', u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDOYPqPd/UiUmJnjrDViaCcDfKVbStQMhFPvH77QTOpIHU5GTm5/oY6SCPNxyxYltK3ItkCCPkm50Hw7wOWtOo10WU4gBCZRg+LENO/VTRX3UZ8Ei6UxnZJFF0j3Cxb0HYq4jVp1OEXvxd/t9jD/Af7ZRMvNL94vGeWiKT518uV+Q27CTa5T8Rq2EaZttei4Y7oNJ3t3EESB4BklstIz9QPLIZgU6OO/ZInQxk8wXpP63G8zEpzRbx5L1lZOmnVmskELvLxaCFItZ+MFXNa1E1EVmidmmXs5oCchznuJl4q8PfM/KkxKBM9bF6oO2GZIHot+ipIIgILQh8WNT71GXkqqX/QuieKrMpOtR98eswbhpb9WyB0xC5fmRLYtb/e4RL56U4epLLZiB9UQRXzJH8rdsET3RA8LHEqh4CAQ7vhPtabiP25w4iDL017m2kfyAGWzcgwW3pO9PuqfsRTes+EZa5ZcXhPsvfXrOnbv+N1B45z9+JW2G6TmRb2uTsP031kYxJGnC39ORLTkvTLUcsv0YIJ52HCZQUWiWkGoClOoAmwKDlZcAhwwKHpStB3AxSDjjn+vcMuVrlGBmKrJZB4IRoAuEYkf1s53wKdrj+hG9S8g3frahHJYn5ERNvqmaR1HxKuAE9FX1IOFmDu3XUY1CRtKi59KayQwU4xWxo15Q== Niels - VRT MacBook Air'})

TASK [common-ssh : load the vault vars] ****************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [common-ssh : Install ssh key for the janitor user] ***********************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [openresty : info about extra vars] ***************************************
ok: [nginx1.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}
ok: [nginx2.oeni.vrt.be] => {
    "msg": "set --extra-vars=\"yes\" to force ansible to reinstall the openresty tar file"
}

TASK [openresty : install prerequisites] ***************************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for openresty] ******************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : unpack openresty directly] ***********************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : create directory for logs] ***********************************
ok: [nginx2.oeni.vrt.be]
ok: [nginx1.oeni.vrt.be]

TASK [openresty : create directory for nginx conf repo] ************************
changed: [nginx1.oeni.vrt.be]
changed: [nginx2.oeni.vrt.be]

TASK [openresty : git clone our openresty] *************************************
changed: [nginx2.oeni.vrt.be]
changed: [nginx1.oeni.vrt.be]

TASK [openresty : create directory for nginx conf] *****************************
ok: [nginx1.oeni.vrt.be]
ok: [nginx2.oeni.vrt.be]

TASK [openresty : set a symbolic] **********************************************
fatal: [nginx1.oeni.vrt.be]: FAILED! => {"changed": false, "failed": true, "gid": 0, "group": "root", "mode": "0644", "msg": "src file does not exist, use \"force=yes\" if you really want to create the link: /data/programs/data_nginx_conf/nginx.conf", "owner": "root", "path": "/data/www/conf/nginx.conf", "size": 4675, "src": "/data/programs/data_nginx_conf/nginx.conf", "state": "file", "uid": 0}
fatal: [nginx2.oeni.vrt.be]: FAILED! => {"changed": false, "failed": true, "gid": 0, "group": "root", "mode": "0644", "msg": "src file does not exist, use \"force=yes\" if you really want to create the link: /data/programs/data_nginx_conf/nginx.conf", "owner": "root", "path": "/data/www/conf/nginx.conf", "size": 4675, "src": "/data/programs/data_nginx_conf/nginx.conf", "state": "file", "uid": 0}

RUNNING HANDLER [common : rebuild locales] *************************************
	to retry, use: --limit @/data/projects/habitat-deploy/ansible/openresty.retry

PLAY RECAP *********************************************************************
nginx1.oeni.vrt.be         : ok=20   changed=5    unreachable=0    failed=1   
nginx2.oeni.vrt.be         : ok=20   changed=5    unreachable=0    failed=1   

ubuntu@mastermind:/data/projects/habitat-deploy/ansible$ Timeout, server 54.194.37.69 not responding.
paularmandsmbp.rto.be 04:58:25 (master) ~/dev_habitat/data_nginx$ po
pod2html         pod2man          pod2text         podchecker       policytool       postdrop         postmulti        
pod2html5.16     pod2man5.16      pod2text5.16     podchecker5.16   popd             postfix          postqueue        
pod2html5.18     pod2man5.18      pod2text5.18     podchecker5.18   post-grohtml     postkick         postsuper        
pod2latex        pod2readme       pod2usage        podselect        postalias        postlock         power_report.sh  
pod2latex5.16    pod2readme5.16   pod2usage5.16    podselect5.16    postcat          postlog          powermetrics     
pod2latex5.18    pod2readme5.18   pod2usage5.18    podselect5.18    postconf         postmap          
paularmandsmbp.rto.be 04:58:25 (master) ~/dev_habitat/data_nginx$ po
pod2html         pod2man          pod2text         podchecker       policytool       postdrop         postmulti        
pod2html5.16     pod2man5.16      pod2text5.16     podchecker5.16   popd             postfix          postqueue        
pod2html5.18     pod2man5.18      pod2text5.18     podchecker5.18   post-grohtml     postkick         postsuper        
pod2latex        pod2readme       pod2usage        podselect        postalias        postlock         power_report.sh  
pod2latex5.16    pod2readme5.16   pod2usage5.16    podselect5.16    postcat          postlog          powermetrics     
pod2latex5.18    pod2readme5.18   pod2usage5.18    podselect5.18    postconf         postmap          
paularmandsmbp.rto.be 04:58:25 (master) ~/dev_habitat/data_nginx$ brew install cmake
==> Downloading https://homebrew.bintray.com/bottles/cmake-3.5.2.el_capitan.bottle.tar.gz
######################################################################## 100.0%
==> Pouring cmake-3.5.2.el_capitan.bottle.tar.gz
==> Caveats
Emacs Lisp files have been installed to:
  /usr/local/share/emacs/site-lisp/cmake
==> Summary
🍺  /usr/local/Cellar/cmake/3.5.2: 2,010 files, 27.5M
paularmandsmbp.rto.be 09:48:09 (master) ~/dev_habitat/data_nginx$ cd ..
paularmandsmbp.rto.be 09:48:12 ~/dev_habitat$ cd ..
paularmandsmbp.rto.be 09:48:13 ~$ cd dev
paularmandsmbp.rto.be 09:48:15 ~/dev$ cd ares/
paularmandsmbp.rto.be 09:48:18 (master) ~/dev/ares$ cd ..
paularmandsmbp.rto.be 09:48:20 ~/dev$ mkdir build
paularmandsmbp.rto.be 09:48:24 ~/dev$ cd build
paularmandsmbp.rto.be 09:48:24 ~/dev/build$ cmake -G "Unix Makefiles" ..
CMake Error: The source directory "/Users/paularmand/dev" does not appear to contain CMakeLists.txt.
Specify --help for usage, or press the help button on the CMake GUI.
paularmandsmbp.rto.be 09:48:25 ~/dev/build$ cd ~/D
Desktop/   Documents/ Downloads/ Dropbox/   
paularmandsmbp.rto.be 09:48:25 ~/dev/build$ cd ~/Downloads/
Display all 261 possibilities? (y or n)
paularmandsmbp.rto.be 09:48:25 ~/dev/build$ cd ~/Downloads/opencv-2.4.13
paularmandsmbp.rto.be 09:49:06 ~/Downloads/opencv-2.4.13$ uu
-bash: uu: command not found
paularmandsmbp.rto.be 09:49:07 ~/Downloads/opencv-2.4.13$ ll
total 160
  0 drwxr-xr-x@  18 paularmand  staff   612B Nov 23 21:44 .
  0 drwx------+ 263 paularmand  staff   8.7K Nov 23 21:44 ..
 16 -rw-r--r--@   1 paularmand  staff   6.0K Nov 23 21:44 .DS_Store
  8 -rwxr-xr-x@   1 paularmand  staff    33B Apr 20  2016 .tgitconfig
  0 drwxr-xr-x@  13 paularmand  staff   442B Apr 20  2016 3rdparty
104 -rwxr-xr-x@   1 paularmand  staff    49K Apr 20  2016 CMakeLists.txt
  8 -rwxr-xr-x@   1 paularmand  staff   191B Apr 20  2016 CONTRIBUTING.md
  8 -rwxr-xr-x@   1 paularmand  staff   1.7K Apr 20  2016 LICENSE
  8 -rwxr-xr-x@   1 paularmand  staff   550B Apr 20  2016 README.md
  0 drwxr-xr-x@   7 paularmand  staff   238B Apr 20  2016 apps
  0 drwxr-xr-x@  43 paularmand  staff   1.4K Apr 20  2016 cmake
  0 drwxr-xr-x@   9 paularmand  staff   306B Apr 20  2016 data
  0 drwxr-xr-x@  30 paularmand  staff   1.0K Apr 20  2016 doc
  0 drwxr-xr-x@   5 paularmand  staff   170B Apr 20  2016 include
  8 -rwxr-xr-x@   1 paularmand  staff   509B Apr 20  2016 index.rst
  0 drwxr-xr-x@  29 paularmand  staff   986B Apr 20  2016 modules
  0 drwxr-xr-x@   9 paularmand  staff   306B Apr 20  2016 platforms
  0 drwxr-xr-x@  13 paularmand  staff   442B Apr 20  2016 samples
paularmandsmbp.rto.be 09:49:08 ~/Downloads/opencv-2.4.13$ mkdir build
paularmandsmbp.rto.be 09:49:12 ~/Downloads/opencv-2.4.13$ cd build
paularmandsmbp.rto.be 09:49:12 ~/Downloads/opencv-2.4.13/build$ cmake -G "Unix Makefiles" ..
-- The CXX compiler identification is AppleClang 7.3.0.7030029
-- The C compiler identification is AppleClang 7.3.0.7030029
-- Check for working CXX compiler: /Library/Developer/CommandLineTools/usr/bin/c++
-- Check for working CXX compiler: /Library/Developer/CommandLineTools/usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Performing Test HAVE_CXX_FSIGNED_CHAR
-- Performing Test HAVE_CXX_FSIGNED_CHAR - Success
-- Performing Test HAVE_C_FSIGNED_CHAR
-- Performing Test HAVE_C_FSIGNED_CHAR - Success
-- Performing Test HAVE_CXX_W
-- Performing Test HAVE_CXX_W - Success
-- Performing Test HAVE_C_W
-- Performing Test HAVE_C_W - Success
-- Performing Test HAVE_CXX_WALL
-- Performing Test HAVE_CXX_WALL - Failed
-- Performing Test HAVE_C_WALL
-- Performing Test HAVE_C_WALL - Failed
-- Performing Test HAVE_CXX_WERROR_RETURN_TYPE
-- Performing Test HAVE_CXX_WERROR_RETURN_TYPE - Success
-- Performing Test HAVE_C_WERROR_RETURN_TYPE
-- Performing Test HAVE_C_WERROR_RETURN_TYPE - Success
-- Performing Test HAVE_CXX_WERROR_ADDRESS
-- Performing Test HAVE_CXX_WERROR_ADDRESS - Success
-- Performing Test HAVE_C_WERROR_ADDRESS
-- Performing Test HAVE_C_WERROR_ADDRESS - Success
-- Performing Test HAVE_CXX_WERROR_SEQUENCE_POINT
-- Performing Test HAVE_CXX_WERROR_SEQUENCE_POINT - Success
-- Performing Test HAVE_C_WERROR_SEQUENCE_POINT
-- Performing Test HAVE_C_WERROR_SEQUENCE_POINT - Success
-- Performing Test HAVE_CXX_WFORMAT
-- Performing Test HAVE_CXX_WFORMAT - Success
-- Performing Test HAVE_C_WFORMAT
-- Performing Test HAVE_C_WFORMAT - Success
-- Performing Test HAVE_CXX_WERROR_FORMAT_SECURITY
-- Performing Test HAVE_CXX_WERROR_FORMAT_SECURITY - Success
-- Performing Test HAVE_C_WERROR_FORMAT_SECURITY
-- Performing Test HAVE_C_WERROR_FORMAT_SECURITY - Success
-- Performing Test HAVE_CXX_WMISSING_DECLARATIONS
-- Performing Test HAVE_CXX_WMISSING_DECLARATIONS - Success
-- Performing Test HAVE_C_WMISSING_DECLARATIONS
-- Performing Test HAVE_C_WMISSING_DECLARATIONS - Success
-- Performing Test HAVE_CXX_WMISSING_PROTOTYPES
-- Performing Test HAVE_CXX_WMISSING_PROTOTYPES - Success
-- Performing Test HAVE_C_WMISSING_PROTOTYPES
-- Performing Test HAVE_C_WMISSING_PROTOTYPES - Success
-- Performing Test HAVE_CXX_WSTRICT_PROTOTYPES
-- Performing Test HAVE_CXX_WSTRICT_PROTOTYPES - Success
-- Performing Test HAVE_C_WSTRICT_PROTOTYPES
-- Performing Test HAVE_C_WSTRICT_PROTOTYPES - Success
-- Performing Test HAVE_CXX_WUNDEF
-- Performing Test HAVE_CXX_WUNDEF - Success
-- Performing Test HAVE_C_WUNDEF
-- Performing Test HAVE_C_WUNDEF - Success
-- Performing Test HAVE_CXX_WINIT_SELF
-- Performing Test HAVE_CXX_WINIT_SELF - Success
-- Performing Test HAVE_C_WINIT_SELF
-- Performing Test HAVE_C_WINIT_SELF - Success
-- Performing Test HAVE_CXX_WPOINTER_ARITH
-- Performing Test HAVE_CXX_WPOINTER_ARITH - Success
-- Performing Test HAVE_C_WPOINTER_ARITH
-- Performing Test HAVE_C_WPOINTER_ARITH - Success
-- Performing Test HAVE_CXX_WSHADOW
-- Performing Test HAVE_CXX_WSHADOW - Success
-- Performing Test HAVE_C_WSHADOW
-- Performing Test HAVE_C_WSHADOW - Success
-- Performing Test HAVE_CXX_WSIGN_PROMO
-- Performing Test HAVE_CXX_WSIGN_PROMO - Success
-- Performing Test HAVE_C_WSIGN_PROMO
-- Performing Test HAVE_C_WSIGN_PROMO - Success
-- Performing Test HAVE_CXX_WNO_NARROWING
-- Performing Test HAVE_CXX_WNO_NARROWING - Success
-- Performing Test HAVE_C_WNO_NARROWING
-- Performing Test HAVE_C_WNO_NARROWING - Success
-- Performing Test HAVE_CXX_WNO_DELETE_NON_VIRTUAL_DTOR
-- Performing Test HAVE_CXX_WNO_DELETE_NON_VIRTUAL_DTOR - Success
-- Performing Test HAVE_C_WNO_DELETE_NON_VIRTUAL_DTOR
-- Performing Test HAVE_C_WNO_DELETE_NON_VIRTUAL_DTOR - Success
-- Performing Test HAVE_CXX_WNO_UNNAMED_TYPE_TEMPLATE_ARGS
-- Performing Test HAVE_CXX_WNO_UNNAMED_TYPE_TEMPLATE_ARGS - Success
-- Performing Test HAVE_C_WNO_UNNAMED_TYPE_TEMPLATE_ARGS
-- Performing Test HAVE_C_WNO_UNNAMED_TYPE_TEMPLATE_ARGS - Success
-- Performing Test HAVE_CXX_WNO_ARRAY_BOUNDS
-- Performing Test HAVE_CXX_WNO_ARRAY_BOUNDS - Success
-- Performing Test HAVE_C_WNO_ARRAY_BOUNDS
-- Performing Test HAVE_C_WNO_ARRAY_BOUNDS - Success
-- Performing Test HAVE_CXX_WNO_AGGRESSIVE_LOOP_OPTIMIZATIONS
-- Performing Test HAVE_CXX_WNO_AGGRESSIVE_LOOP_OPTIMIZATIONS - Failed
-- Performing Test HAVE_C_WNO_AGGRESSIVE_LOOP_OPTIMIZATIONS
-- Performing Test HAVE_C_WNO_AGGRESSIVE_LOOP_OPTIMIZATIONS - Failed
-- Performing Test HAVE_CXX_FDIAGNOSTICS_SHOW_OPTION
-- Performing Test HAVE_CXX_FDIAGNOSTICS_SHOW_OPTION - Success
-- Performing Test HAVE_C_FDIAGNOSTICS_SHOW_OPTION
-- Performing Test HAVE_C_FDIAGNOSTICS_SHOW_OPTION - Success
-- Performing Test HAVE_CXX_WNO_LONG_LONG
-- Performing Test HAVE_CXX_WNO_LONG_LONG - Success
-- Performing Test HAVE_C_WNO_LONG_LONG
-- Performing Test HAVE_C_WNO_LONG_LONG - Success
-- Performing Test HAVE_CXX_WNO_SEMICOLON_BEFORE_METHOD_BODY
-- Performing Test HAVE_CXX_WNO_SEMICOLON_BEFORE_METHOD_BODY - Success
-- Performing Test HAVE_C_WNO_SEMICOLON_BEFORE_METHOD_BODY
-- Performing Test HAVE_C_WNO_SEMICOLON_BEFORE_METHOD_BODY - Success
-- Performing Test HAVE_CXX_FNO_OMIT_FRAME_POINTER
-- Performing Test HAVE_CXX_FNO_OMIT_FRAME_POINTER - Success
-- Performing Test HAVE_C_FNO_OMIT_FRAME_POINTER
-- Performing Test HAVE_C_FNO_OMIT_FRAME_POINTER - Success
-- Performing Test HAVE_CXX_MSSE
-- Performing Test HAVE_CXX_MSSE - Success
-- Performing Test HAVE_C_MSSE
-- Performing Test HAVE_C_MSSE - Success
-- Performing Test HAVE_CXX_MSSE2
-- Performing Test HAVE_CXX_MSSE2 - Success
-- Performing Test HAVE_C_MSSE2
-- Performing Test HAVE_C_MSSE2 - Success
-- Performing Test HAVE_CXX_MSSE3
-- Performing Test HAVE_CXX_MSSE3 - Success
-- Performing Test HAVE_C_MSSE3
-- Performing Test HAVE_C_MSSE3 - Success
-- Check if the system is big endian
-- Searching 16 bit integer
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of unsigned short
-- Check size of unsigned short - done
-- Using unsigned short
-- Check if the system is big endian - little endian
-- Looking for fseeko
-- Looking for fseeko - found
-- Looking for unistd.h
-- Looking for unistd.h - found
-- Check size of off64_t
-- Check size of off64_t - failed
-- Performing Test HAVE_C_WNO_SHORTEN_64_TO_32
-- Performing Test HAVE_C_WNO_SHORTEN_64_TO_32 - Success
-- Performing Test HAVE_C_WNO_ATTRIBUTES
-- Performing Test HAVE_C_WNO_ATTRIBUTES - Success
-- Performing Test HAVE_C_WNO_STRICT_PROTOTYPES
-- Performing Test HAVE_C_WNO_STRICT_PROTOTYPES - Success
-- Performing Test HAVE_C_WNO_MISSING_PROTOTYPES
-- Performing Test HAVE_C_WNO_MISSING_PROTOTYPES - Success
-- Performing Test HAVE_C_WNO_MISSING_DECLARATIONS
-- Performing Test HAVE_C_WNO_MISSING_DECLARATIONS - Success
-- Performing Test HAVE_C_WNO_SHIFT_NEGATIVE_VALUE
-- Performing Test HAVE_C_WNO_SHIFT_NEGATIVE_VALUE - Success
-- Looking for assert.h
-- Looking for assert.h - found
-- Looking for fcntl.h
-- Looking for fcntl.h - found
-- Looking for io.h
-- Looking for io.h - not found
-- Looking for jbg_newlen
-- Looking for jbg_newlen - not found
-- Looking for mmap
-- Looking for mmap - found
-- Looking for search.h
-- Looking for search.h - found
-- Looking for string.h
-- Looking for string.h - found
-- Looking for unistd.h
-- Looking for unistd.h - found
-- Performing Test HAVE_C_WNO_UNUSED_BUT_SET_VARIABLE
-- Performing Test HAVE_C_WNO_UNUSED_BUT_SET_VARIABLE - Failed
-- Performing Test HAVE_C_WNO_UNDEF
-- Performing Test HAVE_C_WNO_UNDEF - Success
-- Performing Test HAVE_C_WNO_UNUSED
-- Performing Test HAVE_C_WNO_UNUSED - Success
-- Performing Test HAVE_C_WNO_SIGN_COMPARE
-- Performing Test HAVE_C_WNO_SIGN_COMPARE - Success
-- Performing Test HAVE_C_WNO_CAST_ALIGN
-- Performing Test HAVE_C_WNO_CAST_ALIGN - Success
-- Performing Test HAVE_C_WNO_SHADOW
-- Performing Test HAVE_C_WNO_SHADOW - Success
-- Performing Test HAVE_C_WNO_MAYBE_UNINITIALIZED
-- Performing Test HAVE_C_WNO_MAYBE_UNINITIALIZED - Failed
-- Performing Test HAVE_C_WNO_POINTER_TO_INT_CAST
-- Performing Test HAVE_C_WNO_POINTER_TO_INT_CAST - Success
-- Performing Test HAVE_C_WNO_INT_TO_POINTER_CAST
-- Performing Test HAVE_C_WNO_INT_TO_POINTER_CAST - Success
-- Performing Test HAVE_C_WNO_UNUSED_PARAMETER
-- Performing Test HAVE_C_WNO_UNUSED_PARAMETER - Success
-- Performing Test HAVE_CXX_WNO_MISSING_DECLARATIONS
-- Performing Test HAVE_CXX_WNO_MISSING_DECLARATIONS - Success
-- Performing Test HAVE_CXX_WNO_UNUSED_PARAMETER
-- Performing Test HAVE_CXX_WNO_UNUSED_PARAMETER - Success
-- Performing Test HAVE_C_WNO_IMPLICIT_FUNCTION_DECLARATION
-- Performing Test HAVE_C_WNO_IMPLICIT_FUNCTION_DECLARATION - Success
-- Performing Test HAVE_C_WNO_UNINITIALIZED
-- Performing Test HAVE_C_WNO_UNINITIALIZED - Success
-- Performing Test HAVE_C_WNO_UNUSED_BUT_SET_PARAMETER
-- Performing Test HAVE_C_WNO_UNUSED_BUT_SET_PARAMETER - Failed
-- Looking for semaphore.h
-- Looking for semaphore.h - found
-- Performing Test HAVE_CXX_WNO_SHADOW
-- Performing Test HAVE_CXX_WNO_SHADOW - Success
-- Performing Test HAVE_CXX_WNO_UNUSED
-- Performing Test HAVE_CXX_WNO_UNUSED - Success
-- Performing Test HAVE_CXX_WNO_SIGN_COMPARE
-- Performing Test HAVE_CXX_WNO_SIGN_COMPARE - Success
-- Performing Test HAVE_CXX_WNO_UNDEF
-- Performing Test HAVE_CXX_WNO_UNDEF - Success
-- Performing Test HAVE_CXX_WNO_UNINITIALIZED
-- Performing Test HAVE_CXX_WNO_UNINITIALIZED - Success
-- Performing Test HAVE_CXX_WNO_SWITCH
-- Performing Test HAVE_CXX_WNO_SWITCH - Success
-- Performing Test HAVE_CXX_WNO_PARENTHESES
-- Performing Test HAVE_CXX_WNO_PARENTHESES - Success
-- Performing Test HAVE_CXX_WNO_EXTRA
-- Performing Test HAVE_CXX_WNO_EXTRA - Success
-- Performing Test HAVE_CXX_WNO_DEPRECATED_DECLARATIONS
-- Performing Test HAVE_CXX_WNO_DEPRECATED_DECLARATIONS - Success
-- Looking for linux/videodev.h
-- Looking for linux/videodev.h - not found
-- Looking for linux/videodev2.h
-- Looking for linux/videodev2.h - not found
-- Looking for sys/videoio.h
-- Looking for sys/videoio.h - not found
-- Looking for libavformat/avformat.h
-- Looking for libavformat/avformat.h - found
-- Looking for ffmpeg/avformat.h
-- Looking for ffmpeg/avformat.h - not found
-- Found PythonInterp: /usr/bin/python (found suitable version "2.7.10", minimum required is "2.0") 
-- Found PythonLibs: /usr/lib/libpython2.7.dylib (found suitable exact version "2.7.10") 
-- Found JNI: /Library/Java/JavaVirtualMachines/jdk1.8.0_91.jdk/Contents/Home/jre/lib/libjawt.dylib  
-- Assume that non-module dependency is available: -framework OpenCL (for module opencv_ocl)
-- Performing Test HAVE_OBJCXX_FOBJC_EXCEPTIONS
-- Performing Test HAVE_OBJCXX_FOBJC_EXCEPTIONS - Success
-- Performing Test HAVE_CXX_WNO_CLOBBERED
-- Performing Test HAVE_CXX_WNO_CLOBBERED - Failed
-- 
-- General configuration for OpenCV 2.4.13 =====================================
--   Version control:               unknown
-- 
--   Platform:
--     Host:                        Darwin 15.0.0 x86_64
--     CMake:                       3.5.2
--     CMake generator:             Unix Makefiles
--     CMake build tool:            /usr/bin/make
--     Configuration:               Release
-- 
--   C/C++:
--     Built as dynamic libs?:      YES
--     C++ Compiler:                /Library/Developer/CommandLineTools/usr/bin/c++  (ver 7.3.0.7030029)
--     C++ flags (Release):         -fsigned-char -W -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-array-bounds -fdiagnostics-show-option -Wno-long-long -Wno-semicolon-before-method-body -fno-omit-frame-pointer -msse -msse2 -msse3 -O3 -DNDEBUG  -DNDEBUG
--     C++ flags (Debug):           -fsigned-char -W -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-array-bounds -fdiagnostics-show-option -Wno-long-long -Wno-semicolon-before-method-body -fno-omit-frame-pointer -msse -msse2 -msse3 -g  -O0 -DDEBUG -D_DEBUG
--     C Compiler:                  /Library/Developer/CommandLineTools/usr/bin/cc
--     C flags (Release):           -fsigned-char -W -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-array-bounds -fdiagnostics-show-option -Wno-long-long -Wno-semicolon-before-method-body -fno-omit-frame-pointer -msse -msse2 -msse3 -O3 -DNDEBUG  -DNDEBUG
--     C flags (Debug):             -fsigned-char -W -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-array-bounds -fdiagnostics-show-option -Wno-long-long -Wno-semicolon-before-method-body -fno-omit-frame-pointer -msse -msse2 -msse3 -g  -O0 -DDEBUG -D_DEBUG
--     Linker flags (Release):
--     Linker flags (Debug):
--     Precompiled headers:         NO
-- 
--   OpenCV modules:
--     To be built:                 core flann imgproc highgui features2d calib3d ml video legacy objdetect photo gpu ocl nonfree contrib python stitching superres ts videostab
--     Disabled:                    world
--     Disabled by dependency:      -
--     Unavailable:                 androidcamera dynamicuda java viz
-- 
--   GUI: 
--     QT:                          NO
--     Cocoa:                       YES
--     OpenGL support:              NO
--     VTK support:                 NO
-- 
--   Media I/O: 
--     ZLib:                        build (ver 1.2.7)
--     JPEG:                        build (ver 62)
--     PNG:                         build (ver 1.5.12)
--     TIFF:                        build (ver 42 - 4.0.2)
--     JPEG 2000:                   build (ver 1.900.1)
--     OpenEXR:                     build (ver 1.7.1)
-- 
--   Video I/O:
--     DC1394 1.x:                  NO
--     DC1394 2.x:                  NO
--     FFMPEG:                      YES
--       codec:                     NO
--       format:                    NO
--       util:                      NO
--       swscale:                   NO
--       resample:                  NO
--       gentoo-style:              YES
--     GStreamer:                   NO
--     OpenNI:                      NO
--     OpenNI PrimeSensor Modules:  NO
--     PvAPI:                       NO
--     GigEVisionSDK:               NO
--     QuickTime:                   NO
--     QTKit:                       YES
--     V4L/V4L2:                    NO/NO
--     XIMEA:                       NO
-- 
--   Other third-party libraries:
--     Use IPP:                     NO
--     Use Eigen:                   NO
--     Use TBB:                     NO
--     Use OpenMP:                  NO
--     Use GCD                      YES
--     Use Concurrency              NO
--     Use C=:                      NO
--     Use Cuda:                    NO
--     Use OpenCL:                  YES
-- 
--   OpenCL:
--     Version:                     static
--     libraries:                   -framework OpenCL
--     Use AMD FFT:                 NO
--     Use AMD BLAS:                NO
-- 
--   Python:
--     Interpreter:                 /usr/bin/python (ver 2.7.10)
--     Libraries:                   /usr/lib/libpython2.7.dylib (ver 2.7.10)
--     numpy:                       /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/core/include (ver 1.8.0rc1)
--     packages path:               lib/python2.7/site-packages
-- 
--   Java:
--     ant:                         NO
--     JNI:                         /Library/Java/JavaVirtualMachines/jdk1.8.0_91.jdk/Contents/Home/include /Library/Java/JavaVirtualMachines/jdk1.8.0_91.jdk/Contents/Home/include/darwin /Library/Java/JavaVirtualMachines/jdk1.8.0_91.jdk/Contents/Home/include
--     Java tests:                  NO
-- 
--   Documentation:
--     Build Documentation:         NO
--     Sphinx:                      NO
--     PdfLaTeX compiler:           NO
--     Doxygen:                     NO
-- 
--   Tests and samples:
--     Tests:                       YES
--     Performance tests:           YES
--     C/C++ Examples:              NO
-- 
--   Install path:                  /usr/local
-- 
--   cvconfig.h is in:              /Users/paularmand/Downloads/opencv-2.4.13/build
-- -----------------------------------------------------------------
-- 
CMake Warning at cmake/OpenCVPackaging.cmake:23 (message):
  CPACK_PACKAGE_VERSION does not match version provided by version.hpp
  header!
Call Stack (most recent call first):
  CMakeLists.txt:1105 (include)


-- Configuring done
-- Generating done
-- Build files have been written to: /Users/paularmand/Downloads/opencv-2.4.13/build
paularmandsmbp.rto.be 09:49:34 ~/Downloads/opencv-2.4.13/build$ make -j8
Scanning dependencies of target zlib
Scanning dependencies of target libjasper
Scanning dependencies of target libjpeg
[  0%] Building C object 3rdparty/zlib/CMakeFiles/zlib.dir/adler32.c.o
[  0%] Building C object 3rdparty/zlib/CMakeFiles/zlib.dir/crc32.c.o
[  0%] Building C object 3rdparty/zlib/CMakeFiles/zlib.dir/compress.c.o
[  0%] Building C object 3rdparty/zlib/CMakeFiles/zlib.dir/deflate.c.o
[  0%] Building C object 3rdparty/zlib/CMakeFiles/zlib.dir/gzclose.c.o
[  1%] Building C object 3rdparty/zlib/CMakeFiles/zlib.dir/gzlib.c.o
[  1%] Building C object 3rdparty/zlib/CMakeFiles/zlib.dir/gzread.c.o
[  1%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jcapimin.c.o
[  1%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_cm.c.o
[  1%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_debug.c.o
[  1%] Building C object 3rdparty/zlib/CMakeFiles/zlib.dir/gzwrite.c.o
[  1%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jcapistd.c.o
[  1%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jccoefct.c.o
[  1%] Building C object 3rdparty/zlib/CMakeFiles/zlib.dir/inflate.c.o
[  1%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_getopt.c.o
[  1%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jccolor.c.o
[  1%] Building C object 3rdparty/zlib/CMakeFiles/zlib.dir/infback.c.o
[  2%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_icc.c.o
[  2%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jcdctmgr.c.o
[  2%] Building C object 3rdparty/zlib/CMakeFiles/zlib.dir/inftrees.c.o
[  2%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_iccdata.c.o
[  2%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_image.c.o
[  2%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jchuff.c.o
[  2%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_init.c.o
[  2%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_malloc.c.o
[  2%] Building C object 3rdparty/zlib/CMakeFiles/zlib.dir/inffast.c.o
[  2%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jcinit.c.o
[  2%] Building C object 3rdparty/zlib/CMakeFiles/zlib.dir/trees.c.o
[  2%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_seq.c.o
[  3%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jcmainct.c.o
[  3%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_stream.c.o
[  3%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jcmarker.c.o
[  3%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_string.c.o
[  3%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_tmr.c.o
[  3%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jcmaster.c.o
[  3%] Building C object 3rdparty/zlib/CMakeFiles/zlib.dir/uncompr.c.o
[  3%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_tvp.c.o
[  3%] Building C object 3rdparty/zlib/CMakeFiles/zlib.dir/zutil.c.o
[  4%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_version.c.o
[  4%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jcomapi.c.o
[  4%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jcparam.c.o
[  4%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jp2_cod.c.o
[  4%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jcphuff.c.o
[  5%] Linking C static library ../lib/libzlib.a
[  5%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jcprepct.c.o
[  5%] Built target zlib
[  5%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jp2_dec.c.o
Scanning dependencies of target libtiff
[  5%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_aux.c.o
[  5%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jp2_enc.c.o
[  5%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_close.c.o
Scanning dependencies of target libpng
[  5%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jcsample.c.o
[  5%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_bs.c.o
[  5%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_codec.c.o
[  6%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/png.c.o
[  6%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_color.c.o
[  6%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jctrans.c.o
[  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_compress.c.o
Scanning dependencies of target IlmImf
[  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_dir.c.o
[  7%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngerror.c.o
[  7%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Half/half.cpp.o
[  7%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_cs.c.o
[  7%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jdapimin.c.o
[  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_dirinfo.c.o
Scanning dependencies of target opencv_core
[  7%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/algorithm.cpp.o
[  7%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngget.c.o
[  8%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jdapistd.c.o
[  8%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jdatadst.c.o
[  8%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngmem.c.o
[  8%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jdatasrc.c.o
[  8%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jdcoefct.c.o
[  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_dirread.c.o
[  8%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/alloc.cpp.o
[  8%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngpread.c.o
[  8%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Iex/IexBaseExc.cpp.o
[  8%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_dec.c.o
[  8%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jdcolor.c.o
[  8%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngread.c.o
[  8%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jddctmgr.c.o
[  8%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jdhuff.c.o
[  8%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngrio.c.o
[  8%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngrtran.c.o
[  8%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jdinput.c.o
[  8%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jdmainct.c.o
[  8%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/arithm.cpp.o
[  8%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jdmarker.c.o
[  8%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Iex/IexThrowErrnoExc.cpp.o
[  8%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_enc.c.o
[  9%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jdmaster.c.o
[  9%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jdmerge.c.o
[  9%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_math.c.o
[  9%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngrutil.c.o
[  9%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jdphuff.c.o
[  9%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jdpostct.c.o
[  9%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jdsample.c.o
[  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_dirwrite.c.o
[  9%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jdtrans.c.o
[  9%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jerror.c.o
[  9%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jfdctflt.c.o
[  9%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThread.cpp.o
[  9%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadMutex.cpp.o
[  9%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jfdctfst.c.o
[  9%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadMutexPosix.cpp.o
[  9%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jfdctint.c.o
[ 10%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jidctflt.c.o
[ 10%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jidctfst.c.o
[ 10%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jidctint.c.o
[ 10%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jidctred.c.o
[ 10%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jmemansi.c.o
[ 10%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jmemmgr.c.o
[ 10%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/array.cpp.o
[ 10%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngset.c.o
[ 10%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadPool.cpp.o
[ 10%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jquant1.c.o
[ 10%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_mct.c.o
[ 11%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngtrans.c.o
[ 12%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_mqcod.c.o
[ 12%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_mqdec.c.o
[ 12%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_mqenc.c.o
[ 12%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngwio.c.o
[ 12%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngwrite.c.o
[ 12%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jquant2.c.o
[ 12%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_dumpmode.c.o
[ 12%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadPosix.cpp.o
[ 12%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_qmfb.c.o
[ 12%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_error.c.o
[ 12%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_extension.c.o
[ 12%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_fax3.c.o
[ 12%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngwtran.c.o
[ 13%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/cmdparser.cpp.o
[ 13%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngwutil.c.o
[ 13%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadSemaphore.cpp.o
[ 13%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadSemaphorePosix.cpp.o
[ 13%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/jutils.c.o
[ 13%] Building C object 3rdparty/libjpeg/CMakeFiles/libjpeg.dir/transupp.c.o
[ 14%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadSemaphorePosixCompat.cpp.o
[ 14%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathColorAlgo.cpp.o
[ 14%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_fax3sm.c.o
[ 15%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_flush.c.o
[ 15%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_getimage.c.o
[ 15%] Linking C static library ../lib/liblibpng.a
[ 15%] Built target libpng
[ 15%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t1cod.c.o
[ 15%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathFun.cpp.o
[ 15%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathMatrixAlgo.cpp.o
[ 15%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t1dec.c.o
[ 15%] Linking C static library ../lib/liblibjpeg.a
[ 15%] Built target libjpeg
[ 15%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/convert.cpp.o
[ 15%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathRandom.cpp.o
[ 15%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t1enc.c.o
[ 15%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_jbig.c.o
[ 15%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_jpeg_12.c.o
[ 15%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_jpeg.c.o
[ 15%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_luv.c.o
[ 15%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathVec.cpp.o
[ 15%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/copy.cpp.o
[ 15%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/b44ExpLogTable.cpp.o
[ 15%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_lzma.c.o
[ 15%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_lzw.c.o
[ 15%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t2cod.c.o
[ 15%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/datastructs.cpp.o
[ 15%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_next.c.o
[ 15%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_ojpeg.c.o
[ 16%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_open.c.o
[ 16%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_packbits.c.o
[ 16%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t2dec.c.o
[ 16%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_pixarlog.c.o
[ 16%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/drawing.cpp.o
[ 16%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfAcesFile.cpp.o
[ 16%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t2enc.c.o
[ 16%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_tagtree.c.o
[ 17%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_tsfb.c.o
[ 17%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_util.c.o
[ 17%] Linking C static library ../lib/liblibjasper.a
[ 17%] Built target libjasper
[ 17%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_predict.c.o
[ 17%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfAttribute.cpp.o
[ 17%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/dxt.cpp.o
[ 17%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_print.c.o
[ 17%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_read.c.o
[ 17%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_strip.c.o
[ 17%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_swab.c.o
[ 17%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_thunder.c.o
[ 17%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_tile.c.o
[ 18%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_version.c.o
[ 18%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_warning.c.o
[ 18%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_write.c.o
[ 18%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfB44Compressor.cpp.o
[ 18%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_zip.c.o
[ 18%] Building CXX object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_stream.cxx.o
[ 19%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfBoxAttribute.cpp.o
[ 19%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/gl_core_3_1.cpp.o
[ 19%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_unix.c.o
[ 19%] Linking CXX static library ../lib/liblibtiff.a
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/liblibtiff.a(tif_jbig.c.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/liblibtiff.a(tif_jpeg_12.c.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/liblibtiff.a(tif_jpeg.c.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/liblibtiff.a(tif_lzma.c.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/liblibtiff.a(tif_ojpeg.c.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/liblibtiff.a(tif_jbig.c.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/liblibtiff.a(tif_jpeg_12.c.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/liblibtiff.a(tif_jpeg.c.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/liblibtiff.a(tif_lzma.c.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/liblibtiff.a(tif_ojpeg.c.o) has no symbols
[ 19%] Built target libtiff
[ 19%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfChannelList.cpp.o
[ 19%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/glob.cpp.o
[ 19%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfChannelListAttribute.cpp.o
[ 19%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfChromaticities.cpp.o
[ 19%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/gpumat.cpp.o
[ 19%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/lapack.cpp.o
[ 20%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/mathfuncs.cpp.o
[ 20%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfChromaticitiesAttribute.cpp.o
[ 20%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfCompressionAttribute.cpp.o
[ 20%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matmul.cpp.o
[ 20%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfCompressor.cpp.o
[ 20%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfConvert.cpp.o
[ 20%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfCRgbaFile.cpp.o
[ 20%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matop.cpp.o
[ 20%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix.cpp.o
[ 20%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDoubleAttribute.cpp.o
[ 21%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfEnvmap.cpp.o
[ 21%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/opengl_interop.cpp.o
[ 21%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfEnvmapAttribute.cpp.o
[ 21%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/opengl_interop_deprecated.cpp.o
[ 21%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfFloatAttribute.cpp.o
[ 21%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfFrameBuffer.cpp.o
[ 21%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/out.cpp.o
[ 21%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfFramesPerSecond.cpp.o
[ 21%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfHeader.cpp.o
[ 21%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfHuf.cpp.o
[ 21%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/parallel.cpp.o
[ 21%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfInputFile.cpp.o
[ 21%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/persistence.cpp.o
[ 21%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfIntAttribute.cpp.o
[ 21%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/rand.cpp.o
[ 22%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/stat.cpp.o
[ 22%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/system.cpp.o
[ 22%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfIO.cpp.o
[ 23%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfKeyCode.cpp.o
[ 23%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfKeyCodeAttribute.cpp.o
[ 23%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/tables.cpp.o
[ 23%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfLineOrderAttribute.cpp.o
[ 23%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfLut.cpp.o
[ 23%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfMatrixAttribute.cpp.o
[ 23%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfMisc.cpp.o
[ 23%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfMultiView.cpp.o
[ 23%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfOpaqueAttribute.cpp.o
[ 23%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfOutputFile.cpp.o
[ 23%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfPizCompressor.cpp.o
[ 24%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfPreviewImage.cpp.o
[ 24%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfPreviewImageAttribute.cpp.o
[ 24%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfPxr24Compressor.cpp.o
[ 24%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRational.cpp.o
[ 24%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRationalAttribute.cpp.o
[ 24%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRgbaFile.cpp.o
[ 24%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRgbaYca.cpp.o
[ 24%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRleCompressor.cpp.o
[ 24%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfScanLineInputFile.cpp.o
[ 24%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfStandardAttributes.cpp.o
[ 24%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfStdIO.cpp.o
[ 25%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfStringAttribute.cpp.o
[ 25%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfStringVectorAttribute.cpp.o
[ 25%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTestFile.cpp.o
[ 25%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfThreading.cpp.o
[ 25%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTileDescriptionAttribute.cpp.o
[ 25%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTiledInputFile.cpp.o
[ 25%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTiledMisc.cpp.o
[ 25%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTiledOutputFile.cpp.o
[ 25%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTiledRgbaFile.cpp.o
[ 25%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTileOffsets.cpp.o
[ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTimeCode.cpp.o
[ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTimeCodeAttribute.cpp.o
[ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfVecAttribute.cpp.o
[ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfVersion.cpp.o
[ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfWav.cpp.o
[ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfZipCompressor.cpp.o
[ 26%] Linking CXX static library ../lib/libIlmImf.a
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/libIlmImf.a(IlmThread.cpp.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/libIlmImf.a(IlmThreadMutex.cpp.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/libIlmImf.a(IlmThreadSemaphore.cpp.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/libIlmImf.a(IlmThreadSemaphorePosixCompat.cpp.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/libIlmImf.a(IlmThread.cpp.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/libIlmImf.a(IlmThreadMutex.cpp.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/libIlmImf.a(IlmThreadSemaphore.cpp.o) has no symbols
/Library/Developer/CommandLineTools/usr/bin/ranlib: file: ../lib/libIlmImf.a(IlmThreadSemaphorePosixCompat.cpp.o) has no symbols
[ 26%] Built target IlmImf
[ 26%] Linking CXX shared library ../../lib/libopencv_core.dylib
[ 26%] Built target opencv_core
Scanning dependencies of target opencv_flann
Scanning dependencies of target opencv_ml
Scanning dependencies of target opencv_imgproc
[ 26%] Building CXX object modules/flann/CMakeFiles/opencv_flann.dir/src/flann.cpp.o
[ 26%] Building CXX object modules/flann/CMakeFiles/opencv_flann.dir/src/miniflann.cpp.o
[ 26%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/ann_mlp.cpp.o
[ 26%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/boost.cpp.o
[ 26%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/cnn.cpp.o
[ 26%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/data.cpp.o
[ 27%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/em.cpp.o
[ 28%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/accum.cpp.o
[ 28%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/approx.cpp.o
[ 28%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/ertrees.cpp.o
[ 28%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/estimate.cpp.o
[ 28%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/avx/imgwarp_avx.cpp.o
[ 28%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/gbt.cpp.o
[ 28%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/avx2/imgwarp_avx2.cpp.o
[ 28%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/inner_functions.cpp.o
[ 28%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/canny.cpp.o
[ 28%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/knearest.cpp.o
[ 28%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/ml_init.cpp.o
[ 28%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/nbayes.cpp.o
[ 28%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/clahe.cpp.o
[ 28%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/color.cpp.o
[ 28%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/rtrees.cpp.o
[ 28%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/contours.cpp.o
[ 28%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/svm.cpp.o
[ 28%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/convhull.cpp.o
[ 29%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/testset.cpp.o
[ 29%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/corner.cpp.o
[ 30%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/cornersubpix.cpp.o
[ 30%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/deriv.cpp.o
[ 30%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/tree.cpp.o
[ 30%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/distransform.cpp.o
[ 30%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/emd.cpp.o
[ 30%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/featureselect.cpp.o
[ 30%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/filter.cpp.o
[ 30%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/floodfill.cpp.o
[ 30%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/gabor.cpp.o
[ 30%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/generalized_hough.cpp.o
[ 30%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/geometry.cpp.o
[ 31%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/grabcut.cpp.o
[ 31%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/histogram.cpp.o
[ 31%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/hough.cpp.o
[ 31%] Linking CXX shared library ../../lib/libopencv_ml.dylib
[ 31%] Built target opencv_ml
[ 31%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/imgwarp.cpp.o
[ 31%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/linefit.cpp.o
[ 31%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/matchcontours.cpp.o
[ 31%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/moments.cpp.o
[ 31%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/morph.cpp.o
[ 31%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/phasecorr.cpp.o
[ 31%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/pyramids.cpp.o
[ 31%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/rotcalipers.cpp.o
[ 32%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/samplers.cpp.o
[ 32%] Linking CXX shared library ../../lib/libopencv_flann.dylib
[ 32%] Built target opencv_flann
[ 32%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/segmentation.cpp.o
[ 32%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/shapedescr.cpp.o
[ 32%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/smooth.cpp.o
[ 32%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/subdivision2d.cpp.o
[ 32%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/sumpixels.cpp.o
[ 32%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/tables.cpp.o
[ 32%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/templmatch.cpp.o
[ 32%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/thresh.cpp.o
[ 32%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/undistort.cpp.o
[ 33%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/utils.cpp.o
[ 33%] Linking CXX shared library ../../lib/libopencv_imgproc.dylib
[ 33%] Built target opencv_imgproc
Scanning dependencies of target opencv_photo
Scanning dependencies of target opencv_video
Scanning dependencies of target opencv_highgui
[ 33%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/inpaint.cpp.o
[ 33%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/denoising.cpp.o
[ 33%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/bgfg_gaussmix.cpp.o
[ 33%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/bgfg_gaussmix2.cpp.o
[ 33%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/bgfg_gmg.cpp.o
[ 33%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/camshift.cpp.o
[ 33%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/kalman.cpp.o
[ 34%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/cap.cpp.o
[ 34%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/cap_images.cpp.o
[ 34%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/loadsave.cpp.o
[ 34%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/lkpyramid.cpp.o
[ 34%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/utils.cpp.o
[ 34%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/window.cpp.o
[ 34%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/window_cocoa.mm.o
[ 34%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/motempl.cpp.o
[ 34%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/cap_ffmpeg.cpp.o
[ 34%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/optflowgf.cpp.o
[ 34%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/simpleflow.cpp.o
In file included from /Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg.cpp:45:
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:71:6: error: "libswscale is necessary to build the newer
      OpenCV ffmpeg wrapper"
    #error "libswscale is necessary to build the newer OpenCV ffmpeg wrapper"
     ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:481:9: error: use of undeclared identifier
      'sws_freeContext'
        sws_freeContext(img_convert_ctx);
        ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:965:17: error: use of undeclared identifier 'SWS_BICUBIC'
                SWS_BICUBIC,
                ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:998:5: error: use of undeclared identifier 'sws_scale'
    sws_scale(
    ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:1639:46: error: use of undeclared identifier 'SWS_BICUBIC'
                                             SWS_BICUBIC,
                                             ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:1645:14: error: use of undeclared identifier 'sws_scale'
        if ( sws_scale(img_convert_ctx, input_picture->data,
             ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:1693:9: error: use of undeclared identifier
      'sws_freeContext'
        sws_freeContext(img_convert_ctx);
        ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:2290:9: warning: ignoring return value of function declared
      with warn_unused_result attribute [-Wunused-result]
        avformat_write_header(oc_, NULL);
        ^~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~
1 warning and 7 errors generated.
make[2]: *** [modules/highgui/CMakeFiles/opencv_highgui.dir/src/cap_ffmpeg.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
[ 34%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/cap_qtkit.mm.o
[ 35%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/tvl1flow.cpp.o
[ 35%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/video_init.cpp.o
[ 35%] Linking CXX shared library ../../lib/libopencv_photo.dylib
[ 35%] Built target opencv_photo
make[1]: *** [modules/highgui/CMakeFiles/opencv_highgui.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[ 35%] Linking CXX shared library ../../lib/libopencv_video.dylib
[ 35%] Built target opencv_video
make: *** [all] Error 2
paularmandsmbp.rto.be 09:51:56 ~/Downloads/opencv-2.4.13/build$ make -j8
[  2%] Built target zlib
[  6%] Built target libjpeg
[ 10%] Built target libjasper
[ 12%] Built target libpng
[ 15%] Built target opencv_core
[ 19%] Built target libtiff
[ 19%] Built target opencv_flann
[ 26%] Built target IlmImf
[ 31%] Built target opencv_imgproc
[ 33%] Built target opencv_ml
[ 33%] Built target opencv_photo
[ 34%] Built target opencv_video
[ 34%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/cap_ffmpeg.cpp.o
[ 34%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/grfmt_base.cpp.o
[ 34%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/grfmt_bmp.cpp.o
[ 35%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/grfmt_exr.cpp.o
[ 35%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/grfmt_imageio.cpp.o
[ 35%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/grfmt_jpeg.cpp.o
[ 35%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/grfmt_jpeg2000.cpp.o
[ 35%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/grfmt_png.cpp.o
In file included from /Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg.cpp:45:
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:71:6: error: "libswscale is necessary to build the newer
      OpenCV ffmpeg wrapper"
    #error "libswscale is necessary to build the newer OpenCV ffmpeg wrapper"
     ^
[ 35%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/grfmt_pxm.cpp.o
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:481:9: error: use of undeclared identifier
      'sws_freeContext'
        sws_freeContext(img_convert_ctx);
        ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:965:17: error: use of undeclared identifier 'SWS_BICUBIC'
                SWS_BICUBIC,
                ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:998:5: error: use of undeclared identifier 'sws_scale'
    sws_scale(
    ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:1639:46: error: use of undeclared identifier 'SWS_BICUBIC'
                                             SWS_BICUBIC,
                                             ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:1645:14: error: use of undeclared identifier 'sws_scale'
        if ( sws_scale(img_convert_ctx, input_picture->data,
             ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:1693:9: error: use of undeclared identifier
      'sws_freeContext'
        sws_freeContext(img_convert_ctx);
        ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:2290:9: warning: ignoring return value of function declared
      with warn_unused_result attribute [-Wunused-result]
        avformat_write_header(oc_, NULL);
        ^~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~
1 warning and 7 errors generated.
make[2]: *** [modules/highgui/CMakeFiles/opencv_highgui.dir/src/cap_ffmpeg.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [modules/highgui/CMakeFiles/opencv_highgui.dir/all] Error 2
make: *** [all] Error 2
paularmandsmbp.rto.be 09:52:36 ~/Downloads/opencv-2.4.13/build$ brew install libswscale
Error: No available formula with the name "libswscale" 
==> Searching for similarly named formulae...
Error: No similarly named formulae found.
==> Searching taps...
Error: No formulae found in taps.
==> You haven't updated Homebrew in a while.
A formula for libswscale might have been added recently.
Run `brew update` to get the latest Homebrew updates!
paularmandsmbp.rto.be 09:53:05 ~/Downloads/opencv-2.4.13/build$ brew install ffmpeg
Warning: ffmpeg-3.0.1 already installed
paularmandsmbp.rto.be 09:54:01 ~/Downloads/opencv-2.4.13/build$ brew install --upgrade ffmpeg
Warning: ffmpeg-3.0.1 already installed
paularmandsmbp.rto.be 09:54:10 ~/Downloads/opencv-2.4.13/build$ brew install --upgrade ffmpeg-dev
Error: No available formula with the name "ffmpeg-dev" 
==> Searching for similarly named formulae...
Error: No similarly named formulae found.
==> Searching taps...
Error: No formulae found in taps.
==> You haven't updated Homebrew in a while.
A formula for ffmpeg-dev might have been added recently.
Run `brew update` to get the latest Homebrew updates!
paularmandsmbp.rto.be 09:54:30 ~/Downloads/opencv-2.4.13/build$ brew uninstall lame
Uninstalling /usr/local/Cellar/lame/3.99.5... (26 files, 2M)
paularmandsmbp.rto.be 09:56:15 ~/Downloads/opencv-2.4.13/build$ brew install lame
==> Downloading https://homebrew.bintray.com/bottles/lame-3.99.5.el_capitan.bottle.1.tar.gz
######################################################################## 100.0%
==> Pouring lame-3.99.5.el_capitan.bottle.1.tar.gz
🍺  /usr/local/Cellar/lame/3.99.5: 26 files, 2M
paularmandsmbp.rto.be 09:56:30 ~/Downloads/opencv-2.4.13/build$ make -j8
[  2%] Built target zlib
[  6%] Built target libjpeg
[ 10%] Built target libjasper
[ 12%] Built target libpng
[ 16%] Built target libtiff
[ 19%] Built target opencv_core
[ 26%] Built target IlmImf
[ 26%] Built target opencv_flann
[ 28%] Built target opencv_ml
[ 33%] Built target opencv_imgproc
[ 33%] Built target opencv_photo
[ 34%] Built target opencv_video
[ 34%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/cap_ffmpeg.cpp.o
[ 34%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/grfmt_sunras.cpp.o
[ 34%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/bitstrm.cpp.o
[ 34%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/grfmt_tiff.cpp.o
In file included from /Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg.cpp:45:
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:71:6: error: "libswscale is necessary to build the newer
      OpenCV ffmpeg wrapper"
    #error "libswscale is necessary to build the newer OpenCV ffmpeg wrapper"
     ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:481:9: error: use of undeclared identifier
      'sws_freeContext'
        sws_freeContext(img_convert_ctx);
        ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:965:17: error: use of undeclared identifier 'SWS_BICUBIC'
                SWS_BICUBIC,
                ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:998:5: error: use of undeclared identifier 'sws_scale'
    sws_scale(
    ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:1639:46: error: use of undeclared identifier 'SWS_BICUBIC'
                                             SWS_BICUBIC,
                                             ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:1645:14: error: use of undeclared identifier 'sws_scale'
        if ( sws_scale(img_convert_ctx, input_picture->data,
             ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:1693:9: error: use of undeclared identifier
      'sws_freeContext'
        sws_freeContext(img_convert_ctx);
        ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:2290:9: warning: ignoring return value of function declared
      with warn_unused_result attribute [-Wunused-result]
        avformat_write_header(oc_, NULL);
        ^~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~
1 warning and 7 errors generated.
make[2]: *** [modules/highgui/CMakeFiles/opencv_highgui.dir/src/cap_ffmpeg.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [modules/highgui/CMakeFiles/opencv_highgui.dir/all] Error 2
make: *** [all] Error 2
paularmandsmbp.rto.be 09:56:39 ~/Downloads/opencv-2.4.13/build$ sudo brew link lame
Password:
Error: Cowardly refusing to 'sudo brew link'
You can use brew with sudo, but only if the brew executable is owned by root.
However, this is both not recommended and completely unsupported so do so at
your own risk.
paularmandsmbp.rto.be 09:56:45 ~/Downloads/opencv-2.4.13/build$ make -j8
[  2%] Built target zlib
[  6%] Built target libjpeg
[ 10%] Built target libjasper
[ 12%] Built target libpng
[ 16%] Built target opencv_core
[ 19%] Built target libtiff
[ 19%] Built target opencv_flann
[ 26%] Built target IlmImf
[ 28%] Built target opencv_ml
[ 33%] Built target opencv_imgproc
[ 33%] Built target opencv_photo
[ 33%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/cap_ffmpeg.cpp.o
[ 34%] Built target opencv_video
In file included from /Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg.cpp:45:
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:71:6: error: "libswscale is necessary to build the newer
      OpenCV ffmpeg wrapper"
    #error "libswscale is necessary to build the newer OpenCV ffmpeg wrapper"
     ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:481:9: error: use of undeclared identifier
      'sws_freeContext'
        sws_freeContext(img_convert_ctx);
        ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:965:17: error: use of undeclared identifier 'SWS_BICUBIC'
                SWS_BICUBIC,
                ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:998:5: error: use of undeclared identifier 'sws_scale'
    sws_scale(
    ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:1639:46: error: use of undeclared identifier 'SWS_BICUBIC'
                                             SWS_BICUBIC,
                                             ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:1645:14: error: use of undeclared identifier 'sws_scale'
        if ( sws_scale(img_convert_ctx, input_picture->data,
             ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:1693:9: error: use of undeclared identifier
      'sws_freeContext'
        sws_freeContext(img_convert_ctx);
        ^
/Users/paularmand/Downloads/opencv-2.4.13/modules/highgui/src/cap_ffmpeg_impl.hpp:2290:9: warning: ignoring return value of function declared
      with warn_unused_result attribute [-Wunused-result]
        avformat_write_header(oc_, NULL);
        ^~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~
1 warning and 7 errors generated.
make[2]: *** [modules/highgui/CMakeFiles/opencv_highgui.dir/src/cap_ffmpeg.cpp.o] Error 1
make[1]: *** [modules/highgui/CMakeFiles/opencv_highgui.dir/all] Error 2
make: *** [all] Error 2
paularmandsmbp.rto.be 09:56:50 ~/Downloads/opencv-2.4.13/build$ cmake -G "Unix Makefiles" ..
-- Looking for linux/videodev.h
-- Looking for linux/videodev.h - not found
-- Looking for linux/videodev2.h
-- Looking for linux/videodev2.h - not found
-- Looking for sys/videoio.h
-- Looking for sys/videoio.h - not found
-- Looking for libavformat/avformat.h
-- Looking for libavformat/avformat.h - found
-- Looking for ffmpeg/avformat.h
-- Looking for ffmpeg/avformat.h - not found
-- Assume that non-module dependency is available: -framework OpenCL (for module opencv_ocl)
-- 
-- General configuration for OpenCV 2.4.13 =====================================
--   Version control:               unknown
-- 
--   Platform:
--     Host:                        Darwin 15.0.0 x86_64
--     CMake:                       3.5.2
--     CMake generator:             Unix Makefiles
--     CMake build tool:            /usr/bin/make
--     Configuration:               Release
-- 
--   C/C++:
--     Built as dynamic libs?:      YES
--     C++ Compiler:                /Library/Developer/CommandLineTools/usr/bin/c++  (ver 7.3.0.7030029)
--     C++ flags (Release):         -fsigned-char -W -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-array-bounds -fdiagnostics-show-option -Wno-long-long -Wno-semicolon-before-method-body -fno-omit-frame-pointer -msse -msse2 -msse3 -O3 -DNDEBUG  -DNDEBUG
--     C++ flags (Debug):           -fsigned-char -W -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-array-bounds -fdiagnostics-show-option -Wno-long-long -Wno-semicolon-before-method-body -fno-omit-frame-pointer -msse -msse2 -msse3 -g  -O0 -DDEBUG -D_DEBUG
--     C Compiler:                  /Library/Developer/CommandLineTools/usr/bin/cc
--     C flags (Release):           -fsigned-char -W -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-array-bounds -fdiagnostics-show-option -Wno-long-long -Wno-semicolon-before-method-body -fno-omit-frame-pointer -msse -msse2 -msse3 -O3 -DNDEBUG  -DNDEBUG
--     C flags (Debug):             -fsigned-char -W -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-array-bounds -fdiagnostics-show-option -Wno-long-long -Wno-semicolon-before-method-body -fno-omit-frame-pointer -msse -msse2 -msse3 -g  -O0 -DDEBUG -D_DEBUG
--     Linker flags (Release):
--     Linker flags (Debug):
--     Precompiled headers:         NO
-- 
--   OpenCV modules:
--     To be built:                 core flann imgproc highgui features2d calib3d ml video legacy objdetect photo gpu ocl nonfree contrib python stitching superres ts videostab
--     Disabled:                    world
--     Disabled by dependency:      -
--     Unavailable:                 androidcamera dynamicuda java viz
-- 
--   GUI: 
--     QT:                          NO
--     Cocoa:                       YES
--     OpenGL support:              NO
--     VTK support:                 NO
-- 
--   Media I/O: 
--     ZLib:                        build (ver 1.2.7)
--     JPEG:                        build (ver 62)
--     PNG:                         build (ver 1.5.12)
--     TIFF:                        build (ver 42 - 4.0.2)
--     JPEG 2000:                   build (ver 1.900.1)
--     OpenEXR:                     build (ver 1.7.1)
-- 
--   Video I/O:
--     DC1394 1.x:                  NO
--     DC1394 2.x:                  NO
--     FFMPEG:                      YES
--       codec:                     NO
--       format:                    NO
--       util:                      NO
--       swscale:                   NO
--       resample:                  NO
--       gentoo-style:              YES
--     GStreamer:                   NO
--     OpenNI:                      NO
--     OpenNI PrimeSensor Modules:  NO
--     PvAPI:                       NO
--     GigEVisionSDK:               NO
--     QuickTime:                   NO
--     QTKit:                       YES
--     V4L/V4L2:                    NO/NO
--     XIMEA:                       NO
-- 
--   Other third-party libraries:
--     Use IPP:                     NO
--     Use Eigen:                   NO
--     Use TBB:                     NO
--     Use OpenMP:                  NO
--     Use GCD                      YES
--     Use Concurrency              NO
--     Use C=:                      NO
--     Use Cuda:                    NO
--     Use OpenCL:                  YES
-- 
--   OpenCL:
--     Version:                     static
--     libraries:                   -framework OpenCL
--     Use AMD FFT:                 NO
--     Use AMD BLAS:                NO
-- 
--   Python:
--     Interpreter:                 /usr/bin/python (ver 2.7.10)
--     Libraries:                   /usr/lib/libpython2.7.dylib (ver 2.7.10)
--     numpy:                       /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/core/include (ver 1.8.0rc1)
--     packages path:               lib/python2.7/site-packages
-- 
--   Java:
--     ant:                         NO
--     JNI:                         /Library/Java/JavaVirtualMachines/jdk1.8.0_91.jdk/Contents/Home/include /Library/Java/JavaVirtualMachines/jdk1.8.0_91.jdk/Contents/Home/include/darwin /Library/Java/JavaVirtualMachines/jdk1.8.0_91.jdk/Contents/Home/include
--     Java tests:                  NO
-- 
--   Documentation:
--     Build Documentation:         NO
--     Sphinx:                      NO
--     PdfLaTeX compiler:           NO
--     Doxygen:                     NO
-- 
--   Tests and samples:
--     Tests:                       YES
--     Performance tests:           YES
--     C/C++ Examples:              NO
-- 
--   Install path:                  /usr/local
-- 
--   cvconfig.h is in:              /Users/paularmand/Downloads/opencv-2.4.13/build
-- -----------------------------------------------------------------
-- 
CMake Warning at cmake/OpenCVPackaging.cmake:23 (message):
  CPACK_PACKAGE_VERSION does not match version provided by version.hpp
  header!
Call Stack (most recent call first):
  CMakeLists.txt:1105 (include)


-- Configuring done
-- Generating done
-- Build files have been written to: /Users/paularmand/Downloads/opencv-2.4.13/build
paularmandsmbp.rto.be 09:57:01 ~/Downloads/opencv-2.4.13/build$ pip install cv2
Collecting cv2
  Could not find a version that satisfies the requirement cv2 (from versions: )
No matching distribution found for cv2
You are using pip version 8.1.2, however version 9.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
paularmandsmbp.rto.be 09:58:36 ~/Downloads/opencv-2.4.13/build$ pip install --upgrade pip
Collecting pip
  Using cached pip-9.0.1-py2.py3-none-any.whl
Installing collected packages: pip
  Found existing installation: pip 8.1.2
    Uninstalling pip-8.1.2:
Exception:
Traceback (most recent call last):
  File "/Library/Python/2.7/site-packages/pip-8.1.2-py2.7.egg/pip/basecommand.py", line 215, in main
    status = self.run(options, args)
  File "/Library/Python/2.7/site-packages/pip-8.1.2-py2.7.egg/pip/commands/install.py", line 317, in run
    prefix=options.prefix_path,
  File "/Library/Python/2.7/site-packages/pip-8.1.2-py2.7.egg/pip/req/req_set.py", line 736, in install
    requirement.uninstall(auto_confirm=True)
  File "/Library/Python/2.7/site-packages/pip-8.1.2-py2.7.egg/pip/req/req_install.py", line 742, in uninstall
    paths_to_remove.remove(auto_confirm)
  File "/Library/Python/2.7/site-packages/pip-8.1.2-py2.7.egg/pip/req/req_uninstall.py", line 115, in remove
    renames(path, new_path)
  File "/Library/Python/2.7/site-packages/pip-8.1.2-py2.7.egg/pip/utils/__init__.py", line 267, in renames
    shutil.move(old, new)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/shutil.py", line 300, in move
    rmtree(src)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/shutil.py", line 247, in rmtree
    rmtree(fullname, ignore_errors, onerror)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/shutil.py", line 252, in rmtree
    onerror(os.remove, fullname, sys.exc_info())
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/shutil.py", line 250, in rmtree
    os.remove(fullname)
OSError: [Errno 13] Permission denied: '/Library/Python/2.7/site-packages/pip-8.1.2-py2.7.egg/EGG-INFO/dependency_links.txt'
You are using pip version 8.1.2, however version 9.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
paularmandsmbp.rto.be 09:58:56 ~/Downloads/opencv-2.4.13/build$ sudo pip install --upgrade pip
The directory '/Users/paularmand/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/paularmand/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting pip
  Downloading pip-9.0.1-py2.py3-none-any.whl (1.3MB)
    100% |████████████████████████████████| 1.3MB 805kB/s 
Installing collected packages: pip
  Found existing installation: pip 8.1.2
    Uninstalling pip-8.1.2:
      Successfully uninstalled pip-8.1.2
Successfully installed pip-9.0.1
paularmandsmbp.rto.be 09:59:02 ~/Downloads/opencv-2.4.13/build$ pip install cv2
Collecting cv2
  Could not find a version that satisfies the requirement cv2 (from versions: )
No matching distribution found for cv2
paularmandsmbp.rto.be 09:59:05 ~/Downloads/opencv-2.4.13/build$ pip install opencv
Collecting opencv
  Could not find a version that satisfies the requirement opencv (from versions: )
No matching distribution found for opencv
paularmandsmbp.rto.be 09:59:16 ~/Downloads/opencv-2.4.13/build$ pip install cv
Collecting cv
  Could not find a version that satisfies the requirement cv (from versions: )
No matching distribution found for cv
paularmandsmbp.rto.be 09:59:28 ~/Downloads/opencv-2.4.13/build$ pip install pyopencv
Collecting pyopencv
  Could not find a version that satisfies the requirement pyopencv (from versions: 2.0.wr1.0.1-demo, 2.0.wr1.0.1, 2.0.wr1.1.0, 2.1.0.wr1.0.0, 2.1.0.wr1.0.1, 2.1.0.wr1.0.2, 2.1.0.wr1.1.0, 2.1.0.wr1.2.0)
No matching distribution found for pyopencv
paularmandsmbp.rto.be 10:00:36 ~/Downloads/opencv-2.4.13/build$ pip install pyopencv
paularmandsmbp.rto.be 10:24:21 ~/Downloads/opencv-2.4.13/build$ cd ~/dev/ares/
.DS_Store    .git/        .gitignore   .gitmodules  .idea/       LICENSE      README.md    docs/        hw/          sw/
paularmandsmbp.rto.be 10:24:21 ~/Downloads/opencv-2.4.13/build$ cd ~/dev/ares/
paularmandsmbp.rto.be 10:24:45 (master) ~/dev/ares$ cd ~/dev/ares/
.DS_Store    .git/        .gitignore   .gitmodules  .idea/       LICENSE      README.md    docs/        hw/          sw/
paularmandsmbp.rto.be 10:24:45 (master) ~/dev/ares$ cd ~/dev/ares
paularmandsmbp.rto.be 10:26:39 (master) ~/dev/ares$ ll
total 48
 0 drwxr-xr-x  12 paularmand  staff   408B Nov 18 01:22 .
 0 drwxr-xr-x   7 paularmand  staff   238B Nov 23 21:48 ..
16 -rw-r--r--@  1 paularmand  staff   6.0K Nov  9 21:04 .DS_Store
 0 drwxr-xr-x  17 paularmand  staff   578B Nov 23 22:26 .git
 8 -rw-r--r--   1 paularmand  staff   1.0K Nov 12 09:51 .gitignore
 8 -rw-r--r--   1 paularmand  staff   131B Nov 16 21:13 .gitmodules
 0 drwxr-xr-x   9 paularmand  staff   306B Nov 23 21:52 .idea
 8 -rw-r--r--   1 paularmand  staff   1.0K Nov  9 19:47 LICENSE
 8 -rw-r--r--   1 paularmand  staff   876B Nov 18 00:42 README.md
 0 drwxr-xr-x   4 paularmand  staff   136B Nov 11 22:39 docs
 0 drwxr-xr-x   3 paularmand  staff   102B Nov 11 20:18 hw
 0 drwxr-xr-x   5 paularmand  staff   170B Nov 12 09:43 sw
paularmandsmbp.rto.be 10:26:40 (master) ~/dev/ares$ ssh pi@192.168.1.138

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Nov 23 20:23:32 2016 from paularmandsmbp
cd(cv) pi@raspberrypi:~ $ cd engine/scratchpad/
(failed reverse-i-search)`scp ': cd engine/^Cratchpad/
(cv) pi@raspberrypi:~/engine/scratchpad $ scp pi@192.168.1.138:/home/pi/engine/scratchpad/foo_contours.jpg .
The authenticity of host '192.168.1.138 (192.168.1.138)' can't be established.
ECDSA key fingerprint is 8b:52:cf:af:d5:e2:9a:d5:2f:5d:e5:ef:95:66:00:2c.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.1.138' (ECDSA) to the list of known hosts.
pi@192.168.1.138's password: 
foo_contours.jpg                                                                                           100%  153KB 153.1KB/s   00:00    
(cv) pi@raspberrypi:~/engine/scratchpad $ open foo_contours.jpg 
Couldn't get a file descriptor referring to the console
(cv) pi@raspberrypi:~/engine/scratchpad $ 
(cv) pi@raspberrypi:~/engine/scratchpad $ ll
total 580
  4 drwxr-xr-x 2 pi pi   4096 Nov 23 21:36 .
  4 drwxr-xr-x 3 pi pi   4096 Nov 23 20:23 ..
404 -rw-r--r-- 1 pi pi 411918 Nov 23 21:36 foo.jpg
156 -rw-r--r-- 1 pi pi 156789 Nov 23 21:37 foo_contours.jpg
  4 -rw-r--r-- 1 pi pi    201 Nov 23 20:23 test1.py
  4 -rw-r--r-- 1 pi pi    898 Nov 23 20:23 test2.py
  4 -rw-r--r-- 1 pi pi    565 Nov 23 21:36 test3_contours.py
(cv) pi@raspberrypi:~/engine/scratchpad $ exit
logout
Connection to 192.168.1.138 closed.
paularmandsmbp.rto.be 10:37:52 (master) ~/dev/ares$ scp pi@192.168.1.138:/home/pi/engine/scratchpad/foo_contours.jpg .
foo_contours.jpg                                                                                           100%  153KB 153.1KB/s   00:00    
paularmandsmbp.rto.be 10:38:00 (master) ~/dev/ares$ open foo_contours.jpg 
paularmandsmbp.rto.be 10:38:05 (master) ~/dev/ares$ scp pi@192.168.1.138:/home/pi/engine/scratchpad/foo_contours.jpg .
foo_contours.jpg                                                                                           100%  198KB 197.6KB/s   00:00    
paularmandsmbp.rto.be 11:05:34 (master) ~/dev/ares$ open foo_contours.jpg 
paularmandsmbp.rto.be 11:05:35 (master) ~/dev/ares$ cd ~/Downloads/
paularmandsmbp.rto.be 11:33:43 ~/Downloads$ wget https://raw.githubusercontent.com/diy-electronics/raspberrypi-b-plus-case/master/raspberrypi-b-plus-case.svg
--2016-11-23 23:33:47--  https://raw.githubusercontent.com/diy-electronics/raspberrypi-b-plus-case/master/raspberrypi-b-plus-case.svg
Resolving raw.githubusercontent.com... 151.101.60.133
Connecting to raw.githubusercontent.com|151.101.60.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 288536 (282K) [text/plain]
Saving to: 'raspberrypi-b-plus-case.svg'

raspberrypi-b-plus-case.svg         100%[================================================================>] 281.77K  1.67MB/s    in 0.2s    

2016-11-23 23:33:58 (1.67 MB/s) - 'raspberrypi-b-plus-case.svg' saved [288536/288536]

paularmandsmbp.rto.be 11:33:58 ~/Downloads$ open raspberrypi-b-plus-case.svg 
paularmandsmbp.rto.be 11:34:11 ~/Downloads$ ll
total 27263192
      0 drwx------+ 266 paularmand  staff   8.8K Nov 24 13:37 .
      0 drwxr-xr-x+  67 paularmand  staff   2.2K Nov 24 09:31 ..
     80 -rw-r--r--@   1 paularmand  staff    36K Nov 24 13:37 .DS_Store
    256 -rw-r--r--@   1 paularmand  staff   127K Oct 17 15:16 02-MFF_Taskforce_171015.pdf
    256 -rw-r--r--@   1 paularmand  staff   126K Oct 23 10:43 1037_001-2.pdf
    208 -rw-r--r--@   1 paularmand  staff   104K Apr 26  2016 1080.jpeg
    832 -rw-r--r--@   1 paularmand  staff   415K Jun 23 10:55 1311.1704v3 (1).pdf
    832 -rw-r--r--@   1 paularmand  staff   415K Jun 23 10:04 1311.1704v3.pdf
  39952 -rw-r--r--    1 paularmand  staff    20M Apr 26  2016 2016-04-26_1338.swf
  40200 -rw-r--r--@   1 paularmand  staff    20M Jun 22 10:25 2016-06-15_EBU_RecSys_Yle_status_rel.pdf
8493056 -rw-r--r--    1 paularmand  staff   4.0G Sep 23 09:44 2016-09-23-raspbian-jessie.img
2967104 -rw-r--r--@   1 paularmand  staff   1.4G Nov 16 20:16 2016-09-23-raspbian-jessie.zip
   3064 -rw-r--r--@   1 paularmand  staff   1.5M Mar 10  2016 20160311_usecases.key
  35152 -rw-r--r--@   1 paularmand  staff    17M May 26  2016 20160525_224121.mp4
     96 -rw-r--r--@   1 paularmand  staff    47K Jul 12 14:46 20160629_De-Morgen_p-7_Budget-voor-externe-consultants-VRT.pdf
      0 -rw-r--r--    1 paularmand  staff     0B Aug 11 10:05 20160810_comscore_dump.gz
     96 -rw-r--r--@   1 paularmand  staff    47K Oct 19 15:07 20160908_Trends-Trends_p-88_Groter-bereik-dan-televisie-in-primetime (1).pdf
   5608 -rw-r--r--@   1 paularmand  staff   2.7M Sep 19 08:45 20160917_De-Tijd_p-18-19.pdf
  31736 -rw-r--r--@   1 paularmand  staff    15M Nov 16 09:47 20161115 slides voor Luk.pptx
    152 -rw-r--r--@   1 paularmand  staff    72K May 10  2016 24083084153-505172038-ticket.pdf
    792 -rw-r--r--@   1 paularmand  staff   394K Sep 12 13:08 30b-esp-touch_user_guide_en_v1.1_20160412_0.pdf
      0 drwx------@   7 paularmand  staff   238B Jul 15 15:27 369875_VRT Appreciation & Reach_PANEL_ALL_20160701_CLEAN
   3288 -rw-r--r--@   1 paularmand  staff   1.6M Jul 15 09:05 369875_VRT Appreciation & Reach_PANEL_ALL_20160701_CLEAN.zip
    592 -rw-r--r--@   1 paularmand  staff   292K Apr 26  2016 5789596316 (1).pdf
    592 -rw-r--r--@   1 paularmand  staff   292K Apr 26  2016 5789596316.pdf
    592 -rw-r--r--@   1 paularmand  staff   295K Jun 19 20:23 5905887316.pdf
    664 -rw-r--r--@   1 paularmand  staff   329K Sep 18 12:59 5991734116.pdf
    656 -rw-r--r--@   1 paularmand  staff   327K Sep 18 12:59 6062103316 (1).pdf
    656 -rw-r--r--@   1 paularmand  staff   327K Sep 18 12:58 6062103316.pdf
      8 -rw-r--r--@   1 paularmand  staff   937B Aug 24 00:36 60993.svg
    664 -rw-r--r--@   1 paularmand  staff   330K Oct 18 20:30 6145184216.pdf
   3384 -rw-r--r--@   1 paularmand  staff   1.7M Nov  1 09:39 6357136483338460001831742012.zip
    328 -rw-r--r--@   1 paularmand  staff   161K Jun  8 13:42 A4017539-080616-134207.PDF
    328 -rw-r--r--@   1 paularmand  staff   161K Jun  5 21:18 A4637619-280416-092625.PDF
   1616 -rw-r--r--@   1 paularmand  staff   806K May 16  2016 AdobeReader_11_en_a_install.dmg
   1632 -rw-r--r--@   1 paularmand  staff   814K May 16  2016 AdobeReader_dc_en_a_install.dmg
    296 -rw-r--r--@   1 paularmand  staff   146K Jun 19 22:07 Afbeelding (2).jpg
    536 -rw-r--r--@   1 paularmand  staff   265K Jun 19 22:07 Afbeelding.jpg
     80 -rw-r--r--@   1 paularmand  staff    38K Oct  6 21:11 BE31652846545455_2016_1_3_1475781063068.pdf
    376 -rw-r--r--@   1 paularmand  staff   185K Jun 13 13:17 Centriphone-v08.stl
    424 -rw-r--r--@   1 paularmand  staff   212K Jun 21 11:33 Centripro-v01.stl
   6304 -rw-r--r--@   1 paularmand  staff   3.1M Jun  7 16:12 Cisco_WebEx_Add-On.dmg
  48488 -rw-r--r--@   1 paularmand  staff    24M Apr 26  2016 CleverLions 1080p (Video Only).mp4
      0 drwxr-xr-x@  27 paularmand  staff   918B May  3  2016 CustomDimensions
   3200 -rw-r--r--@   1 paularmand  staff   1.6M May  3  2016 CustomDimensions-0.1.4.zip
    632 -rw-r--r--@   1 paularmand  staff   312K Jul  4 17:23 Datacenter_Projectleider_:_Chef_de_projets_Datacenter.pdf
 219560 -rw-r--r--@   1 paularmand  staff   107M Nov  2 20:17 Docker.dmg
  57744 -rw-r--r--@   1 paularmand  staff    28M Sep  7 18:34 DogBasePose.ai
   1520 -rw-r--r--@   1 paularmand  staff   759K May  3  2016 E1602121946.pdf
   1184 -rw-r--r--@   1 paularmand  staff   589K Oct 18 20:23 E1603671000.pdf
    368 -rw-r--r--@   1 paularmand  staff   180K Oct 18 21:30 Een nieuwe waterfactuur.pdf
    216 -rw-r--r--@   1 paularmand  staff   107K Jun  9 20:44 Fault code sheet  - August 2009.pdf
  22920 -rw-r--r--@   1 paularmand  staff    11M Mar  9  2016 GfK_VRT Mediakids 7.pptx
  97304 -rw-r--r--@   1 paularmand  staff    48M Jun 15 10:33 GoogleEarth-Pro-Intel-7.1.5.1557.dmg
  97304 -rw-r--r--@   1 paularmand  staff    48M Jun 15 10:37 GoogleEarthProMac-Intel.dmg
   5400 -rw-r--r--@   1 paularmand  staff   2.6M Apr 26  2016 HEARTBEAT_01.mp4
   5504 -rw-r--r--@   1 paularmand  staff   2.7M Apr 27  2016 HEARTBEAT_02_converted.mp4
   1256 -rw-r--r--@   1 paularmand  staff   626K Jun  6 21:47 Habit_logo_2.eps
     16 -rw-r--r--@   1 paularmand  staff   7.5K Jun  6 22:27 Habit_logo_2.png
   1416 -rw-r--r--@   1 paularmand  staff   704K Apr 25  2016 IMG_20151231_115351.jpg
   2856 -rw-r--r--@   1 paularmand  staff   1.4M May 11  2016 IMG_20160507_163620.jpg
   2352 -rw-r--r--@   1 paularmand  staff   1.1M May 11  2016 IMG_20160507_163702.jpg
   2544 -rw-r--r--@   1 paularmand  staff   1.2M May 11  2016 IMG_20160507_163718.jpg
   5008 -rw-r--r--@   1 paularmand  staff   2.4M May 11  2016 IMG_20160507_173146.jpg
   3280 -rw-r--r--@   1 paularmand  staff   1.6M Jun 12 22:30 IMG_20160601_171827_01.jpg
   2832 -rw-r--r--@   1 paularmand  staff   1.4M Jun 12 22:30 IMG_20160601_172308.jpg
   3000 -rw-r--r--@   1 paularmand  staff   1.5M Jun 12 22:36 IMG_20160605_091434.jpg
   2160 -rw-r--r--@   1 paularmand  staff   1.1M Oct  6 22:49 IMG_20160810_204551.jpg
 132400 -rw-r--r--@   1 paularmand  staff    65M Aug 23 22:30 Inkscape-0.91-1-x11-10.5-i386_1.dmg
    328 -rw-r--r--@   1 paularmand  staff   163K Aug 30 11:36 Job+Description+-+Linux+and+Open+Source+Embedded+Software+developers.pdf
  88992 -rw-r--r--@   1 paularmand  staff    43M Nov  2 20:25 Kitematic-Mac.zip
   1320 -rw-r--r--@   1 paularmand  staff   659K Sep 13 13:54 Klasbord-Uitnodiging.pdf
  19456 -rw-r--r--@   1 paularmand  staff   9.5M Jun 28 13:14 LWAPluginInstaller.pkg
     56 -rw-r--r--@   1 paularmand  staff    25K Sep 26 09:24 Label overview.xlsx
 412784 -rw-r--r--@   1 paularmand  staff   202M Jun 27 10:22 LibreOffice_5.1.4_MacOS_x86-64.dmg
    216 -rw-r--r--@   1 paularmand  staff   108K Aug 30 10:50 MEDIVRTI002.xls
   1232 -rw-r--r--@   1 paularmand  staff   613K Aug 11 09:52 Mail Attachment.eml
    328 -rw-r--r--@   1 paularmand  staff   162K May 20  2016 MatrixFactorizationALS.pdf
  23048 -rw-r--r--@   1 paularmand  staff    11M May 23  2016 Mike Frampton-Mastering Apache Spark-Packt Publishing - ebooks Account (2015).pdf
   8400 -rw-r--r--@   1 paularmand  staff   4.1M May 10  2016 Mohammed Guller-Big Data Analytics with Spark_ A Practitioner's Guide to Using Spark for Large Scale Data Analysis-Apress (2015).pdf
  12352 -rw-r--r--@   1 paularmand  staff   6.0M Jun 29 17:35 NaturalReader+Free+4.0.pkg
  46904 -rw-r--r--@   1 paularmand  staff    23M Aug 24 14:17 Nederlandse Persoonlijke Omroep (full).pdf
   1664 -rw-r--r--@   1 paularmand  staff   830K Aug 30 09:45 NetWiSE_-_Cut_Sheet_V1.1.pdf
    304 -rw-r--r--@   1 paularmand  staff   148K Jun 17 12:52 ORDERBEVESTIGING_00143791.pdf
    832 -rw-r--r--@   1 paularmand  staff   415K Oct  3 10:21 Office plan2.pdf
     16 -rw-r--r--@   1 paularmand  staff   4.1K Jun  6 23:15 PastedGraphic-1.png
 241744 -rw-r--r--@   1 paularmand  staff   118M Nov 24 13:08 Providence-20161124T120326Z.zip
  33824 -rw-r--r--@   1 paularmand  staff    17M Aug 17 16:17 Providence_CCIII_filmpje-1.mp4
  33824 -rw-r--r--@   1 paularmand  staff    17M Jun  6 12:55 Providence_CCIII_filmpje.mp4
 120960 -rw-r--r--@   1 paularmand  staff    59M Jun  6 12:55 Providence_screencast.mov
      0 drwxrwxrwx@   8 paularmand  staff   272B Aug 18  2014 Raspberry_Pi_B_Case
    208 -rw-r--r--@   1 paularmand  staff   101K Nov 23 23:28 Raspberry_Pi_B_Case.zip
     48 -rw-r--r--@   1 paularmand  staff    20K Sep 13 13:51 Recht om te vertegenwoordigen - Vlaamseoverheid (1).docx
     48 -rw-r--r--@   1 paularmand  staff    20K Sep 13 13:42 Recht om te vertegenwoordigen - Vlaamseoverheid.docx
    208 -rw-r--r--@   1 paularmand  staff   101K Sep 22 10:11 Release_Notes-JS-API-4.1412.05.pdf
    376 -rw-r--r--@   1 paularmand  staff   187K Jun 23 10:51 Rendle2010FM.pdf
     88 -rw-r--r--@   1 paularmand  staff    40K Jun 19 22:02 SA1025931216-250516-112231.PDF
     80 -rw-r--r--@   1 paularmand  staff    38K May  3  2016 SA1025931216-280416-103550.PDF
    344 -rw-r--r--@   1 paularmand  staff   170K May 23  2016 SN_2283_20160524_CAUBERGHE_VEROLINE.pdf
    344 -rw-r--r--@   1 paularmand  staff   171K May 26 22:50 SN_2283_20160527_VERHAEGEN_PAULARMAND.pdf
     80 -rw-r--r--@   1 paularmand  staff    37K Aug  5 10:16 SPJ825931216-260716-104906.PDF
3099864 -rw-r--r--@   1 paularmand  staff   1.5G Jul 15 11:24 SPSS_Statistics_24_mac.dmg
   2608 -rw-r--r--@   1 paularmand  staff   1.3M Apr 25  2016 SandboxFiches_04_250416.pdf
    792 -rw-r--r--@   1 paularmand  staff   394K Jun  6 23:15 Schermafbeelding 2016-06-06 om 22.24.15.png
    232 -rw-r--r--@   1 paularmand  staff   114K May 13  2016 Screenshot 2016-05-13 08.58.49.png
    136 -rw-r--r--@   1 paularmand  staff    68K May 13  2016 Screenshot 2016-05-13 09.01.52.png
      0 drwxr-xr-x@   5 paularmand  staff   170B Nov  1 09:39 Search Tool V1.0.0.3
 131432 -rw-r--r--@   1 paularmand  staff    64M Oct 27 10:05 Slack-2.3.0-macOS.zip
  15408 -rw-r--r--@   1 paularmand  staff   7.5M Jun  6 23:21 SmartOcto1VRT.mov
 103568 -rw-r--r--@   1 paularmand  staff    51M Oct  7 09:41 SourceTree_2.3.1 (1).zip
 103568 -rw-r--r--@   1 paularmand  staff    51M Oct  3 17:57 SourceTree_2.3.1.zip
    840 -rw-r--r--@   1 paularmand  staff   420K Oct 20 13:26 Streaming_Tag-JS-API-Digital_Analytix-EU.pdf
   3520 -rw-r--r--@   1 paularmand  staff   1.7M Jun  6 10:13 TNO_DAMIAN_Lisbon_ICT2015.pdf
     80 -rw-r--r--@   1 paularmand  staff    38K Aug 30 10:08 Test overeenkomst DMP_22082016_FIN[1].docx
    920 -rw-r--r--@   1 paularmand  staff   458K Oct 25 15:34 Thuis 2930 def.rtf
   4112 -rw-r--r--@   1 paularmand  staff   2.0M May 16  2016 Time registration via CAMIS_EN.docx
      0 drwxr-xr-x@  16 paularmand  staff   544B Nov 10 13:35 Topdown_vehicle_sprites_pack
   1016 -rw-r--r--@   1 paularmand  staff   508K Nov  9 23:15 Topdown_vehicle_sprites_pack_Unluckystudio.zip
     72 -rw-r--r--@   1 paularmand  staff    34K Jun 16 11:36 Untitled.pdf
   1296 -rw-r--r--@   1 paularmand  staff   648K Oct 25 15:47 V00050004.XIF
     80 -rw-r--r--@   1 paularmand  staff    37K Jun 27 11:02 VRT Morgen.pdf
      0 drwxr-x---    3 paularmand  admin   102B Apr 22  2016 VRT perso.tblk
    920 -rw-r--r--@   1 paularmand  staff   459K Sep 19 09:06 VRT00102_1_AE_CVGert_Nelissen.pdf
     40 -rw-r--r--@   1 paularmand  staff    16K Sep 19 09:06 VRT00102_1_BigBoards_DaanGerits (1).pdf
    192 -rw-r--r--@   1 paularmand  staff    96K Sep 16 15:35 VRT00102_1_CegekaGroep_CharlesEric-Cegeka.docx
    208 -rw-r--r--@   1 paularmand  staff   101K Sep 16 15:17 VRT00102_1_CegekaGroep_GeertVanLandeghemCegeka.docx
    192 -rw-r--r--@   1 paularmand  staff    94K Sep 16 15:17 VRT00102_1_CegekaGroep_KjellMoensCegeka.docx
    200 -rw-r--r--@   1 paularmand  staff    99K Sep 14 09:36 VRT00102_1_Cotrain_KerremansPhilippe-ENG032016.doc
    112 -rw-r--r--@   1 paularmand  staff    55K Sep 19 09:06 VRT00102_1_Cronos_CV-Alexander_VanLoock.pdf
   1064 -rw-r--r--@   1 paularmand  staff   530K Sep 16 15:07 VRT00102_1_Cronos_CVRobertGibbon.pdf
   1184 -rw-r--r--@   1 paularmand  staff   590K Sep 16 15:01 VRT00102_1_Cronos_CVRonVanderhoydonks.pdf
    760 -rw-r--r--@   1 paularmand  staff   377K Sep 16 13:44 VRT00102_1_Infocura_CVDDE2016.pdf
    560 -rw-r--r--@   1 paularmand  staff   280K Sep 16 13:07 VRT00102_1_LacoInformationServices_CVAndreasSchelfhout.docx
     88 -rw-r--r--@   1 paularmand  staff    42K Sep 16 13:07 VRT00102_1_MarlinGreenLimited_JorisvandenBorre_BigDataArchitect_MarlinGreen_CV.docx
    280 -rw-r--r--@   1 paularmand  staff   139K Sep 19 09:06 VRT00102_1_TenForce_EUROPASSCVAadVersteden.doc
      8 -rw-r--r--@   1 paularmand  staff   1.9K Sep 28 15:54 VRTVPN.tblk.zip
  95968 -rw-r--r--@   1 paularmand  staff    47M Jun 15 21:58 VRT_Centriphone_maidenvoyage.mp4
  31736 -rw-r--r--@   1 paularmand  staff    15M Jun  1 23:33 VRTcoachingPP.pptx
 212104 -rw-r--r--@   1 paularmand  staff   104M Jun  6 23:01 VRTworkshopEBUMDM.key
 230112 -rw-r--r--@   1 paularmand  staff   112M Jun  7 11:23 VRTworkshopEBUMDMv2.key
 152032 -rw-r--r--@   1 paularmand  staff    74M Jul 15 10:45 XQuartz-2.7.9.dmg
      0 drwxr-xr-x   11 paularmand  staff   374B May 16  2016 aangifte_2de_verblijven_kapucijnenvoer_149_leuven
      0 drwxr-xr-x@  11 paularmand  staff   374B Feb 18  2010 abcpipe
     72 -rw-r--r--@   1 paularmand  staff    34K Jun 28 23:00 abcpipe (1).zip
     72 -rw-r--r--@   1 paularmand  staff    34K Jun 28 22:58 abcpipe.zip
     16 -rw-r--r--@   1 paularmand  staff   5.5K Jul 16 09:52 accountingMovementList-1.xls
     16 -rw-r--r--@   1 paularmand  staff   7.0K Jul 16 09:29 accountingMovementList.xls
   2224 -rw-r--r--@   1 paularmand  staff   1.1M Apr 26  2016 armandpien.m4v
  11072 -rw-r--r--@   1 paularmand  staff   5.4M Apr 26  2016 armandpien.mov
   2160 -rw-r--r--@   1 paularmand  staff   1.1M Apr 26  2016 armandpien.mp4
   1336 -rw-r--r--@   1 paularmand  staff   667K Apr 26  2016 armandpien_1080i.mp4
      8 -rw-r--r--@   1 paularmand  staff   920B Aug  5 14:27 belgiumrca.crt
      8 -rw-r--r--@   1 paularmand  staff   914B Aug  5 14:27 belgiumrca2.crt
      8 -rw-r--r--@   1 paularmand  staff   1.4K Aug  5 14:27 belgiumrca3.crt
      8 -rw-r--r--@   1 paularmand  staff   1.4K Aug  5 14:27 belgiumrca4.crt
      8 -rw-r--r--@   1 paularmand  staff   736B Oct 18 18:45 big-data-initiative-workshop-algorithms-and-society.ics
      0 drwxr-xr-x    4 paularmand  staff   136B May 24  2016 carroserie
   2584 -rw-r--r--@   1 paularmand  staff   1.3M Jun 15 14:49 christoffel-recsys.pdf
   1488 -rw-r--r--@   1 paularmand  staff   743K May 18  2016 clustering_v2.pages
      0 drwxr-xr-x@   6 paularmand  staff   204B Nov  9 21:04 cocos2d-python-tutorials-master
     16 -rw-r--r--@   1 paularmand  staff   6.4K Nov  9 21:04 cocos2d-python-tutorials-master.zip
      8 -rw-r--r--@   1 paularmand  staff   3.6K Aug  8 17:06 cpub-MAN-AD-DLBeheer-Managment_Server-CmsRdsh.rdp
      8 -rw-r--r--@   1 paularmand  staff   3.6K Aug  8 17:06 cpub-MAN-AD-Groepenbeheer-Managment_Server-CmsRdsh.rdp
      8 -rw-r--r--@   1 paularmand  staff   3.6K Aug  8 17:06 cpub-MAN-PC_Cinfo-Managment_Server-CmsRdsh.rdp
      8 -rw-r--r--@   1 paularmand  staff   122B Oct 13 13:50 credentials.csv
      8 -rw-r--r--@   1 paularmand  staff   144B Sep 27 12:08 custom.css
      8 -rw-r--r--@   1 paularmand  staff   2.3K Sep 28 17:27 dashboard (1).json
     16 -rw-r--r--@   1 paularmand  staff   5.4K Sep 27 17:56 dashboard.json
      8 -rw-r--r--@   1 paularmand  staff   2.3K Sep 28 17:01 dashboard_001.json
      8 -rw-r--r--@   1 paularmand  staff   1.1K Sep 27 18:43 dashboard_kijkcijfers.json
  10904 -rw-r--r--@   1 paularmand  staff   5.3M Nov  7 14:30 dashboard_voorstelling.key
      8 -rw-r--r--@   1 paularmand  staff   375B Sep 27 16:16 dashku_57ea7e5453146d790901215c.py
      8 -rw-r--r--@   1 paularmand  staff   430B Sep 29 11:50 dashku_57ece3ac53146d7909012186.py
      8 -rw-r--r--@   1 paularmand  staff   378B Sep 30 12:18 dashku_57ee3be67ef3da0c00b5e41c.py
      8 -rw-r--r--@   1 paularmand  staff   378B Oct 31 15:21 dashku_57ee906b4ce6ef0c00fcdbd4 (1).py
      8 -rw-r--r--@   1 paularmand  staff   378B Sep 30 18:20 dashku_57ee906b4ce6ef0c00fcdbd4.py
   2608 -rw-r--r--@   1 paularmand  staff   1.3M Aug 18 13:22 data & personalisatie 6 2016.key
   2600 -rw-r--r--@   1 paularmand  staff   1.3M Aug 18 13:48 data & personalisatie 7 2016.key
      8 -rw-r--r--@   1 paularmand  staff   779B Jun 10 13:29 data.tsv
 120960 -rw-r--r--@   1 paularmand  staff    59M Apr 25  2016 demo2.mov
  19976 -rw-r--r--    1 paularmand  staff   9.8M Sep  7 19:14 dog1.svg
   7072 -rw-r--r--@   1 paularmand  staff   3.4M Jun 29 11:50 download (1).svg
   3200 -rw-r--r--@   1 paularmand  staff   1.6M Jul 13 16:45 download (2).svg
   1640 -rw-r--r--@   1 paularmand  staff   819K Nov 18 13:36 download.jpeg
     16 -rw-r--r--@   1 paularmand  staff   6.0K Jun  1 16:36 download.png
   1344 -rw-r--r--@   1 paularmand  staff   668K Jun 29 11:23 download.svg
  21976 -rw-r--r--@   1 paularmand  staff    11M May 16  2016 eID-Quickinstaller-4.1.11 (1).dmg
  21976 -rw-r--r--@   1 paularmand  staff    11M Apr 23  2016 eID-Quickinstaller-4.1.11.dmg
      0 drwxr-xr-x   10 paularmand  staff   340B Sep 29 22:04 epson
      8 -rw-r--r--@   1 paularmand  staff   415B Aug 24 10:57 event.ics
     16 -rw-r--r--    1 paularmand  staff   6.0K Sep 27 17:33 example-freeboard.json
  14776 -rw-r--r--    1 paularmand  staff   7.2M Sep  7 22:18 export11.png
  22928 -rw-r--r--    1 paularmand  staff    11M Sep  7 22:18 export11.svg
  44856 -rw-r--r--@   1 paularmand  staff    22M Oct 27 08:31 finaldraft1000Mac.zip
      0 drwxr-xr-x    5 paularmand  staff   170B Sep 18 10:31 house
  10616 -rw-r--r--@   1 paularmand  staff   5.2M Aug 24 16:21 iTerm2-3_0_4.zip
 638168 -rw-r--r--@   1 paularmand  staff   312M Jul 12 22:14 ideaIC-2016.2.dmg
 465480 -rw-r--r--@   1 paularmand  staff   227M Jul 12 23:14 jdk-8u91-macosx-x64.dmg
   9536 -rw-r--r--@   1 paularmand  staff   4.7M Apr 26  2016 jing.dmg
 131728 -rw-r--r--@   1 paularmand  staff    64M Aug 21 21:17 jre-8u101-macosx-x64.dmg
 131744 -rw-r--r--@   1 paularmand  staff    64M Oct 27 20:52 jre-8u111-macosx-x64.dmg
 131632 -rw-r--r--@   1 paularmand  staff    64M Apr 23  2016 jre-8u91-macosx-x64(1).dmg
 131632 -rw-r--r--@   1 paularmand  staff    64M May 18  2016 jre-8u91-macosx-x64.dmg
 104800 -rw-r--r--@   1 paularmand  staff    51M Oct 28 14:31 kafkatool.dmg
  23304 -rw-r--r--@   1 paularmand  staff    11M Jun 12 23:10 konijntjes.pages
  27936 -rw-r--r--@   1 paularmand  staff    14M Jun 12 23:09 konijntjes.pdf
  13976 -rw-r--r--@   1 paularmand  staff   6.8M Jun 12 23:06 konijntjes2.pdf
     80 -rw-r--r--@   1 paularmand  staff    39K May 19  2016 kostenplaatje.ods
     80 -rw-r--r--    1 paularmand  staff    38K May 19  2016 kostenplaatje.ods.cpgz
     40 -rw-r--r--@   1 paularmand  staff    20K May 19  2016 kostenplaatje.xls
  18512 -rw-r--r--@   1 paularmand  staff   9.0M Sep  7 16:21 lastposition_poc_2016_09_17_pave-1.swf
  18512 -rw-r--r--    1 paularmand  staff   9.0M Sep  7 16:19 lastposition_poc_2016_09_17_pave.swf
      0 drwx------@   5 paularmand  staff   170B Nov 14 09:54 lpmacosx
  42464 -rw-r--r--@   1 paularmand  staff    21M Nov 14 09:53 lpmacosx.zip
  70288 -rw-r--r--@   1 paularmand  staff    34M Apr 26  2016 mac-video-converter-free_full1009.dmg
5724632 -rw-r--r--@   1 paularmand  staff   2.7G Sep 13 10:46 mactex-20160603.pkg
      0 drwx------    8 paularmand  staff   272B Aug 24 17:02 mascotte_animations
   3760 -rw-r--r--    1 paularmand  staff   1.8M Aug 24 17:02 mascotte_animations.zip
     96 -rw-r--r--@   1 paularmand  staff    47K May 12  2016 mds.png
     80 -rw-r--r--@   1 paularmand  staff    39K Jul 15 21:37 mergedDocuments (1).pdf
     80 -rw-r--r--@   1 paularmand  staff    39K Sep 18 12:09 mergedDocuments (2).pdf
     40 -rw-r--r--@   1 paularmand  staff    19K Sep 18 12:10 mergedDocuments (3).pdf
     80 -rw-r--r--@   1 paularmand  staff    39K Sep 18 12:08 mergedDocuments.pdf
    552 -rw-r--r--@   1 paularmand  staff   272K Aug 14 11:31 mpdf.pdf
     24 -rw-r--r--@   1 paularmand  staff   8.8K Jun  1 16:18 number_of_clusters.png
      0 drwxr-xr-x@  19 paularmand  staff   646B Nov 23 21:49 opencv-2.4.13
 184224 -rw-r--r--@   1 paularmand  staff    90M Nov 23 21:44 opencv-2.4.13.zip
   1424 -rw-r--r--    1 paularmand  staff   711K Sep  7 19:05 outline_dog.png
   7976 -rw-r--r--@   1 paularmand  staff   3.9M Nov 17 00:16 output.jpg
      0 drwxr-xr-x@  21 paularmand  staff   714B Apr 26  2016 pancartes 1
   3672 -rw-r--r--@   1 paularmand  staff   1.8M Apr 26  2016 pancartes 1.zip
   7088 -rw-r--r--@   1 paularmand  staff   3.5M Jun  2 13:59 paularmand_verhaegen.png
    200 -rw-r--r--@   1 paularmand  staff    98K May 12  2016 pc5_6.png
      8 -rw-r--r--@   1 paularmand  staff   180B Sep 13 14:27 playlist.m3u8
      8 -rw-r--r--@   1 paularmand  staff     9B Jun 29 10:47 plot (1).svg
      8 -rw-r--r--@   1 paularmand  staff     9B Jun 29 11:00 plot (2).svg
      8 -rw-r--r--@   1 paularmand  staff     9B Jun 29 11:02 plot (3).svg
      8 -rw-r--r--@   1 paularmand  staff     9B Jun 29 11:04 plot (4).svg
      8 -rw-r--r--@   1 paularmand  staff     9B Jun 29 10:44 plot.svg
   2728 -rw-r--r--@   1 paularmand  staff   1.3M Nov 21  2015 plugins.pkg
 364480 -rw-r--r--@   1 paularmand  staff   178M Nov  9 20:33 pycharm-community-2016.2.3.dmg
    568 -rw-r--r--    1 paularmand  staff   282K Nov 23 23:33 raspberrypi-b-plus-case.svg
    720 -rw-r--r--@   1 paularmand  staff   358K Jun 30 11:46 recsys arch1.key
    304 -rw-r--r--@   1 paularmand  staff   150K May 17  2016 sandbox_dashboard_ips.pdf
  56016 -rw-r--r--@   1 paularmand  staff    27M Jul 12 22:40 scala-2.11.8.tgz
    392 -rw-r--r--@   1 paularmand  staff   195K Jul  3 22:43 schoolmateriaal 2016-2017.pdf
    960 -rw-r--r--@   1 paularmand  staff   477K Jun  6 23:15 screenshotacts.png
      8 -rw-r--r--@   1 paularmand  staff   136B Oct  6 21:58 searchMovement.txt
   4184 -rw-r--r--@   1 paularmand  staff   2.0M Sep 29 10:00 shrook-1294.dmg
      8 -rw-r--r--@   1 paularmand  staff   267B May 12  2016 simple_plot.py
   1088 -rw-r--r--@   1 paularmand  staff   542K May 26  2016 skype_siamak_amini_bbc.pdf
      8 -rw-r--r--@   1 paularmand  staff   3.9K Aug 11 10:54 spark-csv-1.4.0-s_2.10.pom
      8 -rw-r--r--@   1 paularmand  staff   4.0K Sep 27 13:24 speedGauge.js
 448656 -rw-r--r--@   1 paularmand  staff   219M Jun 15 21:47 test2.mov
      8 -rw-r--r--@   1 paularmand  staff   2.9K Nov  2 15:08 tms1a_76474.pdf
      0 drwxr-xr-x    2 paularmand  staff    68B Aug 29 11:14 untitled folder
     96 -rw-r--r--@   1 paularmand  staff    45K Jun 15 14:49 viewings_against_duration.png
   1616 -rw-r--r--@   1 paularmand  staff   806K Jun  6 22:34 vrt_personalisatie_technisch_architectuur_v2_16_03_02_pave 2.key
   1656 -rw-r--r--@   1 paularmand  staff   824K May 19  2016 vrt_personalisatie_technisch_architectuur_v2_16_03_02_pave 2.pdf
   1560 -rw-r--r--@   1 paularmand  staff   778K Apr 28  2016 vrt_personalisatie_technisch_architectuur_v2_16_03_02_pave.key.zip
   1720 -rw-r--r--@   1 paularmand  staff   857K May 13  2016 vrt_personalisatie_technisch_architectuur_v3_16_05_13_pave.key
   4496 -rw-r--r--@   1 paularmand  staff   2.2M Oct 20 16:10 vrt_personalisatie_v6_16_08_25_pave.key
     16 -rw-r--r--@   1 paularmand  staff   4.6K May  9  2016 vrt_piwik.user.js
      0 drwx------@   8 paularmand  staff   272B Apr 25  2016 wetransfer-91d28e
 538640 -rw-r--r--@   1 paularmand  staff   263M Apr 25  2016 wetransfer-91d28e.zip
      8 -rw-r--r--@   1 paularmand  staff   3.1K Oct 12 15:26 workshop.html
paularmandsmbp.rto.be 02:56:23 ~/Downloads$ cd ~/D
Desktop/   Documents/ Downloads/ Dropbox/   
paularmandsmbp.rto.be 02:56:23 ~/Downloads$ cd ~/dev_habitat
paularmandsmbp.rto.be 02:56:42 ~/dev_habitat$ ll
total 24
 0 drwxr-xr-x@ 12 paularmand  staff   408B Nov 24 13:46 .
 0 drwxr-xr-x@  8 paularmand  staff   272B Aug 19 09:51 ..
24 -rw-r--r--@  1 paularmand  staff    10K Nov 24 14:54 .DS_Store
 0 drwxr-xr-x@  9 paularmand  staff   306B Nov 24 13:47 Providence
 0 drwxr-xr-x@ 15 paularmand  staff   510B Nov 15 08:22 baldrick
 0 drwxr-xr-x@  7 paularmand  staff   238B Nov 23 16:36 data_nginx
 0 drwxr-xr-x@  4 paularmand  staff   136B Nov 16 10:43 de_slimste_mens_tensorflow
 0 drwxr-xr-x@  8 paularmand  staff   272B Nov 15 09:06 habitat-deploy
 0 drwxr-xr-x@  8 paularmand  staff   272B Oct 20 15:20 habitat-doc
 0 drwxr-xr-x@ 10 paularmand  staff   340B Oct 19 14:37 habitat-kafka
 0 drwxr-xr-x@  3 paularmand  staff   102B Nov 15 08:19 pio-kafka
 0 drwxr-xr-x@  7 paularmand  staff   238B Nov 22 16:54 radioplus_site
paularmandsmbp.rto.be 02:56:42 ~/dev_habitat$ mv Providence providence
paularmandsmbp.rto.be 02:57:16 ~/dev_habitat$ ll
total 24
 0 drwxr-xr-x@ 12 paularmand  staff   408B Nov 24 14:57 .
 0 drwxr-xr-x@  8 paularmand  staff   272B Aug 19 09:51 ..
24 -rw-r--r--@  1 paularmand  staff    10K Nov 24 14:54 .DS_Store
 0 drwxr-xr-x@ 15 paularmand  staff   510B Nov 15 08:22 baldrick
 0 drwxr-xr-x@  7 paularmand  staff   238B Nov 23 16:36 data_nginx
 0 drwxr-xr-x@  4 paularmand  staff   136B Nov 16 10:43 de_slimste_mens_tensorflow
 0 drwxr-xr-x@  8 paularmand  staff   272B Nov 15 09:06 habitat-deploy
 0 drwxr-xr-x@  8 paularmand  staff   272B Oct 20 15:20 habitat-doc
 0 drwxr-xr-x@ 10 paularmand  staff   340B Oct 19 14:37 habitat-kafka
 0 drwxr-xr-x@  3 paularmand  staff   102B Nov 15 08:19 pio-kafka
 0 drwxr-xr-x@  9 paularmand  staff   306B Nov 24 13:47 providence
 0 drwxr-xr-x@  7 paularmand  staff   238B Nov 22 16:54 radioplus_site
paularmandsmbp.rto.be 02:57:18 ~/dev_habitat$ cd providence/
paularmandsmbp.rto.be 02:57:23 ~/dev_habitat/providence$ ll
total 24
 0 drwxr-xr-x@  9 paularmand  staff   306B Nov 24 13:47 .
 0 drwxr-xr-x@ 12 paularmand  staff   408B Nov 24 14:57 ..
16 -rw-r--r--@  1 paularmand  staff   6.0K Nov 24 13:47 .DS_Store
 0 drwxr-xr-x@  8 paularmand  staff   272B Nov 24 14:54 .idea
 0 drwxr-xr-x@  6 paularmand  staff   204B Nov 24 13:37 PROVIstorm
 8 -rwxr-xr-x@  1 paularmand  staff   525B Nov 24 03:41 README.txt
 0 drwxr-xr-x@ 19 paularmand  staff   646B Nov 24 13:17 providence-api
 0 drwxr-xr-x@ 24 paularmand  staff   816B Nov 24 13:43 providence-play
 0 drwxr-xr-x@ 25 paularmand  staff   850B Nov 24 13:38 providence-prediction
paularmandsmbp.rto.be 02:57:23 ~/dev_habitat/providence$ git init
Initialized empty Git repository in /Users/paularmand/Dropbox/personal/duktify/projects/vrt/proj_personalisation/dev/providence/.git/
paularmandsmbp.rto.be 02:57:33 (master) ~/dev_habitat/providence$ git remote add origin git@gitlab.com:vrtoeni/providence.git
paularmandsmbp.rto.be 02:57:48 (master) ~/dev_habitat/providence$ git add .
paularmandsmbp.rto.be 02:58:04 (master) ~/dev_habitat/providence$ git commit
[master (root-commit) 37bd942] t push -u origin master
 Committer: Paul-Armand Verhaegen <paularmand@paularmandsmbp.rto.be>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 3649 files changed, 775715 insertions(+)
 create mode 100644 .idea/Providence.iml
 create mode 100644 .idea/compiler.xml
 create mode 100644 .idea/copyright/profiles_settings.xml
 create mode 100644 .idea/misc.xml
 create mode 100644 .idea/modules.xml
 create mode 100644 .idea/workspace.xml
 create mode 100755 PROVIstorm/PROVIstorm/.settings/org.eclipse.core.resources.prefs
 create mode 100755 PROVIstorm/PROVIstorm/.settings/org.eclipse.jdt.core.prefs
 create mode 100755 PROVIstorm/PROVIstorm/.settings/org.eclipse.m2e.core.prefs
 create mode 100755 PROVIstorm/PROVIstorm/_classpath.xml
 create mode 100755 PROVIstorm/PROVIstorm/_project.xml
 create mode 100755 PROVIstorm/PROVIstorm/pom.xml
 create mode 100755 PROVIstorm/PROVIstorm/target/PROVIstorm-1.0-SNAPSHOT-jar-with-dependencies.jar
 create mode 100755 PROVIstorm/PROVIstorm/target/PROVIstorm-1.0-SNAPSHOT.jar
 create mode 100755 PROVIstorm/PROVIstorm/target/maven-archiver/pom.properties
 create mode 100755 PROVIstorm/PROVIstorm/target/maven-status/maven-compiler-plugin/compile/default-compile/createdFiles.lst
 create mode 100755 PROVIstorm/PROVIstorm/target/maven-status/maven-compiler-plugin/compile/default-compile/inputFiles.lst
 create mode 100755 PROVIstorm/README.txt
 create mode 100755 PROVIstorm/_DS_Store
 create mode 100755 README.txt
 create mode 100755 providence-api/.settings/org.eclipse.jdt.core.prefs
 create mode 100755 providence-api/README.txt
 create mode 100755 providence-api/_DS_Store
 create mode 100755 providence-api/_cache-main
 create mode 100755 providence-api/_classpath.xml
 create mode 100755 providence-api/_project.xml
 create mode 100755 providence-api/bin/api/ArticleAPI$$anonfun$1.class
 create mode 100755 providence-api/bin/api/ArticleAPI$$anonfun$2.class
 create mode 100755 providence-api/bin/api/ArticleAPI$$anonfun$3.class
 create mode 100755 providence-api/bin/api/ArticleAPI$$anonfun$4.class
 create mode 100755 providence-api/bin/api/ArticleAPI$$anonfun$5.class
 create mode 100755 providence-api/bin/api/ArticleAPI$$anonfun$getArticlesPublishedLastWeek$1.class
 create mode 100755 providence-api/bin/api/ArticleAPI$$anonfun$getArticlesPublishedLastWeek$2.class
 create mode 100755 providence-api/bin/api/ArticleAPI$$anonfun$getFacebookPagePopularitiesLast$1.class
 create mode 100755 providence-api/bin/api/ArticleAPI$$anonfun$getFacebookPagePopularitiesLast$2.class
 create mode 100755 providence-api/bin/api/ArticleAPI$$anonfun$getFacebookPopularities$1.class
 create mode 100755 providence-api/bin/api/ArticleAPI$$anonfun$getTwitterPagePopularitiesLast$1.class
 create mode 100755 providence-api/bin/api/ArticleAPI$$anonfun$getTwitterPagePopularitiesLast$2.class
 create mode 100755 providence-api/bin/api/ArticleAPI$$anonfun$getTwitterPopularities$1.class
 create mode 100755 providence-api/bin/api/ArticleAPI$$anonfun$getViewPopularitiesShort$1.class
 create mode 100755 providence-api/bin/api/ArticleAPI$.class
 create mode 100755 providence-api/bin/api/ArticleAPI.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$1.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$2.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$3.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$4.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$5.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$6.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$7.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$8.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$predictFacebookViralityDeredactie$1.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$predictFacebookViralityDeredactie$2.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$predictFacebookViralityDeredactie$3.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$predictFacebookViralityNewsmonkey$1.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$predictFacebookViralityNewsmonkey$2.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$predictFacebookViralityNewsmonkey$3.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$predictViewPopularityNewsmonkey$1.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$predictViewPopularityNewsmonkey$2.class
 create mode 100755 providence-api/bin/classification/Classification$$anonfun$predictViewPopularityNewsmonkey$3.class
 create mode 100755 providence-api/bin/classification/Classification.class
 create mode 100755 providence-api/bin/classification/ClassificationModel.class
 create mode 100755 providence-api/bin/classification/ClassificationRF.class
 create mode 100755 providence-api/bin/classification/python/ModelThomas$$anonfun$1.class
 create mode 100755 providence-api/bin/classification/python/ModelThomas$$anonfun$getPredictions$1.class
 create mode 100755 providence-api/bin/classification/python/ModelThomas$.class
 create mode 100755 providence-api/bin/classification/python/ModelThomas.class
 create mode 100755 providence-api/bin/classification/python/Python$$anonfun$fromSVMtoCVS$1$$anonfun$1.class
 create mode 100755 providence-api/bin/classification/python/Python$$anonfun$fromSVMtoCVS$1.class
 create mode 100755 providence-api/bin/classification/python/Python$.class
 create mode 100755 providence-api/bin/classification/python/Python.class
 create mode 100755 providence-api/bin/classification/python/RandomForest$$anonfun$getPredictions$1.class
 create mode 100755 providence-api/bin/classification/python/RandomForest$.class
 create mode 100755 providence-api/bin/classification/python/RandomForest.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$10.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$13.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$14.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$9.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getBasicFeatures$1$$anonfun$5.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getBasicFeatures$1$$anonfun$6.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getBasicFeatures$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getBasicFeatures$2$$anonfun$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getBasicFeatures$2.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getBasicFeatures$3$$anonfun$7.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getBasicFeatures$3$$anonfun$8.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getBasicFeatures$3.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getBasicFeatures$4$$anonfun$2.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getBasicFeatures$4.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getBasicFeaturesNewsmonkey$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getBasicFeaturesNewsmonkey$2.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getBasicFeaturesNewsmonkey$3$$anonfun$apply$2.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getBasicFeaturesNewsmonkey$3.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getFacebookFeatures$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getFacebookFeatures$2$$anonfun$11.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getFacebookFeatures$2$$anonfun$12.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getFacebookFeatures$2.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getFacebookFeatures$3$$anonfun$3.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getFacebookFeatures$3.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getViewFeatures$1$$anonfun$apply$mcVI$sp$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getViewFeatures$1$$anonfun$apply$mcVI$sp$2.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getViewFeatures$1$$anonfun$apply$mcVI$sp$3.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$getViewFeatures$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$init$1$$anonfun$apply$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$init$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$init$2.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$init$3.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$init$4.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$loadFeatures$1$$anonfun$4.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$loadFeatures$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$loadMaps$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$loadMaps$2.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$loadMaps$3.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$loadMaps$4.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$loadMaps$5.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData$$anonfun$loadMaps$6.class
 create mode 100755 providence-api/bin/classification/svm/ProcessData.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$10.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$13.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$14.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$8.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$9.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$1$$anonfun$4.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$1$$anonfun$5.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$2$$anonfun$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$2.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$3$$anonfun$6.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$3$$anonfun$7.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$3.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$4$$anonfun$2.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$4.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeaturesNewsmonkey$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeaturesNewsmonkey$2.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeaturesNewsmonkey$3$$anonfun$apply$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeaturesNewsmonkey$3.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeaturesNewsmonkey$4.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeaturesNewsmonkey$5.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeaturesNewsmonkey$6.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicPopularityFeatures$1$$anonfun$apply$mcVI$sp$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicPopularityFeatures$1$$anonfun$apply$mcVI$sp$2.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicPopularityFeatures$1$$anonfun$apply$mcVI$sp$3.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicPopularityFeatures$1$$anonfun$apply$mcVI$sp$4.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicPopularityFeatures$1$$anonfun$apply$mcVI$sp$5.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getBasicPopularityFeatures$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getFacebookFeatures$1$$anonfun$11.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getFacebookFeatures$1$$anonfun$12.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$getFacebookFeatures$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$loadFeatures$1$$anonfun$3.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$loadFeatures$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$loadMaps$1.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$loadMaps$2.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$loadMaps$3.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$loadMaps$4.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$loadMaps$5.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF$$anonfun$loadMaps$6.class
 create mode 100755 providence-api/bin/classification/svm/ProcessDataRF.class
 create mode 100755 providence-api/bin/classification/svm/SVMlinear$$anonfun$predict$1.class
 create mode 100755 providence-api/bin/classification/svm/SVMlinear.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/ArraySorter.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/DoubleArrayPointer.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/FeatureNode.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/Function.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/IntArrayPointer.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/InvalidInputDataException.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/L2R_L2_SvcFunction.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/L2R_LrFunction.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/Linear$GroupClassesReturn.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/Linear.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/Model.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/Parameter.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/Predict.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/PredictOnline.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/Problem.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/Record.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/SolverMCSVM_CS.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/SolverType.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/Train.class
 create mode 100755 providence-api/bin/classification/svm/liblinear/Tron.class
 create mode 100755 providence-api/bin/core/Config$.class
 create mode 100755 providence-api/bin/core/Config.class
 create mode 100755 providence-api/bin/core/Main$$anonfun$1.class
 create mode 100755 providence-api/bin/core/Main$$anonfun$2.class
 create mode 100755 providence-api/bin/core/Main$.class
 create mode 100755 providence-api/bin/core/Main$delayedInit$body.class
 create mode 100755 providence-api/bin/core/Main.class
 create mode 100755 providence-api/bin/entities/ApiLog.class
 create mode 100755 providence-api/bin/entities/Article$$anonfun$setNamedEntities$1.class
 create mode 100755 providence-api/bin/entities/Article$$anonfun$setNamedEntities$2.class
 create mode 100755 providence-api/bin/entities/Article$$anonfun$toText$1.class
 create mode 100755 providence-api/bin/entities/Article$$anonfun$toText$2.class
 create mode 100755 providence-api/bin/entities/Article$$anonfun$toText$3.class
 create mode 100755 providence-api/bin/entities/Article$$anonfun$toText$4.class
 create mode 100755 providence-api/bin/entities/Article$$anonfun$toText$5.class
 create mode 100755 providence-api/bin/entities/Article$$anonfun$toText$6.class
 create mode 100755 providence-api/bin/entities/Article.class
 create mode 100755 providence-api/bin/entities/ArticleFeatures.class
 create mode 100755 providence-api/bin/entities/FacebookPagePopularity$$anonfun$toText$1.class
 create mode 100755 providence-api/bin/entities/FacebookPagePopularity$$anonfun$toText$2.class
 create mode 100755 providence-api/bin/entities/FacebookPagePopularity.class
 create mode 100755 providence-api/bin/entities/FacebookPopularities$$anonfun$toText$1.class
 create mode 100755 providence-api/bin/entities/FacebookPopularities.class
 create mode 100755 providence-api/bin/entities/FacebookPopularity.class
 create mode 100755 providence-api/bin/entities/Feature.class
 create mode 100755 providence-api/bin/entities/NamedEntity.class
 create mode 100755 providence-api/bin/entities/QueryType$.class
 create mode 100755 providence-api/bin/entities/QueryType.class
 create mode 100755 providence-api/bin/entities/TwitterPagePopularity.class
 create mode 100755 providence-api/bin/entities/TwitterPopularities$$anonfun$toText$1.class
 create mode 100755 providence-api/bin/entities/TwitterPopularities.class
 create mode 100755 providence-api/bin/entities/TwitterPopularity$$anonfun$toText$1.class
 create mode 100755 providence-api/bin/entities/TwitterPopularity.class
 create mode 100755 providence-api/bin/entities/ViewPopularities$$anonfun$toText$1.class
 create mode 100755 providence-api/bin/entities/ViewPopularities$$anonfun$toText$2.class
 create mode 100755 providence-api/bin/entities/ViewPopularities$$anonfun$toText$3.class
 create mode 100755 providence-api/bin/entities/ViewPopularities.class
 create mode 100755 providence-api/bin/entities/ViewPopularity.class
 create mode 100755 providence-api/bin/entities/ViralityPrediction$.class
 create mode 100755 providence-api/bin/entities/ViralityPrediction.class
 create mode 100755 providence-api/bin/entities/ViralityPredictions$.class
 create mode 100755 providence-api/bin/entities/ViralityPredictions.class
 create mode 100755 providence-api/bin/entities/ViralityProbability$.class
 create mode 100755 providence-api/bin/entities/ViralityProbability.class
 create mode 100755 providence-api/bin/featuresextractors/ArticleFeaturesExtractor.class
 create mode 100755 providence-api/bin/featuresextractors/DeredactieArticleFeaturesExtractor.class
 create mode 100755 providence-api/bin/featuresextractors/HtmlArticleFeaturesExtractor.class
 create mode 100755 providence-api/bin/featuresextractors/NewsmonkeyArticleFeaturesExtractor.class
 create mode 100755 providence-api/bin/http/HtmlReceiver$.class
 create mode 100755 providence-api/bin/http/HtmlReceiver.class
 create mode 100755 providence-api/bin/persistence/ApiLogDAO.class
 create mode 100755 providence-api/bin/persistence/ArticleDAO.class
 create mode 100755 providence-api/bin/persistence/FacebookPagePopularityDAO.class
 create mode 100755 providence-api/bin/persistence/FacebookPopularityDAO.class
 create mode 100755 providence-api/bin/persistence/FeatureDAO.class
 create mode 100755 providence-api/bin/persistence/TwitterPagePopularityDAO.class
 create mode 100755 providence-api/bin/persistence/TwitterPopularityDAO.class
 create mode 100755 providence-api/bin/persistence/ViewPopularityDAO.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraApiLogDAO$$anonfun$getApiLogs$1.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraApiLogDAO.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraArticleDAO$$anonfun$getArticles$1.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraArticleDAO$$anonfun$getArticlesPublishedLastWeek$1.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraArticleDAO$$anonfun$getArticlesPublishedLastWeek$2.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraArticleDAO.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraClient$.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraClient.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraDAO.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraFacebookPagePopularityDAO$$anonfun$getFacebookPagePopularities$1.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraFacebookPagePopularityDAO$$anonfun$getFacebookPagePopularities$2.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraFacebookPagePopularityDAO.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraFacebookPopularityDAO$$anonfun$getFacebookPopularities$1.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraFacebookPopularityDAO$$anonfun$getFacebookPopularities$2.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraFacebookPopularityDAO.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraTwitterPagePopularityDAO$$anonfun$getTwitterPagePopularities$1.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraTwitterPagePopularityDAO$$anonfun$getTwitterPagePopularities$2.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraTwitterPagePopularityDAO.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraTwitterPopularityDAO$$anonfun$getTwitterPopularities$1.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraTwitterPopularityDAO$$anonfun$getTwitterPopularities$2.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraTwitterPopularityDAO.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraViewPopularityDAO$$anonfun$getViewPopularities$1.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraViewPopularityDAO$$anonfun$getViewPopularities$2.class
 create mode 100755 providence-api/bin/persistence/cassandra/CassandraViewPopularityDAO.class
 create mode 100755 providence-api/bin/persistence/file/FacebookPopularitiesDAO$$anonfun$read$1$$anonfun$apply$1.class
 create mode 100755 providence-api/bin/persistence/file/FacebookPopularitiesDAO$$anonfun$read$1.class
 create mode 100755 providence-api/bin/persistence/file/FacebookPopularitiesDAO$$anonfun$write$1.class
 create mode 100755 providence-api/bin/persistence/file/FacebookPopularitiesDAO$.class
 create mode 100755 providence-api/bin/persistence/file/FacebookPopularitiesDAO.class
 create mode 100755 providence-api/bin/persistence/file/FileArticleDAO$$anonfun$read$1$$anonfun$apply$1.class
 create mode 100755 providence-api/bin/persistence/file/FileArticleDAO$$anonfun$read$1$$anonfun$apply$2.class
 create mode 100755 providence-api/bin/persistence/file/FileArticleDAO$$anonfun$read$1$$anonfun$apply$3.class
 create mode 100755 providence-api/bin/persistence/file/FileArticleDAO$$anonfun$read$1$$anonfun$apply$4.class
 create mode 100755 providence-api/bin/persistence/file/FileArticleDAO$$anonfun$read$1$$anonfun$apply$5.class
 create mode 100755 providence-api/bin/persistence/file/FileArticleDAO$$anonfun$read$1$$anonfun$apply$6.class
 create mode 100755 providence-api/bin/persistence/file/FileArticleDAO$$anonfun$read$1$$anonfun$apply$7.class
 create mode 100755 providence-api/bin/persistence/file/FileArticleDAO$$anonfun$read$1.class
 create mode 100755 providence-api/bin/persistence/file/FileArticleDAO$$anonfun$write$1.class
 create mode 100755 providence-api/bin/persistence/file/FileArticleDAO.class
 create mode 100755 providence-api/bin/persistence/file/FileFeatureDAO$$anonfun$read$1.class
 create mode 100755 providence-api/bin/persistence/file/FileFeatureDAO.class
 create mode 100755 providence-api/bin/persistence/file/ReadDAO.class
 create mode 100755 providence-api/bin/persistence/file/TwitterPopularitiesDAO$$anonfun$read$1$$anonfun$apply$1.class
 create mode 100755 providence-api/bin/persistence/file/TwitterPopularitiesDAO$$anonfun$read$1.class
 create mode 100755 providence-api/bin/persistence/file/TwitterPopularitiesDAO$$anonfun$write$1.class
 create mode 100755 providence-api/bin/persistence/file/TwitterPopularitiesDAO$.class
 create mode 100755 providence-api/bin/persistence/file/TwitterPopularitiesDAO.class
 create mode 100755 providence-api/bin/persistence/file/ViewPopularitiesDAO$$anonfun$read$1$$anonfun$apply$1.class
 create mode 100755 providence-api/bin/persistence/file/ViewPopularitiesDAO$$anonfun$read$1$$anonfun$apply$2.class
 create mode 100755 providence-api/bin/persistence/file/ViewPopularitiesDAO$$anonfun$read$1$$anonfun$apply$3.class
 create mode 100755 providence-api/bin/persistence/file/ViewPopularitiesDAO$$anonfun$read$1.class
 create mode 100755 providence-api/bin/persistence/file/ViewPopularitiesDAO$$anonfun$write$1.class
 create mode 100755 providence-api/bin/persistence/file/ViewPopularitiesDAO$.class
 create mode 100755 providence-api/bin/persistence/file/ViewPopularitiesDAO.class
 create mode 100755 providence-api/bin/persistence/file/WriteDAO.class
 create mode 100755 providence-api/bin/runjava/RunJava.class
 create mode 100755 providence-api/bin/socialmedia/Facebook$.class
 create mode 100755 providence-api/bin/socialmedia/Facebook.class
 create mode 100755 providence-api/bin/socialmedia/Twitter$.class
 create mode 100755 providence-api/bin/socialmedia/Twitter.class
 create mode 100755 providence-api/dist/providence-api.jar
 create mode 100755 providence-api/lib/cassandra209/cassandra-driver-core-2.0.9.jar
 create mode 100755 providence-api/lib/cassandra209/cassandra-driver-dse-2.0.9.jar
 create mode 100755 providence-api/lib/cassandra209/lib/guava-14.0.1.jar
 create mode 100755 providence-api/lib/cassandra209/lib/lz4-1.2.0.jar
 create mode 100755 providence-api/lib/cassandra209/lib/metrics-core-3.0.2.jar
 create mode 100755 providence-api/lib/cassandra209/lib/slf4j-api-1.7.5.jar
 create mode 100755 providence-api/lib/cassandra209/lib/snappy-java-1.0.5.jar
 create mode 100755 providence-api/lib/commons-lang3-3.4.jar
 create mode 100755 providence-api/lib/commons-logging-1.2.jar
 create mode 100755 providence-api/lib/joda-time-2.6.jar
 create mode 100755 providence-api/lib/json-simple-1.1.1.jar
 create mode 100755 providence-api/lib/org.scala-lang.scala-library_2.11.7.v20150622-112736-1fbce4612c.jar
 create mode 100755 providence-api/lib/slf4j-api-1.7.13.jar
 create mode 100755 providence-api/providence-api-v1.0.pdf
 create mode 100755 providence-api/src/api/ArticleAPI.scala
 create mode 100755 providence-api/src/classification/Classification.scala
 create mode 100755 providence-api/src/classification/ClassificationModel.scala
 create mode 100755 providence-api/src/classification/ClassificationRF.scala
 create mode 100755 providence-api/src/classification/python/ModelThomas.scala
 create mode 100755 providence-api/src/classification/python/Python.scala
 create mode 100755 providence-api/src/classification/python/RandomForest.scala
 create mode 100755 providence-api/src/classification/svm/ProcessData.scala
 create mode 100755 providence-api/src/classification/svm/ProcessDataRF.scala
 create mode 100755 providence-api/src/classification/svm/SVMlinear.scala
 create mode 100755 providence-api/src/classification/svm/liblinear/ArraySorter.java
 create mode 100755 providence-api/src/classification/svm/liblinear/DoubleArrayPointer.java
 create mode 100755 providence-api/src/classification/svm/liblinear/FeatureNode.java
 create mode 100755 providence-api/src/classification/svm/liblinear/Function.java
 create mode 100755 providence-api/src/classification/svm/liblinear/IntArrayPointer.java
 create mode 100755 providence-api/src/classification/svm/liblinear/InvalidInputDataException.java
 create mode 100755 providence-api/src/classification/svm/liblinear/L2R_L2_SvcFunction.java
 create mode 100755 providence-api/src/classification/svm/liblinear/L2R_LrFunction.java
 create mode 100755 providence-api/src/classification/svm/liblinear/Linear.java
 create mode 100755 providence-api/src/classification/svm/liblinear/Model.java
 create mode 100755 providence-api/src/classification/svm/liblinear/Parameter.java
 create mode 100755 providence-api/src/classification/svm/liblinear/Predict.java
 create mode 100755 providence-api/src/classification/svm/liblinear/PredictOnline.java
 create mode 100755 providence-api/src/classification/svm/liblinear/Problem.java
 create mode 100755 providence-api/src/classification/svm/liblinear/Record.java
 create mode 100755 providence-api/src/classification/svm/liblinear/SolverMCSVM_CS.java
 create mode 100755 providence-api/src/classification/svm/liblinear/SolverType.java
 create mode 100755 providence-api/src/classification/svm/liblinear/Train.java
 create mode 100755 providence-api/src/classification/svm/liblinear/Tron.java
 create mode 100755 providence-api/src/core/Config.scala
 create mode 100755 providence-api/src/core/Main.scala
 create mode 100755 providence-api/src/entities/ApiLog.scala
 create mode 100755 providence-api/src/entities/Article.scala
 create mode 100755 providence-api/src/entities/ArticleFeatures.scala
 create mode 100755 providence-api/src/entities/FacebookPagePopularity.scala
 create mode 100755 providence-api/src/entities/FacebookPopularities.scala
 create mode 100755 providence-api/src/entities/FacebookPopularity.scala
 create mode 100755 providence-api/src/entities/Feature.scala
 create mode 100755 providence-api/src/entities/NamedEntity.scala
 create mode 100755 providence-api/src/entities/QueryType.scala
 create mode 100755 providence-api/src/entities/TwitterPagePopularity.scala
 create mode 100755 providence-api/src/entities/TwitterPopularities.scala
 create mode 100755 providence-api/src/entities/TwitterPopularity.scala
 create mode 100755 providence-api/src/entities/ViewPopularities.scala
 create mode 100755 providence-api/src/entities/ViewPopularity.scala
 create mode 100755 providence-api/src/entities/ViralityPrediction.scala
 create mode 100755 providence-api/src/entities/ViralityPredictions.scala
 create mode 100755 providence-api/src/entities/ViralityProbability.scala
 create mode 100755 providence-api/src/featuresextractors/ArticleFeaturesExtractor.java
 create mode 100755 providence-api/src/featuresextractors/DeredactieArticleFeaturesExtractor.java
 create mode 100755 providence-api/src/featuresextractors/HtmlArticleFeaturesExtractor.java
 create mode 100755 providence-api/src/featuresextractors/NewsmonkeyArticleFeaturesExtractor.java
 create mode 100755 providence-api/src/http/HtmlReceiver.scala
 create mode 100755 providence-api/src/persistence/ApiLogDAO.scala
 create mode 100755 providence-api/src/persistence/ArticleDAO.scala
 create mode 100755 providence-api/src/persistence/FacebookPagePopularityDAO.scala
 create mode 100755 providence-api/src/persistence/FacebookPopularityDAO.scala
 create mode 100755 providence-api/src/persistence/FeatureDAO.scala
 create mode 100755 providence-api/src/persistence/TwitterPagePopularityDAO.scala
 create mode 100755 providence-api/src/persistence/TwitterPopularityDAO.scala
 create mode 100755 providence-api/src/persistence/ViewPopularityDAO.scala
 create mode 100755 providence-api/src/persistence/cassandra/CassandraApiLogDAO.scala
 create mode 100755 providence-api/src/persistence/cassandra/CassandraArticleDAO.scala
 create mode 100755 providence-api/src/persistence/cassandra/CassandraClient.scala
 create mode 100755 providence-api/src/persistence/cassandra/CassandraDAO.scala
 create mode 100755 providence-api/src/persistence/cassandra/CassandraFacebookPagePopularityDAO.scala
 create mode 100755 providence-api/src/persistence/cassandra/CassandraFacebookPopularityDAO.scala
 create mode 100755 providence-api/src/persistence/cassandra/CassandraTwitterPagePopularityDAO.scala
 create mode 100755 providence-api/src/persistence/cassandra/CassandraTwitterPopularityDAO.scala
 create mode 100755 providence-api/src/persistence/cassandra/CassandraViewPopularityDAO.scala
 create mode 100755 providence-api/src/persistence/file/FacebookPopularitiesDAO.scala
 create mode 100755 providence-api/src/persistence/file/FileArticleDAO.scala
 create mode 100755 providence-api/src/persistence/file/FileFeatureDAO.scala
 create mode 100755 providence-api/src/persistence/file/ReadDAO.scala
 create mode 100755 providence-api/src/persistence/file/TwitterPopularitiesDAO.scala
 create mode 100755 providence-api/src/persistence/file/ViewPopularitiesDAO.scala
 create mode 100755 providence-api/src/persistence/file/WriteDAO.scala
 create mode 100755 providence-api/src/runjava/RunJava.java
 create mode 100755 providence-api/src/socialmedia/Facebook.scala
 create mode 100755 providence-api/src/socialmedia/Twitter.scala
 create mode 100755 providence-api/svm/deredactie-facebook/authorMap.txt
 create mode 100755 providence-api/svm/deredactie-facebook/categoryMap.txt
 create mode 100755 providence-api/svm/deredactie-facebook/deredactie_facebook.txt
 create mode 100755 providence-api/svm/deredactie-facebook/facebookPageMap.txt
 create mode 100755 providence-api/svm/deredactie-facebook/training-1.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-10.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-100.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-101.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-102.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-103.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-104.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-105.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-106.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-107.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-108.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-109.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-11.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-110.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-111.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-112.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-113.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-114.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-115.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-116.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-117.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-118.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-119.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-12.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-120.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-121.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-122.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-123.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-124.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-125.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-126.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-127.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-128.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-129.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-13.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-130.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-131.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-132.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-133.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-134.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-135.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-136.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-137.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-138.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-139.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-14.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-140.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-141.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-142.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-143.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-144.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-145.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-146.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-147.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-148.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-149.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-15.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-150.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-151.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-152.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-153.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-154.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-155.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-156.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-157.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-158.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-159.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-16.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-160.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-161.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-162.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-163.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-164.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-165.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-17.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-18.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-19.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-2.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-20.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-21.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-22.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-23.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-24.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-25.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-26.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-27.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-28.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-29.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-3.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-30.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-31.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-32.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-33.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-34.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-35.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-36.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-37.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-38.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-39.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-4.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-40.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-41.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-42.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-43.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-44.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-45.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-46.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-47.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-48.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-49.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-5.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-50.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-51.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-52.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-53.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-54.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-55.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-56.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-57.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-58.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-59.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-6.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-60.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-61.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-62.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-63.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-64.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-65.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-66.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-67.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-68.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-69.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-7.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-70.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-71.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-72.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-73.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-74.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-75.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-76.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-77.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-78.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-79.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-8.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-80.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-81.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-82.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-83.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-84.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-85.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-86.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-87.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-88.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-89.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-9.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-90.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-91.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-92.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-93.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-94.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-95.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-96.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-97.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-98.txt.model
 create mode 100755 providence-api/svm/deredactie-facebook/training-99.txt.model
 create mode 100755 providence-api/svm/deredactie-views/authorMap.txt
 create mode 100755 providence-api/svm/deredactie-views/categoryMap.txt
 create mode 100755 providence-api/svm/deredactie-views/deredactie_views.txt
 create mode 100755 providence-api/svm/deredactie-views/facebookPageMap.txt
 create mode 100755 providence-api/svm/deredactie-views/training-1.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-10.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-100.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-101.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-102.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-103.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-104.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-105.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-106.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-107.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-108.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-109.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-11.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-110.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-111.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-112.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-113.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-114.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-115.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-116.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-117.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-118.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-119.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-12.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-120.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-121.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-122.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-123.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-124.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-125.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-126.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-127.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-128.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-129.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-13.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-130.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-131.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-132.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-133.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-134.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-135.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-136.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-137.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-138.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-139.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-14.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-140.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-141.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-142.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-143.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-144.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-145.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-146.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-147.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-148.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-149.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-15.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-150.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-151.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-152.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-153.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-154.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-155.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-156.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-157.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-158.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-159.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-16.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-160.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-161.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-162.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-163.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-164.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-165.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-17.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-18.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-19.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-2.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-20.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-21.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-22.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-23.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-24.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-25.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-26.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-27.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-28.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-29.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-3.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-30.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-31.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-32.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-33.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-34.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-35.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-36.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-37.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-38.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-39.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-4.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-40.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-41.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-42.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-43.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-44.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-45.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-46.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-47.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-48.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-49.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-5.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-50.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-51.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-52.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-53.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-54.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-55.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-56.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-57.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-58.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-59.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-6.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-60.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-61.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-62.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-63.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-64.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-65.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-66.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-67.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-68.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-69.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-7.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-70.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-71.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-72.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-73.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-74.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-75.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-76.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-77.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-78.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-79.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-8.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-80.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-81.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-82.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-83.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-84.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-85.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-86.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-87.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-88.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-89.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-9.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-90.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-91.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-92.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-93.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-94.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-95.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-96.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-97.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-98.txt.model
 create mode 100755 providence-api/svm/deredactie-views/training-99.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/authorMap.txt
 create mode 100755 providence-api/svm/newsmonkey-facebook/categoryMap.txt
 create mode 100755 providence-api/svm/newsmonkey-facebook/facebookPageMap.txt
 create mode 100755 providence-api/svm/newsmonkey-facebook/newsmonkey_ann_facebook.txt
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-0.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-1.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-10.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-100.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-101.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-102.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-103.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-104.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-105.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-106.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-107.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-108.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-109.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-11.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-110.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-111.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-112.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-113.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-114.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-115.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-116.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-117.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-118.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-119.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-12.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-120.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-121.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-122.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-123.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-124.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-125.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-126.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-127.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-128.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-129.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-13.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-130.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-131.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-132.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-133.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-134.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-135.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-136.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-137.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-138.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-139.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-14.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-140.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-141.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-142.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-143.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-144.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-145.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-146.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-147.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-148.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-149.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-15.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-150.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-151.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-152.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-153.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-154.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-155.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-156.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-157.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-158.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-159.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-16.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-160.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-161.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-162.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-163.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-164.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-165.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-17.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-18.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-19.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-2.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-20.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-21.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-22.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-23.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-24.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-25.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-26.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-27.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-28.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-29.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-3.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-30.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-31.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-32.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-33.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-34.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-35.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-36.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-37.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-38.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-39.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-4.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-40.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-41.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-42.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-43.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-44.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-45.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-46.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-47.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-48.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-49.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-5.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-50.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-51.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-52.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-53.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-54.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-55.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-56.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-57.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-58.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-59.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-6.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-60.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-61.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-62.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-63.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-64.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-65.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-66.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-67.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-68.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-69.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-7.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-70.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-71.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-72.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-73.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-74.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-75.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-76.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-77.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-78.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-79.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-8.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-80.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-81.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-82.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-83.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-84.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-85.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-86.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-87.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-88.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-89.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-9.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-90.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-91.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-92.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-93.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-94.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-95.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-96.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-97.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-98.txt.model
 create mode 100755 providence-api/svm/newsmonkey-facebook/training-99.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/authorMap.txt
 create mode 100755 providence-api/svm/newsmonkey-views/categoryMap.txt
 create mode 100755 providence-api/svm/newsmonkey-views/facebookPageMap.txt
 create mode 100755 providence-api/svm/newsmonkey-views/newsmonkey_ann_views.txt
 create mode 100755 providence-api/svm/newsmonkey-views/training-0.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-1.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-10.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-100.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-101.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-102.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-103.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-104.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-105.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-106.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-107.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-108.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-109.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-11.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-110.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-111.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-112.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-113.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-114.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-115.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-116.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-117.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-118.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-119.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-12.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-120.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-121.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-122.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-123.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-124.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-125.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-126.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-127.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-128.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-129.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-13.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-130.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-131.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-132.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-133.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-134.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-135.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-136.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-137.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-138.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-139.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-14.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-140.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-141.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-142.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-143.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-144.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-145.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-146.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-147.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-148.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-149.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-15.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-150.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-151.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-152.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-153.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-154.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-155.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-156.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-157.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-158.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-159.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-16.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-160.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-161.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-162.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-163.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-164.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-165.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-17.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-18.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-19.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-2.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-20.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-21.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-22.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-23.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-24.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-25.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-26.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-27.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-28.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-29.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-3.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-30.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-31.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-32.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-33.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-34.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-35.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-36.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-37.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-38.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-39.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-4.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-40.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-41.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-42.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-43.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-44.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-45.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-46.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-47.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-48.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-49.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-5.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-50.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-51.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-52.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-53.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-54.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-55.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-56.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-57.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-58.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-59.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-6.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-60.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-61.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-62.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-63.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-64.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-65.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-66.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-67.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-68.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-69.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-7.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-70.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-71.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-72.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-73.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-74.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-75.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-76.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-77.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-78.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-79.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-8.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-80.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-81.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-82.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-83.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-84.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-85.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-86.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-87.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-88.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-89.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-9.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-90.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-91.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-92.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-93.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-94.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-95.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-96.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-97.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-98.txt.model
 create mode 100755 providence-api/svm/newsmonkey-views/training-99.txt.model
 create mode 100755 providence-api/svm/rf/deredactie-views/authorMap.txt
 create mode 100755 providence-api/svm/rf/deredactie-views/categoryMap.txt
 create mode 100755 providence-api/svm/rf/deredactie-views/facebookPageMap.txt
 create mode 100755 providence-api/svm/rf/deredactie-views/features.txt
 create mode 100755 providence-play/.sbtserver/connections/master.log
 create mode 100755 providence-play/.sbtserver/connections/play-fork-run-028132b6-8cbb-4867-af41-09750a704c9e.log
 create mode 100755 providence-play/.sbtserver/master.log
 create mode 100755 providence-play/.sbtserver/previous.log
 create mode 100755 providence-play/LICENSE
 create mode 100755 providence-play/README.txt
 create mode 100755 providence-play/RUNNING_PID
 create mode 100755 providence-play/_DS_Store
 create mode 100755 providence-play/_gitignore
 create mode 100755 providence-play/_history
 create mode 100755 providence-play/activator
 create mode 100755 providence-play/activator-launch-1.3.4.jar
 create mode 100755 providence-play/activator.bat
 create mode 100755 providence-play/app/Global.scala
 create mode 100755 providence-play/app/controllers/Application.scala
 create mode 100755 providence-play/app/controllers/Article.scala
 create mode 100755 providence-play/app/controllers/Facebook.scala
 create mode 100755 providence-play/app/controllers/Twitter.scala
 create mode 100755 providence-play/app/controllers/View.scala
 create mode 100755 providence-play/app/models/Configuration.scala
 create mode 100755 providence-play/app/views/index.scala.html
 create mode 100755 providence-play/app/views/main.scala.html
 create mode 100755 providence-play/build.sbt
 create mode 100755 providence-play/command_to_run_on_server.txt
 create mode 100755 providence-play/conf/application.conf
 create mode 100755 providence-play/conf/logback.xml
 create mode 100755 providence-play/conf/routes
 create mode 100755 providence-play/lib/providence-api.jar
 create mode 100755 providence-play/logs/application.log
 create mode 100755 providence-play/project/_DS_Store
 create mode 100755 providence-play/project/_sbtserver
 create mode 100755 providence-play/project/_sbtserver.lock
 create mode 100755 providence-play/project/build.properties
 create mode 100755 providence-play/project/play-fork-run.sbt
 create mode 100755 providence-play/project/plugins.sbt
 create mode 100755 providence-play/project/project/target/config-classes/$1fbd07580eb473c85e30$.class
 create mode 100755 providence-play/project/project/target/config-classes/$1fbd07580eb473c85e30.cache
 create mode 100755 providence-play/project/project/target/config-classes/$1fbd07580eb473c85e30.class
 create mode 100755 providence-play/project/project/target/config-classes/$33ab188d56e53a5e3e7f$.class
 create mode 100755 providence-play/project/project/target/config-classes/$33ab188d56e53a5e3e7f.cache
 create mode 100755 providence-play/project/project/target/config-classes/$33ab188d56e53a5e3e7f.class
 create mode 100755 providence-play/project/project/target/config-classes/$656cfe7d725b70af02c4$.class
 create mode 100755 providence-play/project/project/target/config-classes/$656cfe7d725b70af02c4.cache
 create mode 100755 providence-play/project/project/target/config-classes/$656cfe7d725b70af02c4.class
 create mode 100755 providence-play/project/project/target/config-classes/$6f1336abb12de463414b$.class
 create mode 100755 providence-play/project/project/target/config-classes/$6f1336abb12de463414b.cache
 create mode 100755 providence-play/project/project/target/config-classes/$6f1336abb12de463414b.class
 create mode 100755 providence-play/project/project/target/config-classes/$778042b8a09dcf15a2e6$.class
 create mode 100755 providence-play/project/project/target/config-classes/$778042b8a09dcf15a2e6.cache
 create mode 100755 providence-play/project/project/target/config-classes/$778042b8a09dcf15a2e6.class
 create mode 100755 providence-play/project/project/target/config-classes/$7a82b2e3abb95128191a$.class
 create mode 100755 providence-play/project/project/target/config-classes/$7a82b2e3abb95128191a.cache
 create mode 100755 providence-play/project/project/target/config-classes/$7a82b2e3abb95128191a.class
 create mode 100755 providence-play/project/project/target/config-classes/$958e36c3cbc8f2c6e617$.class
 create mode 100755 providence-play/project/project/target/config-classes/$958e36c3cbc8f2c6e617.cache
 create mode 100755 providence-play/project/project/target/config-classes/$958e36c3cbc8f2c6e617.class
 create mode 100755 providence-play/project/project/target/config-classes/$c44f644530bdd41057d2$.class
 create mode 100755 providence-play/project/project/target/config-classes/$c44f644530bdd41057d2.cache
 create mode 100755 providence-play/project/project/target/config-classes/$c44f644530bdd41057d2.class
 create mode 100755 providence-play/project/project/target/config-classes/$eba6ccd2296a89eedb78$.class
 create mode 100755 providence-play/project/project/target/config-classes/$eba6ccd2296a89eedb78.cache
 create mode 100755 providence-play/project/project/target/config-classes/$eba6ccd2296a89eedb78.class
 create mode 100755 providence-play/project/sbt-ui.sbt
 create mode 100755 providence-play/project/target/_DS_Store
 create mode 100755 providence-play/project/target/coffeescript/sbt-coffeescript-1.0.0.jar
 create mode 100755 providence-play/project/target/config-classes/$1125825342bed28fba01$$anonfun$root$1.class
 create mode 100755 providence-play/project/target/config-classes/$1125825342bed28fba01$$anonfun$root$2.class
 create mode 100755 providence-play/project/target/config-classes/$1125825342bed28fba01$$anonfun$root$3.class
 create mode 100755 providence-play/project/target/config-classes/$1125825342bed28fba01$$anonfun$root$4.class
 create mode 100755 providence-play/project/target/config-classes/$1125825342bed28fba01$.class
 create mode 100755 providence-play/project/target/config-classes/$1125825342bed28fba01.cache
 create mode 100755 providence-play/project/target/config-classes/$1125825342bed28fba01.class
 create mode 100755 providence-play/project/target/config-classes/$2095546371bc550defcd$$anonfun$$sbtdef$1.class
 create mode 100755 providence-play/project/target/config-classes/$2095546371bc550defcd$.class
 create mode 100755 providence-play/project/target/config-classes/$2095546371bc550defcd.cache
 create mode 100755 providence-play/project/target/config-classes/$2095546371bc550defcd.class
 create mode 100755 providence-play/project/target/config-classes/$2b8fba1f4ae368d00fc5$$anonfun$$sbtdef$1.class
 create mode 100755 providence-play/project/target/config-classes/$2b8fba1f4ae368d00fc5$.class
 create mode 100755 providence-play/project/target/config-classes/$2b8fba1f4ae368d00fc5.cache
 create mode 100755 providence-play/project/target/config-classes/$2b8fba1f4ae368d00fc5.class
 create mode 100755 providence-play/project/target/config-classes/$2ba14ffb6e5f8bb9709b$$anonfun$$sbtdef$1.class
 create mode 100755 providence-play/project/target/config-classes/$2ba14ffb6e5f8bb9709b$.class
 create mode 100755 providence-play/project/target/config-classes/$2ba14ffb6e5f8bb9709b.cache
 create mode 100755 providence-play/project/target/config-classes/$2ba14ffb6e5f8bb9709b.class
 create mode 100755 providence-play/project/target/config-classes/$3e04193ae53fc17dfc96$$anonfun$$sbtdef$1.class
 create mode 100755 providence-play/project/target/config-classes/$3e04193ae53fc17dfc96$.class
 create mode 100755 providence-play/project/target/config-classes/$3e04193ae53fc17dfc96.cache
 create mode 100755 providence-play/project/target/config-classes/$3e04193ae53fc17dfc96.class
 create mode 100755 providence-play/project/target/config-classes/$8aaff70fc44f800b17c8$$anonfun$$sbtdef$1.class
 create mode 100755 providence-play/project/target/config-classes/$8aaff70fc44f800b17c8$.class
 create mode 100755 providence-play/project/target/config-classes/$8aaff70fc44f800b17c8.cache
 create mode 100755 providence-play/project/target/config-classes/$8aaff70fc44f800b17c8.class
 create mode 100755 providence-play/project/target/config-classes/$9eb3dc80289c0413524d$$anonfun$$sbtdef$1.class
 create mode 100755 providence-play/project/target/config-classes/$9eb3dc80289c0413524d$.class
 create mode 100755 providence-play/project/target/config-classes/$9eb3dc80289c0413524d.cache
 create mode 100755 providence-play/project/target/config-classes/$9eb3dc80289c0413524d.class
 create mode 100755 providence-play/project/target/config-classes/$b34d788b8287d2a85b63$$anonfun$$sbtdef$1.class
 create mode 100755 providence-play/project/target/config-classes/$b34d788b8287d2a85b63$.class
 create mode 100755 providence-play/project/target/config-classes/$b34d788b8287d2a85b63.cache
 create mode 100755 providence-play/project/target/config-classes/$b34d788b8287d2a85b63.class
 create mode 100755 providence-play/project/target/jshint/sbt-jshint-1.0.3.jar
 create mode 100755 providence-play/project/target/less/sbt-less-1.0.6.jar
 create mode 100755 providence-play/project/target/node-modules/_DS_Store
 create mode 100755 providence-play/project/target/node-modules/webjars/_DS_Store
 create mode 100755 providence-play/project/target/node-modules/webjars/amdefine/amdefine.js
 create mode 100755 providence-play/project/target/node-modules/webjars/amdefine/intercept.js
 create mode 100755 providence-play/project/target/node-modules/webjars/amdefine/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/clean.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/colors/hsl-to-hex.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/colors/long-to-short-hex.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/colors/rgb-to-hex.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/colors/shortener.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/images/url-rebase.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/images/url-rewriter.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/imports/inliner.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/properties/optimizer.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/properties/override-compactor.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/properties/processable.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/properties/scanner.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/properties/shorthand-compactor.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/properties/token.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/properties/validator.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/selectors/empty-removal.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/selectors/optimizer.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/selectors/tokenizer.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/text/comma-splitter.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/text/comments.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/text/escape-store.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/text/expressions.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/text/free.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/text/name-quotes.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/text/quote-scanner.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/lib/text/urls.js
 create mode 100755 providence-play/project/target/node-modules/webjars/clean-css/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/lib/coffee-script/browser.js
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/lib/coffee-script/cake.js
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/lib/coffee-script/coffee-script.js
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/lib/coffee-script/command.js
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/lib/coffee-script/grammar.js
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/lib/coffee-script/helpers.js
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/lib/coffee-script/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/lib/coffee-script/lexer.js
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/lib/coffee-script/nodes.js
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/lib/coffee-script/optparse.js
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/lib/coffee-script/parser.js
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/lib/coffee-script/register.js
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/lib/coffee-script/repl.js
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/lib/coffee-script/rewriter.js
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/lib/coffee-script/scope.js
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/lib/coffee-script/sourcemap.js
 create mode 100755 providence-play/project/target/node-modules/webjars/coffee-script/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/console-browserify/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/console-browserify/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/debug/lib/debug.js
 create mode 100755 providence-play/project/target/node-modules/webjars/debug/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/diff/diff.js
 create mode 100755 providence-play/project/target/node-modules/webjars/diff/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/jshint/data/ascii-identifier-data.js
 create mode 100755 providence-play/project/target/node-modules/webjars/jshint/data/non-ascii-identifier-part-only.js
 create mode 100755 providence-play/project/target/node-modules/webjars/jshint/data/non-ascii-identifier-start.js
 create mode 100755 providence-play/project/target/node-modules/webjars/jshint/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/jshint/src/jshint.js
 create mode 100755 providence-play/project/target/node-modules/webjars/jshint/src/lex.js
 create mode 100755 providence-play/project/target/node-modules/webjars/jshint/src/messages.js
 create mode 100755 providence-play/project/target/node-modules/webjars/jshint/src/reg.js
 create mode 100755 providence-play/project/target/node-modules/webjars/jshint/src/state.js
 create mode 100755 providence-play/project/target/node-modules/webjars/jshint/src/style.js
 create mode 100755 providence-play/project/target/node-modules/webjars/jshint/src/vars.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/browser.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/colors.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/encoder.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/env.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/extend-visitor.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/fs.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/functions.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/import-visitor.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/join-selector-visitor.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/lessc_helper.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/parser.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/rhino.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/source-map-output.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/to-css-visitor.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/alpha.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/anonymous.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/assignment.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/call.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/color.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/comment.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/condition.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/detached-ruleset.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/dimension.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/directive.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/element.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/expression.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/extend.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/import.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/javascript.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/keyword.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/media.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/mixin.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/negative.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/operation.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/paren.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/quoted.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/rule.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/ruleset-call.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/ruleset.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/selector.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/unicode-descriptor.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/url.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/value.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/tree/variable.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/less/visitor.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/source-map/source-map-0.1.31.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/source-map/source-map-footer.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/lib/source-map/source-map-header.js
 create mode 100755 providence-play/project/target/node-modules/webjars/less/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/mkdirp/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mkdirp/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/browser/debug.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/browser/events.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/browser/fs.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/browser/path.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/browser/progress.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/browser/tty.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/context.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/hook.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/interfaces/bdd.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/interfaces/exports.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/interfaces/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/interfaces/qunit.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/interfaces/tdd.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/mocha.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/ms.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/base.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/doc.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/dot.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/html-cov.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/html.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/json-cov.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/json-stream.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/json.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/landing.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/list.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/markdown.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/min.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/nyan.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/progress.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/spec.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/tap.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/templates/coverage.jade
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/templates/menu.jade
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/templates/script.html
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/templates/style.html
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/reporters/xunit.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/runnable.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/runner.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/suite.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/template.html
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/test.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/lib/utils.js
 create mode 100755 providence-play/project/target/node-modules/webjars/mocha/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/_DS_Store
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/bin/node-gyp-bin/node-gyp
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/bin/node-gyp-bin/node-gyp.cmd
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/bin/npm
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/bin/npm-cli.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/bin/npm.cmd
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/bin/read-package-json.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/adduser.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/bin.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/bugs.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/build.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/cache.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/completion.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/config.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/dedupe.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/deprecate.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/docs.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/edit.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/explore.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/faq.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/get.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/help-search.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/help.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/init.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/install.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/link.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/ls.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/npm.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/outdated.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/owner.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/pack.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/prefix.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/prune.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/publish.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/rebuild.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/repo.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/restart.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/root.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/run-script.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/search.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/set.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/shrinkwrap.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/star.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/stars.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/start.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/stop.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/submodule.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/substack.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/tag.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/test.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/unbuild.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/uninstall.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/unpublish.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/update.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/utils/completion.sh
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/utils/completion/file-completion.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/utils/completion/installed-deep.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/utils/completion/installed-shallow.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/utils/error-handler.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/utils/fetch.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/utils/find-prefix.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/utils/gently-rm.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/utils/is-git-url.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/utils/lifecycle.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/utils/link.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/utils/tar.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/version.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/view.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/visnup.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/whoami.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/lib/xmas.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/abbrev/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/abbrev/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/abbrev/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansi/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansi/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansi/color-spaces.pl
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansi/examples/cursorPosition.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansi/examples/starwars.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansi/lib/ansi.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansi/lib/newlines.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansi/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansicolors/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansicolors/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansicolors/ansicolors.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansicolors/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansistyles/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansistyles/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansistyles/ansistyles.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansistyles/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ansistyles/test/ansistyles.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/archy/README.markdown
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/archy/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/archy/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/block-stream/LICENCE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/block-stream/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/block-stream/bench/block-stream-pause.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/block-stream/bench/block-stream.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/block-stream/bench/dropper-pause.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/block-stream/bench/dropper.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/block-stream/block-stream.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/block-stream/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/block-stream/test/basic.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/child-process-close/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/child-process-close/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/child-process-close/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/chmodr/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/chmodr/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/chmodr/chmodr.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/chmodr/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/chmodr/test/basic.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/chmodr/test/sync.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/chownr/LICENCE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/chownr/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/chownr/chownr.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/chownr/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/cmd-shim/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/cmd-shim/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/cmd-shim/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/cmd-shim/_travis.yml
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/cmd-shim/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/cmd-shim/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/cmd-shim/test/00-setup.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/cmd-shim/test/basic.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/cmd-shim/test/zz-cleanup.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/columnify/Readme.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/columnify/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/columnify/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/columnify/utils.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/editor/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/editor/README.markdown
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/editor/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/editor/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream-npm/LICENCE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream-npm/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream-npm/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream-npm/fstream-npm.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream-npm/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream/_travis.yml
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream/fstream.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream/lib/abstract.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream/lib/collect.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream/lib/dir-reader.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream/lib/dir-writer.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream/lib/file-reader.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream/lib/file-writer.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream/lib/get-type.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream/lib/link-reader.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream/lib/reader.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream/lib/writer.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/fstream/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/github-url-from-git/History.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/github-url-from-git/Makefile
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/github-url-from-git/Readme.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/github-url-from-git/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/github-url-from-git/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/github-url-from-git/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/github-url-from-git/test.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/github-url-from-username-repo/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/github-url-from-username-repo/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/github-url-from-username-repo/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/github-url-from-username-repo/_travis.yml
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/github-url-from-username-repo/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/github-url-from-username-repo/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/glob/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/glob/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/glob/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/glob/_travis.yml
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/glob/examples/g.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/glob/examples/usr-local.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/glob/glob.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/glob/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/graceful-fs/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/graceful-fs/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/graceful-fs/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/graceful-fs/graceful-fs.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/graceful-fs/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/graceful-fs/polyfills.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/inherits/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/inherits/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/inherits/inherits.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/inherits/inherits_browser.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/inherits/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/inherits/test.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ini/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ini/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ini/ini.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/ini/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/init-package-json/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/init-package-json/default-input.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/init-package-json/init-package-json.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/init-package-json/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/lockfile/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/lockfile/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/lockfile/lockfile.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/lockfile/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/lru-cache/CONTRIBUTORS
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/lru-cache/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/lru-cache/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/lru-cache/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/lru-cache/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/minimatch/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/minimatch/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/minimatch/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/minimatch/minimatch.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/minimatch/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/mkdirp/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/mkdirp/README.markdown
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/mkdirp/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/mkdirp/_travis.yml
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/mkdirp/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/mkdirp/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/node-gyp/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/node-gyp/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/node-gyp/_jshintrc
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/node-gyp/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/node-gyp/addon.gypi
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/node-gyp/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/nopt/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/nopt/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/nopt/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/nopt/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npm-registry-client/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npm-registry-client/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npm-registry-client/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npm-registry-client/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npm-registry-client/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npm-user-validate/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npm-user-validate/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npm-user-validate/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npm-user-validate/_travis.yml
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npm-user-validate/npm-user-validate.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npm-user-validate/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npmconf/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npmconf/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npmconf/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npmconf/config-defs.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npmconf/npmconf.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npmconf/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npmlog/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npmlog/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npmlog/example.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npmlog/log.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/npmlog/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/once/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/once/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/once/once.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/once/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/opener/LICENSE.txt
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/opener/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/opener/opener.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/opener/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/osenv/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/osenv/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/osenv/osenv.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/osenv/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/path-is-inside/LICENSE.txt
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/path-is-inside/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/path-is-inside/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/read-installed/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/read-installed/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/read-installed/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/read-installed/read-installed.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/read-package-json/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/read-package-json/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/read-package-json/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/read-package-json/read-json.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/read/LICENCE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/read/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/read/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/read/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/read/rs.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/request/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/request/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/request/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/request/_travis.yml
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/request/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/request/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/request/request.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/retry/License
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/retry/Makefile
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/retry/Readme.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/retry/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/retry/equation.gif
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/retry/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/retry/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/rimraf/AUTHORS
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/rimraf/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/rimraf/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/rimraf/bin.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/rimraf/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/rimraf/rimraf.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/semver/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/semver/Makefile
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/semver/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/semver/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/semver/foot.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/semver/head.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/semver/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/semver/semver.browser.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/semver/semver.browser.js.gz
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/semver/semver.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/semver/semver.min.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/semver/semver.min.js.gz
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/sha/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/sha/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/sha/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/sha/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/sha/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/slide/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/slide/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/slide/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/slide/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/tar/LICENCE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/tar/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/tar/_npmignore
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/tar/_travis.yml
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/tar/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/tar/tar.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/text-table/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/text-table/_travis.yml
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/text-table/index.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/text-table/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/text-table/readme.markdown
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/uid-number/LICENCE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/uid-number/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/uid-number/get-uid-gid.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/uid-number/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/uid-number/uid-number.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/which/LICENSE
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/which/README.md
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/which/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/node_modules/which/which.js
 create mode 100755 providence-play/project/target/node-modules/webjars/npm/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/requirejs/bin/r.js
 create mode 100755 providence-play/project/target/node-modules/webjars/requirejs/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/source-map/lib/source-map.js
 create mode 100755 providence-play/project/target/node-modules/webjars/source-map/lib/source-map/array-set.js
 create mode 100755 providence-play/project/target/node-modules/webjars/source-map/lib/source-map/base64-vlq.js
 create mode 100755 providence-play/project/target/node-modules/webjars/source-map/lib/source-map/base64.js
 create mode 100755 providence-play/project/target/node-modules/webjars/source-map/lib/source-map/binary-search.js
 create mode 100755 providence-play/project/target/node-modules/webjars/source-map/lib/source-map/source-map-consumer.js
 create mode 100755 providence-play/project/target/node-modules/webjars/source-map/lib/source-map/source-map-generator.js
 create mode 100755 providence-play/project/target/node-modules/webjars/source-map/lib/source-map/source-node.js
 create mode 100755 providence-play/project/target/node-modules/webjars/source-map/lib/source-map/util.js
 create mode 100755 providence-play/project/target/node-modules/webjars/source-map/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/strip-json-comments/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/strip-json-comments/strip-json-comments.js
 create mode 100755 providence-play/project/target/node-modules/webjars/underscore/package.json
 create mode 100755 providence-play/project/target/node-modules/webjars/underscore/underscore-min.js
 create mode 100755 providence-play/project/target/node-modules/webjars/underscore/underscore-min.map
 create mode 100755 providence-play/project/target/node-modules/webjars/underscore/underscore.js
 create mode 100755 providence-play/project/target/resolution-cache/reports/default-providence-play-build-compile-internal.xml
 create mode 100755 providence-play/project/target/resolution-cache/reports/default-providence-play-build-compile.xml
 create mode 100755 providence-play/project/target/resolution-cache/reports/default-providence-play-build-docs.xml
 create mode 100755 providence-play/project/target/resolution-cache/reports/default-providence-play-build-optional.xml
 create mode 100755 providence-play/project/target/resolution-cache/reports/default-providence-play-build-plugin.xml
 create mode 100755 providence-play/project/target/resolution-cache/reports/default-providence-play-build-pom.xml
 create mode 100755 providence-play/project/target/resolution-cache/reports/default-providence-play-build-provided.xml
 create mode 100755 providence-play/project/target/resolution-cache/reports/default-providence-play-build-runtime-internal.xml
 create mode 100755 providence-play/project/target/resolution-cache/reports/default-providence-play-build-runtime.xml
 create mode 100755 providence-play/project/target/resolution-cache/reports/default-providence-play-build-scala-tool.xml
 create mode 100755 providence-play/project/target/resolution-cache/reports/default-providence-play-build-sources.xml
 create mode 100755 providence-play/project/target/resolution-cache/reports/default-providence-play-build-test-internal.xml
 create mode 100755 providence-play/project/target/resolution-cache/reports/default-providence-play-build-test.xml
 create mode 100755 providence-play/project/target/resolution-cache/reports/ivy-report.css
 create mode 100755 providence-play/project/target/resolution-cache/reports/ivy-report.xsl
 create mode 100755 providence-play/project/target/streams/$global/$global/$global/streams/out
 create mode 100755 providence-play/project/target/streams/$global/ivyConfiguration/$global/streams/out
 create mode 100755 providence-play/project/target/streams/$global/ivySbt/$global/streams/out
 create mode 100755 providence-play/project/target/streams/$global/projectDescriptors/$global/streams/out
 create mode 100755 providence-play/project/target/streams/$global/update/$global/streams/out
 create mode 100755 providence-play/project/target/streams/$global/update/$global/streams/update_cache_2.10/output
 create mode 100755 providence-play/project/target/streams/compile/$global/$global/discoveredMainClasses/data
 create mode 100755 providence-play/project/target/streams/compile/compile/$global/streams/out
 create mode 100755 providence-play/project/target/streams/compile/compileIncremental/$global/streams/export
 create mode 100755 providence-play/project/target/streams/compile/compileIncremental/$global/streams/out
 create mode 100755 providence-play/project/target/streams/compile/copyResources/$global/streams/copy-resources.gz
 create mode 100755 providence-play/project/target/streams/compile/copyResources/$global/streams/out
 create mode 100755 providence-play/project/target/streams/compile/dependencyClasspath/$global/streams/export
 create mode 100755 providence-play/project/target/streams/compile/exportedProducts/$global/streams/export
 create mode 100755 providence-play/project/target/streams/compile/externalDependencyClasspath/$global/streams/export
 create mode 100755 providence-play/project/target/streams/compile/internalDependencyClasspath/$global/streams/export
 create mode 100755 providence-play/project/target/streams/compile/managedClasspath/$global/streams/export
 create mode 100755 providence-play/project/target/streams/compile/unmanagedClasspath/$global/streams/export
 create mode 100755 providence-play/project/target/streams/compile/unmanagedJars/$global/streams/export
 create mode 100755 providence-play/project/target/streams/runtime/dependencyClasspath/$global/streams/export
 create mode 100755 providence-play/project/target/streams/runtime/exportedProducts/$global/streams/export
 create mode 100755 providence-play/project/target/streams/runtime/externalDependencyClasspath/$global/streams/export
 create mode 100755 providence-play/project/target/streams/runtime/fullClasspath/$global/streams/export
 create mode 100755 providence-play/project/target/streams/runtime/internalDependencyClasspath/$global/streams/export
 create mode 100755 providence-play/project/target/streams/runtime/managedClasspath/$global/streams/export
 create mode 100755 providence-play/project/target/streams/runtime/unmanagedClasspath/$global/streams/export
 create mode 100755 providence-play/project/target/streams/runtime/unmanagedJars/$global/streams/export
 create mode 100755 providence-play/project/target/webjars-plugin.cache
 create mode 100755 providence-play/providence-api-v1.0.pdf
 create mode 100755 providence-play/public/images/favicon.png
 create mode 100755 providence-play/public/javascripts/hello.js
 create mode 100755 providence-play/public/stylesheets/main.css
 create mode 100755 providence-play/target/- Copy.history
 create mode 100755 providence-play/target/_history
 create mode 100755 providence-play/target/resolution-cache/providence-play/providence-play_2.11/1.0-SNAPSHOT/resolved.xml.properties
 create mode 100755 providence-play/target/resolution-cache/providence-play/providence-play_2.11/1.0-SNAPSHOT/resolved.xml.xml
 create mode 100755 providence-play/target/resolution-cache/reports/ivy-report.css
 create mode 100755 providence-play/target/resolution-cache/reports/ivy-report.xsl
 create mode 100755 providence-play/target/resolution-cache/reports/providence-play-providence-play_2.11-compile-internal.xml
 create mode 100755 providence-play/target/resolution-cache/reports/providence-play-providence-play_2.11-compile.xml
 create mode 100755 providence-play/target/resolution-cache/reports/providence-play-providence-play_2.11-docs.xml
 create mode 100755 providence-play/target/resolution-cache/reports/providence-play-providence-play_2.11-fork-run.xml
 create mode 100755 providence-play/target/resolution-cache/reports/providence-play-providence-play_2.11-optional.xml
 create mode 100755 providence-play/target/resolution-cache/reports/providence-play-providence-play_2.11-plugin.xml
 create mode 100755 providence-play/target/resolution-cache/reports/providence-play-providence-play_2.11-pom.xml
 create mode 100755 providence-play/target/resolution-cache/reports/providence-play-providence-play_2.11-provided.xml
 create mode 100755 providence-play/target/resolution-cache/reports/providence-play-providence-play_2.11-runtime-internal.xml
 create mode 100755 providence-play/target/resolution-cache/reports/providence-play-providence-play_2.11-runtime.xml
 create mode 100755 providence-play/target/resolution-cache/reports/providence-play-providence-play_2.11-scala-tool.xml
 create mode 100755 providence-play/target/resolution-cache/reports/providence-play-providence-play_2.11-sources.xml
 create mode 100755 providence-play/target/resolution-cache/reports/providence-play-providence-play_2.11-test-internal.xml
 create mode 100755 providence-play/target/resolution-cache/reports/providence-play-providence-play_2.11-test.xml
 create mode 100755 providence-play/target/scala-2.11/api/Global$.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/Application.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/Article.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/Facebook.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/GetArticleForm.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/GetFacebookForm.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/GetLatestArticleForm.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/GetTwitterForm.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/GetViewCacheForm.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/GetViewForm.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/ReverseApplication.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/ReverseArticle.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/ReverseAssets.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/ReverseFacebook.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/ReverseTwitter.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/ReverseView.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/Twitter.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/View.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/javascript/ReverseApplication.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/javascript/ReverseArticle.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/javascript/ReverseAssets.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/javascript/ReverseFacebook.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/javascript/ReverseTwitter.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/javascript/ReverseView.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/javascript/package.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/package.html
 create mode 100755 providence-play/target/scala-2.11/api/controllers/routes.html
 create mode 100755 providence-play/target/scala-2.11/api/index.html
 create mode 100755 providence-play/target/scala-2.11/api/index.js
 create mode 100755 providence-play/target/scala-2.11/api/index/index-_.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-a.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-b.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-c.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-d.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-e.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-f.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-g.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-h.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-i.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-j.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-k.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-m.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-n.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-p.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-r.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-s.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-t.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-v.html
 create mode 100755 providence-play/target/scala-2.11/api/index/index-w.html
 create mode 100755 providence-play/target/scala-2.11/api/lib/arrow-down.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/arrow-right.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/class.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/class_big.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/class_diagram.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/class_to_object_big.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/constructorsbg.gif
 create mode 100755 providence-play/target/scala-2.11/api/lib/conversionbg.gif
 create mode 100755 providence-play/target/scala-2.11/api/lib/defbg-blue.gif
 create mode 100755 providence-play/target/scala-2.11/api/lib/defbg-green.gif
 create mode 100755 providence-play/target/scala-2.11/api/lib/diagrams.css
 create mode 100755 providence-play/target/scala-2.11/api/lib/diagrams.js
 create mode 100755 providence-play/target/scala-2.11/api/lib/filter_box_left.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/filter_box_left2.gif
 create mode 100755 providence-play/target/scala-2.11/api/lib/filter_box_right.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/filterbg.gif
 create mode 100755 providence-play/target/scala-2.11/api/lib/filterboxbarbg.gif
 create mode 100755 providence-play/target/scala-2.11/api/lib/filterboxbarbg.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/filterboxbg.gif
 create mode 100755 providence-play/target/scala-2.11/api/lib/fullcommenttopbg.gif
 create mode 100755 providence-play/target/scala-2.11/api/lib/index.css
 create mode 100755 providence-play/target/scala-2.11/api/lib/index.js
 create mode 100755 providence-play/target/scala-2.11/api/lib/jquery-ui.js
 create mode 100755 providence-play/target/scala-2.11/api/lib/jquery.js
 create mode 100755 providence-play/target/scala-2.11/api/lib/jquery.layout.js
 create mode 100755 providence-play/target/scala-2.11/api/lib/modernizr.custom.js
 create mode 100755 providence-play/target/scala-2.11/api/lib/navigation-li-a.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/navigation-li.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/object.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/object_big.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/object_diagram.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/object_to_class_big.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/object_to_trait_big.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/object_to_type_big.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/ownderbg2.gif
 create mode 100755 providence-play/target/scala-2.11/api/lib/ownerbg.gif
 create mode 100755 providence-play/target/scala-2.11/api/lib/ownerbg2.gif
 create mode 100755 providence-play/target/scala-2.11/api/lib/package.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/package_big.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/packagesbg.gif
 create mode 100755 providence-play/target/scala-2.11/api/lib/permalink.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/ref-index.css
 create mode 100755 providence-play/target/scala-2.11/api/lib/remove.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/scheduler.js
 create mode 100755 providence-play/target/scala-2.11/api/lib/selected-implicits.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/selected-right-implicits.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/selected-right.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/selected.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/selected2-right.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/selected2.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/signaturebg.gif
 create mode 100755 providence-play/target/scala-2.11/api/lib/signaturebg2.gif
 create mode 100755 providence-play/target/scala-2.11/api/lib/template.css
 create mode 100755 providence-play/target/scala-2.11/api/lib/template.js
 create mode 100755 providence-play/target/scala-2.11/api/lib/tools.tooltip.js
 create mode 100755 providence-play/target/scala-2.11/api/lib/trait.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/trait_big.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/trait_diagram.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/trait_to_object_big.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/type.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/type_big.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/type_diagram.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/type_to_object_big.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/typebg.gif
 create mode 100755 providence-play/target/scala-2.11/api/lib/unselected.png
 create mode 100755 providence-play/target/scala-2.11/api/lib/valuemembersbg.gif
 create mode 100755 providence-play/target/scala-2.11/api/models/Configuration$.html
 create mode 100755 providence-play/target/scala-2.11/api/models/package.html
 create mode 100755 providence-play/target/scala-2.11/api/package.html
 create mode 100755 providence-play/target/scala-2.11/api/router/Routes.html
 create mode 100755 providence-play/target/scala-2.11/api/router/RoutesPrefix$.html
 create mode 100755 providence-play/target/scala-2.11/api/router/package.html
 create mode 100755 providence-play/target/scala-2.11/api/views/html/index$.html
 create mode 100755 providence-play/target/scala-2.11/api/views/html/index_Scope0$$index.html
 create mode 100755 providence-play/target/scala-2.11/api/views/html/index_Scope0$.html
 create mode 100755 providence-play/target/scala-2.11/api/views/html/main$.html
 create mode 100755 providence-play/target/scala-2.11/api/views/html/main_Scope0$$main.html
 create mode 100755 providence-play/target/scala-2.11/api/views/html/main_Scope0$.html
 create mode 100755 providence-play/target/scala-2.11/api/views/html/package.html
 create mode 100755 providence-play/target/scala-2.11/api/views/package.html
 create mode 100755 providence-play/target/scala-2.11/classes/Global$.class
 create mode 100755 providence-play/target/scala-2.11/classes/Global.class
 create mode 100755 providence-play/target/scala-2.11/classes/application.conf
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Application$$anonfun$index$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Application.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Article$$anon$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Article$$anon$2.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Article$$anonfun$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Article$$anonfun$2.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Article$$anonfun$3.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Article$$anonfun$4.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Article$$anonfun$getArticle$1$$anonfun$apply$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Article$$anonfun$getArticle$1$$anonfun$apply$2.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Article$$anonfun$getArticle$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Article$$anonfun$getLatestArticles$1$$anonfun$apply$3.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Article$$anonfun$getLatestArticles$1$$anonfun$apply$4.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Article$$anonfun$getLatestArticles$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Article.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anon$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$2.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getNow$1$$anonfun$apply$3.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getNow$1$$anonfun$apply$4.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getNow$1$$anonfun$apply$8.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getNow$1$$anonfun$apply$9$$anonfun$3.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getNow$1$$anonfun$apply$9.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getNow$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getPages$1$$anonfun$apply$10.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getPages$1$$anonfun$apply$11.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getPages$1$$anonfun$apply$5.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getPages$1$$anonfun$apply$6.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getPages$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getPredict$1$$anonfun$apply$3.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getPredict$1$$anonfun$apply$4$$anonfun$apply$5.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getPredict$1$$anonfun$apply$4.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getPredict$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getTimeline$1$$anonfun$apply$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getTimeline$1$$anonfun$apply$2.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getTimeline$1$$anonfun$apply$6.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getTimeline$1$$anonfun$apply$7.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getTimeline$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getViral$1$$anonfun$apply$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getViral$1$$anonfun$apply$2.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook$$anonfun$getViral$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Facebook.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/GetArticleForm$.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/GetArticleForm.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/GetFacebookForm$.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/GetFacebookForm.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/GetLatestArticleForm$.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/GetLatestArticleForm.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/GetTwitterForm$.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/GetTwitterForm.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/GetViewCacheForm$.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/GetViewCacheForm.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/GetViewForm$.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/GetViewForm.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/ReverseApplication.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/ReverseArticle.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/ReverseAssets.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/ReverseFacebook.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/ReverseTwitter.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/ReverseView.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anon$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$2.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$getNow$1$$anonfun$apply$8.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$getNow$1$$anonfun$apply$9.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$getNow$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$getPages$1$$anonfun$apply$10.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$getPages$1$$anonfun$apply$11.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$getPages$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$getPredict$1$$anonfun$apply$3.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$getPredict$1$$anonfun$apply$4$$anonfun$apply$5.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$getPredict$1$$anonfun$apply$4.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$getPredict$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$getTimeline$1$$anonfun$apply$6.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$getTimeline$1$$anonfun$apply$7.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$getTimeline$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$getViral$1$$anonfun$apply$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$getViral$1$$anonfun$apply$2.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter$$anonfun$getViral$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/Twitter.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anon$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anon$2.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anon$3.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$2.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$3.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$4.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getNow$1$$anonfun$apply$15.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getNow$1$$anonfun$apply$16.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getNow$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getPredict$1$$anonfun$apply$8.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getPredict$1$$anonfun$apply$9.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getPredict$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getPredictDummy$1$$anonfun$apply$10.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getPredictDummy$1$$anonfun$apply$11$$anonfun$apply$12.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getPredictDummy$1$$anonfun$apply$11.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getPredictDummy$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getPredictToCache$1$$anonfun$apply$5.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getPredictToCache$1$$anonfun$apply$6$$anonfun$apply$7.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getPredictToCache$1$$anonfun$apply$6.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getPredictToCache$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getTimeline$1$$anonfun$apply$13.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getTimeline$1$$anonfun$apply$14.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getTimeline$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getViral$1$$anonfun$apply$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getViral$1$$anonfun$apply$2.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getViral$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getViralDummy$1$$anonfun$apply$3.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getViralDummy$1$$anonfun$apply$4.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View$$anonfun$getViralDummy$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/View.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/javascript/ReverseApplication.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/javascript/ReverseArticle.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/javascript/ReverseAssets.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/javascript/ReverseFacebook.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/javascript/ReverseTwitter.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/javascript/ReverseView.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/routes$javascript.class
 create mode 100755 providence-play/target/scala-2.11/classes/controllers/routes.class
 create mode 100755 providence-play/target/scala-2.11/classes/logback.xml
 create mode 100755 providence-play/target/scala-2.11/classes/models/Configuration$.class
 create mode 100755 providence-play/target/scala-2.11/classes/models/Configuration.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$documentation$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Application_index0_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Article_getArticle1_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Article_getArticle2_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Article_getLatestArticles3_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Article_getLatestArticles4_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Assets_versioned21_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Assets_versioned35_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Facebook_getNow7_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Facebook_getNow8_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Facebook_getPages10_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Facebook_getPages9_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Facebook_getPredict11_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Facebook_getPredict12_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Facebook_getTimeline5_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Facebook_getTimeline6_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Facebook_getViral13_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Facebook_getViral14_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Twitter_getNow13_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Twitter_getNow14_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Twitter_getNow17_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Twitter_getNow18_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Twitter_getPages15_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Twitter_getPages16_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Twitter_getPages19_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Twitter_getPages20_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Twitter_getPredict21_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Twitter_getPredict22_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Twitter_getTimeline11_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Twitter_getTimeline12_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Twitter_getTimeline15_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Twitter_getTimeline16_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Twitter_getViral23_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_Twitter_getViral24_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_View_getNow19_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_View_getNow20_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_View_getNow27_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_View_getNow28_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_View_getPredict29_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_View_getPredict30_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_View_getPredictToCache31_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_View_getPredictToCache32_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_View_getTimeline17_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_View_getTimeline18_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_View_getTimeline25_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_View_getTimeline26_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_View_getViral33_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$router$Routes$$controllers_View_getViral34_invoker$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$1$$anonfun$apply$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$10$$anonfun$apply$10.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$10.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$11$$anonfun$apply$11.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$11.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$12$$anonfun$apply$12.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$12.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$13$$anonfun$apply$13.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$13.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$14$$anonfun$apply$14.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$14.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$15$$anonfun$apply$15.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$15.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$16$$anonfun$apply$16.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$16.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$17$$anonfun$apply$17.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$17.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$18$$anonfun$apply$18.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$18.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$19$$anonfun$apply$19.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$19.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$2$$anonfun$apply$2.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$2.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$20$$anonfun$apply$20.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$20.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$21$$anonfun$apply$21.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$21.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$22$$anonfun$apply$22.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$22.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$23$$anonfun$apply$23.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$23.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$24$$anonfun$apply$24.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$24.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$25$$anonfun$apply$25.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$25.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$26$$anonfun$apply$26.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$26.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$27$$anonfun$apply$27.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$27.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$28$$anonfun$apply$28.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$28.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$29$$anonfun$apply$29.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$29.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$3$$anonfun$apply$3.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$3.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$30$$anonfun$apply$30.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$30.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$31$$anonfun$apply$31.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$31.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$32$$anonfun$apply$32.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$32.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$33$$anonfun$apply$33.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$33.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$34$$anonfun$apply$34.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$34.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$35$$anonfun$apply$35.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$35.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$36$$anonfun$apply$36.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$36.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$4$$anonfun$apply$4.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$4.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$5$$anonfun$apply$5.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$5.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$6$$anonfun$apply$6.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$6.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$7$$anonfun$apply$7.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$7.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$8$$anonfun$apply$8.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$8.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$9$$anonfun$apply$9.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1$$anonfun$applyOrElse$9.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes$$anonfun$routes$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/Routes.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/RoutesPrefix$$anonfun$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/RoutesPrefix$.class
 create mode 100755 providence-play/target/scala-2.11/classes/router/RoutesPrefix.class
 create mode 100755 providence-play/target/scala-2.11/classes/routes
 create mode 100755 providence-play/target/scala-2.11/classes/views/html/index$.class
 create mode 100755 providence-play/target/scala-2.11/classes/views/html/index.class
 create mode 100755 providence-play/target/scala-2.11/classes/views/html/index_Scope0$.class
 create mode 100755 providence-play/target/scala-2.11/classes/views/html/index_Scope0$index$$anonfun$f$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/views/html/index_Scope0$index.class
 create mode 100755 providence-play/target/scala-2.11/classes/views/html/index_Scope0.class
 create mode 100755 providence-play/target/scala-2.11/classes/views/html/main$.class
 create mode 100755 providence-play/target/scala-2.11/classes/views/html/main.class
 create mode 100755 providence-play/target/scala-2.11/classes/views/html/main_Scope0$.class
 create mode 100755 providence-play/target/scala-2.11/classes/views/html/main_Scope0$main$$anonfun$f$1$$anonfun$apply$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/views/html/main_Scope0$main$$anonfun$f$1.class
 create mode 100755 providence-play/target/scala-2.11/classes/views/html/main_Scope0$main.class
 create mode 100755 providence-play/target/scala-2.11/classes/views/html/main_Scope0.class
 create mode 100755 providence-play/target/scala-2.11/providence-play_2.11-1.0-SNAPSHOT-javadoc.jar
 create mode 100755 providence-play/target/scala-2.11/providence-play_2.11-1.0-SNAPSHOT-sources.jar
 create mode 100755 providence-play/target/scala-2.11/providence-play_2.11-1.0-SNAPSHOT-web-assets.jar
 create mode 100755 providence-play/target/scala-2.11/providence-play_2.11-1.0-SNAPSHOT.jar
 create mode 100755 providence-play/target/scala-2.11/providence-play_2.11-1.0-SNAPSHOT.pom
 create mode 100755 providence-play/target/scala-2.11/routes/main/controllers/ReverseRoutes.scala
 create mode 100755 providence-play/target/scala-2.11/routes/main/controllers/javascript/JavaScriptReverseRoutes.scala
 create mode 100755 providence-play/target/scala-2.11/routes/main/controllers/routes.java
 create mode 100755 providence-play/target/scala-2.11/routes/main/router/Routes.scala
 create mode 100755 providence-play/target/scala-2.11/routes/main/router/RoutesPrefix.scala
 create mode 100755 providence-play/target/scala-2.11/twirl/main/views/html/index.template.scala
 create mode 100755 providence-play/target/scala-2.11/twirl/main/views/html/main.template.scala
 create mode 100755 providence-play/target/streams/$global/$global/$global/streams/out
 create mode 100755 providence-play/target/streams/$global/coffeescript/$global/streams/copy-resource/op-cache
 create mode 100755 providence-play/target/streams/$global/compilerReporter/$global/streams/out
 create mode 100755 providence-play/target/streams/$global/dependencyPositions/$global/streams/update_cache_2.11/input_dsp
 create mode 100755 providence-play/target/streams/$global/dependencyPositions/$global/streams/update_cache_2.11/output_dsp
 create mode 100755 providence-play/target/streams/$global/ivyConfiguration/$global/streams/out
 create mode 100755 providence-play/target/streams/$global/ivySbt/$global/streams/out
 create mode 100755 providence-play/target/streams/$global/jshint/$global/streams/copy-resource/op-cache
 create mode 100755 providence-play/target/streams/$global/less/$global/streams/copy-resource/op-cache
 create mode 100755 providence-play/target/streams/$global/makePom/$global/streams/out
 create mode 100755 providence-play/target/streams/$global/mappings/$global/streams/out
 create mode 100755 providence-play/target/streams/$global/playCommonClassloader/$global/streams/out
 create mode 100755 providence-play/target/streams/$global/playCompileEverything/$global/streams/out
 create mode 100755 providence-play/target/streams/$global/playForkRun/$global/streams/out
 create mode 100755 providence-play/target/streams/$global/playGenerateSecret/$global/streams/out
 create mode 100755 providence-play/target/streams/$global/playUpdateSecret/$global/streams/out
 create mode 100755 providence-play/target/streams/$global/projectDescriptors/$global/streams/out
 create mode 100755 providence-play/target/streams/$global/update/$global/streams/out
 create mode 100755 providence-play/target/streams/$global/update/$global/streams/update_cache_2.11/inputs
 create mode 100755 providence-play/target/streams/$global/update/$global/streams/update_cache_2.11/output
 create mode 100755 providence-play/target/streams/$global/webReporter/$global/streams/out
 create mode 100755 providence-play/target/streams/compile/$global/$global/discoveredMainClasses/data
 create mode 100755 providence-play/target/streams/compile/compile/$global/streams/out
 create mode 100755 providence-play/target/streams/compile/compileIncremental/$global/streams/export
 create mode 100755 providence-play/target/streams/compile/compileIncremental/$global/streams/out
 create mode 100755 providence-play/target/streams/compile/copyResources/$global/streams/copy-resources.gz
 create mode 100755 providence-play/target/streams/compile/copyResources/$global/streams/out
 create mode 100755 providence-play/target/streams/compile/dependencyClasspath/$global/streams/export
 create mode 100755 providence-play/target/streams/compile/doc/$global/streams/export
 create mode 100755 providence-play/target/streams/compile/doc/$global/streams/out
 create mode 100755 providence-play/target/streams/compile/doc/$global/streams/scala/inputs
 create mode 100755 providence-play/target/streams/compile/doc/$global/streams/scala/output
 create mode 100755 providence-play/target/streams/compile/exportedProducts/$global/streams/export
 create mode 100755 providence-play/target/streams/compile/externalDependencyClasspath/$global/streams/export
 create mode 100755 providence-play/target/streams/compile/incCompileSetup/$global/streams/inc_compile_2.11
 create mode 100755 providence-play/target/streams/compile/internalDependencyClasspath/$global/streams/export
 create mode 100755 providence-play/target/streams/compile/managedClasspath/$global/streams/export
 create mode 100755 providence-play/target/streams/compile/packageBin/$global/streams/inputs
 create mode 100755 providence-play/target/streams/compile/packageBin/$global/streams/out
 create mode 100755 providence-play/target/streams/compile/packageBin/$global/streams/output
 create mode 100755 providence-play/target/streams/compile/packageDoc/$global/streams/inputs
 create mode 100755 providence-play/target/streams/compile/packageDoc/$global/streams/out
 create mode 100755 providence-play/target/streams/compile/packageDoc/$global/streams/output
 create mode 100755 providence-play/target/streams/compile/packageSrc/$global/streams/inputs
 create mode 100755 providence-play/target/streams/compile/packageSrc/$global/streams/out
 create mode 100755 providence-play/target/streams/compile/packageSrc/$global/streams/output
 create mode 100755 providence-play/target/streams/compile/playRoutes/$global/streams/op-cache
 create mode 100755 providence-play/target/streams/compile/twirlCompileTemplates/$global/streams/out
 create mode 100755 providence-play/target/streams/compile/unmanagedClasspath/$global/streams/export
 create mode 100755 providence-play/target/streams/compile/unmanagedJars/$global/streams/export
 create mode 100755 providence-play/target/streams/runtime/dependencyClasspath/$global/streams/export
 create mode 100755 providence-play/target/streams/runtime/exportedProducts/$global/streams/export
 create mode 100755 providence-play/target/streams/runtime/externalDependencyClasspath/$global/streams/export
 create mode 100755 providence-play/target/streams/runtime/internalDependencyClasspath/$global/streams/export
 create mode 100755 providence-play/target/streams/runtime/managedClasspath/$global/streams/export
 create mode 100755 providence-play/target/streams/runtime/unmanagedClasspath/$global/streams/export
 create mode 100755 providence-play/target/streams/runtime/unmanagedJars/$global/streams/export
 create mode 100755 providence-play/target/streams/universal/dist/$global/streams/out
 create mode 100755 providence-play/target/streams/web-assets/assets/$global/streams/sync-mappings.gz
 create mode 100755 providence-play/target/streams/web-assets/coffeescript/$global/streams/run/op-cache
 create mode 100755 providence-play/target/streams/web-assets/jshint/$global/streams/run/op-cache
 create mode 100755 providence-play/target/streams/web-assets/less/$global/streams/run/op-cache
 create mode 100755 providence-play/target/streams/web-assets/packageBin/$global/streams/inputs
 create mode 100755 providence-play/target/streams/web-assets/packageBin/$global/streams/out
 create mode 100755 providence-play/target/streams/web-assets/packageBin/$global/streams/output
 create mode 100755 providence-play/target/streams/web-assets/webExportedDirectory/$global/streams/sync-mappings.gz
 create mode 100755 providence-play/target/universal/providence-play-1.0-SNAPSHOT.zip
 create mode 100755 providence-play/target/universal/tmp/bin/providence-play
 create mode 100755 providence-play/target/universal/tmp/bin/providence-play.bat
 create mode 100755 providence-play/target/web/public/main/images/favicon.png
 create mode 100755 providence-play/target/web/public/main/javascripts/hello.js
 create mode 100755 providence-play/target/web/public/main/stylesheets/main.css
 create mode 100755 providence-play/test/ApplicationSpec.scala
 create mode 100755 providence-play/test/IntegrationSpec.scala
 create mode 100755 providence-prediction/.settings/org.eclipse.jdt.core.prefs
 create mode 100755 providence-prediction/README.txt
 create mode 100755 providence-prediction/_DS_Store
 create mode 100755 providence-prediction/_cache-main
 create mode 100755 providence-prediction/_classpath.xml
 create mode 100755 providence-prediction/_project.xml
 create mode 100755 providence-prediction/bin/classification/R/R$$anonfun$saveCSVfromSVM$1.class
 create mode 100755 providence-prediction/bin/classification/R/R$$anonfun$saveCSVfromSVM$2$$anonfun$apply$1$$anonfun$1.class
 create mode 100755 providence-prediction/bin/classification/R/R$$anonfun$saveCSVfromSVM$2$$anonfun$apply$1.class
 create mode 100755 providence-prediction/bin/classification/R/R$$anonfun$saveCSVfromSVM$2$$anonfun$apply$2.class
 create mode 100755 providence-prediction/bin/classification/R/R$$anonfun$saveCSVfromSVM$2.class
 create mode 100755 providence-prediction/bin/classification/R/R$.class
 create mode 100755 providence-prediction/bin/classification/R/R.class
 create mode 100755 providence-prediction/bin/classification/model/ModelThomas$$anonfun$1.class
 create mode 100755 providence-prediction/bin/classification/model/ModelThomas$$anonfun$2.class
 create mode 100755 providence-prediction/bin/classification/model/ModelThomas$$anonfun$3.class
 create mode 100755 providence-prediction/bin/classification/model/ModelThomas$$anonfun$getDirectViewsPredictions$1.class
 create mode 100755 providence-prediction/bin/classification/model/ModelThomas$$anonfun$getFacebookViewsPredictions$1.class
 create mode 100755 providence-prediction/bin/classification/model/ModelThomas$$anonfun$getTwitterViewsPredictions$1.class
 create mode 100755 providence-prediction/bin/classification/model/ModelThomas$$anonfun$getViewsFit$1.class
 create mode 100755 providence-prediction/bin/classification/model/ModelThomas$$anonfun$getViewsFit$2.class
 create mode 100755 providence-prediction/bin/classification/model/ModelThomas$$anonfun$getViewsFit$3.class
 create mode 100755 providence-prediction/bin/classification/model/ModelThomas$$anonfun$getViewsFitUntil$1.class
 create mode 100755 providence-prediction/bin/classification/model/ModelThomas$$anonfun$getViewsFitUntil$2.class
 create mode 100755 providence-prediction/bin/classification/model/ModelThomas$.class
 create mode 100755 providence-prediction/bin/classification/model/ModelThomas.class
 create mode 100755 providence-prediction/bin/classification/python/Python$$anonfun$evaluation$1.class
 create mode 100755 providence-prediction/bin/classification/python/Python$$anonfun$saveCSVfromSVM$1$$anonfun$apply$1$$anonfun$1.class
 create mode 100755 providence-prediction/bin/classification/python/Python$$anonfun$saveCSVfromSVM$1$$anonfun$apply$1.class
 create mode 100755 providence-prediction/bin/classification/python/Python$$anonfun$saveCSVfromSVM$1$$anonfun$apply$2.class
 create mode 100755 providence-prediction/bin/classification/python/Python$$anonfun$saveCSVfromSVM$1.class
 create mode 100755 providence-prediction/bin/classification/python/Python$$anonfun$setPredictions$1.class
 create mode 100755 providence-prediction/bin/classification/python/Python$$anonfun$setPredictions$2.class
 create mode 100755 providence-prediction/bin/classification/python/Python$.class
 create mode 100755 providence-prediction/bin/classification/python/Python.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$17.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$18.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$19.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$24.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$25.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$26.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$adaptPredications$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$1$$anonfun$apply$mcVI$sp$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$1$$anonfun$apply$mcVI$sp$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$1$$anonfun$apply$mcVI$sp$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$1$$anonfun$apply$mcVI$sp$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$1$$anonfun$apply$mcVI$sp$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$10.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$11.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$2$$anonfun$13.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$2$$anonfun$14.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$3$$anonfun$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$4$$anonfun$15.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$4$$anonfun$16.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$5$$anonfun$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$7.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$8$$anonfun$apply$15.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$8.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeatures$9.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesBaseline$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesBaseline$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesBaseline$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesBaseline$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesBaseline$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesBaseline$6$$anonfun$apply$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesBaseline$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesBaseline$7$$anonfun$apply$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesBaseline$7.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$1$$anonfun$apply$mcVI$sp$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$1$$anonfun$apply$mcVI$sp$7.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$1$$anonfun$apply$mcVI$sp$8.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$10.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$11.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$2$$anonfun$20.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$2$$anonfun$21.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$3$$anonfun$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$4$$anonfun$22.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$4$$anonfun$23.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$5$$anonfun$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$7.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$8$$anonfun$apply$16.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$8.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$classification$svm$ProcessData$$getFeaturesFacebookPush$9.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$evaluation$1$$anonfun$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$evaluation$1$$anonfun$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$evaluation$1$$anonfun$7.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$evaluation$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$evaluation$2$$anonfun$10.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$evaluation$2$$anonfun$8.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$evaluation$2$$anonfun$9.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$evaluation$2$$anonfun$apply$18.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$evaluation$2$$anonfun$apply$19.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$evaluation$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$getFeaturesNames$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$getFeaturesNames$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$getFeaturesNames$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$getFeaturesNames$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$getFeaturesNames$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$getFeaturesNames$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$init$1$$anonfun$apply$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$init$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$init$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$init$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$init$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$initBaselines$1$$anonfun$11.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$initBaselines$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$loadFeatures$1$$anonfun$12.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$loadFeatures$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$saveData$1$$anonfun$apply$7.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$saveData$1$$anonfun$apply$8.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$saveData$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$saveDataBaseline$1$$anonfun$apply$11.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$saveDataBaseline$1$$anonfun$apply$12.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$saveDataBaseline$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$saveDataBaselineCluster$1$$anonfun$apply$10.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$saveDataBaselineCluster$1$$anonfun$apply$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$saveDataBaselineCluster$1$$anonfun$apply$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$saveDataBaselineCluster$1$$anonfun$apply$9.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$saveDataBaselineCluster$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$saveDataFacebookPush$1$$anonfun$apply$13.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$saveDataFacebookPush$1$$anonfun$apply$14.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$saveDataFacebookPush$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$setLabels$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$setPredictions$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$setPredictions2$1$$anonfun$apply$17.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$setPredictions2$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$setPushes$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$setPushes$2$$anonfun$apply$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$$anonfun$setPushes$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData$.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessData.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$10.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$11.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$14.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$15.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getBasicFeatures$1$$anonfun$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getBasicFeatures$1$$anonfun$7.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getBasicFeatures$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getBasicFeatures$2$$anonfun$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getBasicFeatures$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getBasicFeatures$3$$anonfun$8.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getBasicFeatures$3$$anonfun$9.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getBasicFeatures$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getBasicFeatures$4$$anonfun$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getBasicFeatures$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getBasicFeaturesNewsmonkey$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getBasicFeaturesNewsmonkey$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getBasicFeaturesNewsmonkey$3$$anonfun$apply$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getBasicFeaturesNewsmonkey$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getFacebookFeatures$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getFacebookFeatures$2$$anonfun$12.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getFacebookFeatures$2$$anonfun$13.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getFacebookFeatures$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getFacebookFeatures$3$$anonfun$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getFacebookFeatures$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getViewFeatures$1$$anonfun$apply$mcVI$sp$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getViewFeatures$1$$anonfun$apply$mcVI$sp$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getViewFeatures$1$$anonfun$apply$mcVI$sp$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$getViewFeatures$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$init$1$$anonfun$apply$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$init$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$init$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$init$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$init$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$loadFeatures$1$$anonfun$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$loadFeatures$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$loadFeaturesFromDir$1$$anonfun$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$loadFeaturesFromDir$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$loadMaps$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$loadMaps$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$loadMaps$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$loadMaps$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$loadMaps$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI$$anonfun$loadMaps$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataAPI.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$classification$svm$ProcessDataBasic$$getFeatures$1$$anonfun$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$classification$svm$ProcessDataBasic$$getFeatures$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$classification$svm$ProcessDataBasic$$getFeatures$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$classification$svm$ProcessDataBasic$$getFeatures$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$classification$svm$ProcessDataBasic$$getFeatures$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$classification$svm$ProcessDataBasic$$getFeatures$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$classification$svm$ProcessDataBasic$$getFeatures$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$classification$svm$ProcessDataBasic$$getFeatures$7.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$classification$svm$ProcessDataBasic$$getFeatures$8.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$classification$svm$ProcessDataBasic$$getFeatures$9.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$evaluation$1$$anonfun$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$evaluation$1$$anonfun$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$evaluation$1$$anonfun$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$evaluation$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$evaluation$2$$anonfun$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$evaluation$2$$anonfun$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$evaluation$2$$anonfun$7.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$evaluation$2$$anonfun$apply$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$evaluation$2$$anonfun$apply$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$evaluation$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$init$1$$anonfun$apply$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$init$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$init$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$init$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$init$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$loadFeatures$1$$anonfun$8.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$loadFeatures$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$saveData$1$$anonfun$apply$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$saveData$1$$anonfun$apply$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$saveData$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$$anonfun$setLabels$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic$.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataBasic.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$17.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$18.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$19.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$22.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$23.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$28.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$29.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$30.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$1$$anonfun$apply$mcVI$sp$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$1$$anonfun$apply$mcVI$sp$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$1$$anonfun$apply$mcVI$sp$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$1$$anonfun$apply$mcVI$sp$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$1$$anonfun$apply$mcVI$sp$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$10.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$11.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$12.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$13.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$14$$anonfun$20.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$14$$anonfun$21.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$14.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$2$$anonfun$13.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$2$$anonfun$14.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$3$$anonfun$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$4$$anonfun$15.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$4$$anonfun$16.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$5$$anonfun$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$7.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$8$$anonfun$apply$25.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$8.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeatures$9.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$10.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$11.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$12$$anonfun$apply$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$12.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$13$$anonfun$apply$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$13.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$14$$anonfun$apply$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$14.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$15$$anonfun$apply$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$15.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$16$$anonfun$apply$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$16.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$17$$anonfun$apply$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$17.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$7.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$8.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesAllBaselines$9.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$classification$svm$ProcessDataNewsmonkey$$getFeaturesBaseline$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$evaluation$1$$anonfun$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$evaluation$1$$anonfun$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$evaluation$1$$anonfun$7.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$evaluation$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$evaluation$2$$anonfun$10.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$evaluation$2$$anonfun$8.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$evaluation$2$$anonfun$9.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$evaluation$2$$anonfun$apply$26.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$evaluation$2$$anonfun$apply$27.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$evaluation$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$10.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$11.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$12.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$13.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$3$$anonfun$apply$mcVI$sp$10.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$3$$anonfun$apply$mcVI$sp$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$3$$anonfun$apply$mcVI$sp$7.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$3$$anonfun$apply$mcVI$sp$8.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$3$$anonfun$apply$mcVI$sp$9.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$4$$anonfun$24.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$4$$anonfun$25.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$5$$anonfun$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$6$$anonfun$26.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$6$$anonfun$27.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$7$$anonfun$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$7.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$8.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$getFeaturesNames$9.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$init$1$$anonfun$apply$16.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$init$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$init$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$init$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$init$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$initAllBaselines$1$$anonfun$11.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$initAllBaselines$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$initCurveFeatures$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$initCurveFeatures$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$initCurveFeatures$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$loadFeatures$1$$anonfun$12.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$loadFeatures$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveData$1$$anonfun$apply$17.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveData$1$$anonfun$apply$18.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveData$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataAllBaselines$1$$anonfun$apply$19.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataAllBaselines$1$$anonfun$apply$20.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataAllBaselines$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataBaseline$1$$anonfun$apply$21.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataBaseline$1$$anonfun$apply$22.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataBaseline$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataBaselineCluster$1$$anonfun$apply$10.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataBaselineCluster$1$$anonfun$apply$11.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataBaselineCluster$1$$anonfun$apply$12.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataBaselineCluster$1$$anonfun$apply$13.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataBaselineCluster$1$$anonfun$apply$14.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataBaselineCluster$1$$anonfun$apply$15.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataBaselineCluster$1$$anonfun$apply$23.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataBaselineCluster$1$$anonfun$apply$24.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataBaselineCluster$1$$anonfun$apply$7.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataBaselineCluster$1$$anonfun$apply$8.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataBaselineCluster$1$$anonfun$apply$9.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey$$anonfun$saveDataBaselineCluster$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataNewsmonkey.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$10.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$13.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$14.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$8.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$9.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$1$$anonfun$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$1$$anonfun$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$2$$anonfun$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$3$$anonfun$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$3$$anonfun$7.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$4$$anonfun$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeatures$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeaturesNewsmonkey$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeaturesNewsmonkey$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeaturesNewsmonkey$3$$anonfun$apply$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeaturesNewsmonkey$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeaturesNewsmonkey$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeaturesNewsmonkey$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicFeaturesNewsmonkey$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicPopularityFeatures$1$$anonfun$apply$mcVI$sp$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicPopularityFeatures$1$$anonfun$apply$mcVI$sp$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicPopularityFeatures$1$$anonfun$apply$mcVI$sp$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicPopularityFeatures$1$$anonfun$apply$mcVI$sp$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicPopularityFeatures$1$$anonfun$apply$mcVI$sp$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getBasicPopularityFeatures$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getFacebookFeatures$1$$anonfun$11.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getFacebookFeatures$1$$anonfun$12.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$getFacebookFeatures$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$loadFeatures$1$$anonfun$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$loadFeatures$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$loadMaps$1.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$loadMaps$2.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$loadMaps$3.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$loadMaps$4.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$loadMaps$5.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF$$anonfun$loadMaps$6.class
 create mode 100755 providence-prediction/bin/classification/svm/ProcessDataRF.class
 create mode 100755 providence-prediction/bin/classification/svm/SVMlinear.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/ArraySorter.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/DoubleArrayPointer.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/FeatureNode.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/Function.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/IntArrayPointer.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/InvalidInputDataException.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/L2R_L2_SvcFunction.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/L2R_LrFunction.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/Linear$GroupClassesReturn.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/Linear.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/Model.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/Parameter.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/Predict.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/PredictOnline.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/Problem.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/README.md
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/Record.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/SolverMCSVM_CS.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/SolverType.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/Train.class
 create mode 100755 providence-prediction/bin/classification/svm/liblinear/Tron.class
 create mode 100755 providence-prediction/bin/classification/weka/Weka$$anonfun$evaluation$1.class
 create mode 100755 providence-prediction/bin/classification/weka/Weka$$anonfun$saveARFFfromSVM$1.class
 create mode 100755 providence-prediction/bin/classification/weka/Weka$$anonfun$saveARFFfromSVM$2$$anonfun$apply$1.class
 create mode 100755 providence-prediction/bin/classification/weka/Weka$$anonfun$saveARFFfromSVM$2.class
 create mode 100755 providence-prediction/bin/classification/weka/Weka$$anonfun$saveARFFfromSVMNoCategory$1.class
 create mode 100755 providence-prediction/bin/classification/weka/Weka$$anonfun$saveARFFfromSVMNoCategory$2$$anonfun$apply$2.class
 create mode 100755 providence-prediction/bin/classification/weka/Weka$$anonfun$saveARFFfromSVMNoCategory$2.class
 create mode 100755 providence-prediction/bin/classification/weka/Weka$$anonfun$setPredictions$1.class
 create mode 100755 providence-prediction/bin/classification/weka/Weka$.class
 create mode 100755 providence-prediction/bin/classification/weka/Weka.class
 create mode 100755 providence-prediction/bin/classification/weka/WekaClassifier$$anonfun$predict$1.class
 create mode 100755 providence-prediction/bin/classification/weka/WekaClassifier.class
 create mode 100755 providence-prediction/bin/core/Config$.class
 create mode 100755 providence-prediction/bin/core/Config.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$11.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$30.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$31.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$32.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$33.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$45.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$46.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$47.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$48.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$49.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$50.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$51.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$52.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$54.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$55.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$57.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$adaptNewsmonkeyMonitoredData$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$adaptNewsmonkeyMonitoredData$2$$anonfun$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$adaptNewsmonkeyMonitoredData$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$adaptNewsmonkeyMonitoredData$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$adaptNewsmonkeyMonitoredData$4$$anonfun$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$adaptNewsmonkeyMonitoredData$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$adaptNewsmonkeyMonitoredDataNotFinalPopularity$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$adaptNewsmonkeyMonitoredDataNotFinalPopularity$2$$anonfun$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$adaptNewsmonkeyMonitoredDataNotFinalPopularity$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$adaptNewsmonkeyMonitoredDataNotFinalPopularity$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$adaptNewsmonkeyMonitoredDataNotFinalPopularity$4$$anonfun$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$adaptNewsmonkeyMonitoredDataNotFinalPopularity$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$averagePopularityPerHour$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$averagePopularityPerHour$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$averagePopularityPerHour$3$$anonfun$apply$124.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$averagePopularityPerHour$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$averagePopularityPerHour$4$$anonfun$apply$125.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$averagePopularityPerHour$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures$1$$anonfun$apply$150$$anonfun$apply$151$$anonfun$apply$67.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures$1$$anonfun$apply$150$$anonfun$apply$151$$anonfun$apply$68.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures$1$$anonfun$apply$150$$anonfun$apply$151.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures$1$$anonfun$apply$150.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures$1$$anonfun$apply$152.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures$1$$anonfun$apply$153$$anonfun$apply$154$$anonfun$apply$69.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures$1$$anonfun$apply$153$$anonfun$apply$154.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures$1$$anonfun$apply$153.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures$1$$anonfun$apply$155.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures$1$$anonfun$apply$156.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures$1$$anonfun$apply$157.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$1$$anonfun$apply$mcVI$sp$90.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$10$$anonfun$apply$142$$anonfun$apply$143$$anonfun$apply$64.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$10$$anonfun$apply$142$$anonfun$apply$143$$anonfun$apply$65.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$10$$anonfun$apply$142$$anonfun$apply$143.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$10$$anonfun$apply$142.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$10$$anonfun$apply$144.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$10$$anonfun$apply$145$$anonfun$apply$146$$anonfun$apply$66.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$10$$anonfun$apply$145$$anonfun$apply$146.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$10$$anonfun$apply$145.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$10$$anonfun$apply$147.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$10$$anonfun$apply$148.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$10$$anonfun$apply$149.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$10.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$2$$anonfun$apply$mcVI$sp$91.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$3$$anonfun$apply$mcVI$sp$92.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeatures5Fold$9.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesAverages$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesAverages$2$$anonfun$9.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesAverages$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesAverages$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesAverages$4$$anonfun$10.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesAverages$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesAverages$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesAverages$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesAverages$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesAverages$8$$anonfun$apply$158$$anonfun$apply$70.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesAverages$8$$anonfun$apply$158$$anonfun$apply$71.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesAverages$8$$anonfun$apply$158.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesAverages$8$$anonfun$apply$159.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesAverages$8$$anonfun$apply$72.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesAverages$8$$anonfun$apply$73.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesAverages$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesFacebookPush$1$$anonfun$apply$160$$anonfun$apply$161$$anonfun$apply$74.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesFacebookPush$1$$anonfun$apply$160$$anonfun$apply$161$$anonfun$apply$75.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesFacebookPush$1$$anonfun$apply$160$$anonfun$apply$161.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesFacebookPush$1$$anonfun$apply$160.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesFacebookPush$1$$anonfun$apply$162.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesFacebookPush$1$$anonfun$apply$163$$anonfun$apply$164$$anonfun$apply$76.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesFacebookPush$1$$anonfun$apply$163$$anonfun$apply$164.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesFacebookPush$1$$anonfun$apply$163.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesFacebookPush$1$$anonfun$apply$165.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesFacebookPush$1$$anonfun$apply$166.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesFacebookPush$1$$anonfun$apply$167.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesFacebookPush$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesRFTrainingDeredactie$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesRFTrainingNewsmonkey$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesRFTrainingNewsmonkey$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesRFTrainingNewsmonkey$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesRFTrainingNewsmonkey$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesRFTrainingNewsmonkey$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesRFTrainingNewsmonkey$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesTraining$1$$anonfun$apply$134$$anonfun$apply$135$$anonfun$apply$61.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesTraining$1$$anonfun$apply$134$$anonfun$apply$135$$anonfun$apply$62.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesTraining$1$$anonfun$apply$134$$anonfun$apply$135.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesTraining$1$$anonfun$apply$134.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesTraining$1$$anonfun$apply$136.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesTraining$1$$anonfun$apply$137$$anonfun$apply$138$$anonfun$apply$63.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesTraining$1$$anonfun$apply$137$$anonfun$apply$138.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesTraining$1$$anonfun$apply$137.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesTraining$1$$anonfun$apply$139.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesTraining$1$$anonfun$apply$140.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesTraining$1$$anonfun$apply$141.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$calculateFeaturesTraining$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify$3$$anonfun$apply$56$$anonfun$apply$mcVI$sp$88.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify$3$$anonfun$apply$56.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5Fold$1$$anonfun$apply$mcVI$sp$27.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5Fold$1$$anonfun$apply$mcVI$sp$82.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5Fold$1$$anonfun$apply$mcVI$sp$83.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5Fold$1$$anonfun$apply$mcVI$sp$84.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5Fold$1$$anonfun$apply$mcVI$sp$85.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5Fold$1$$anonfun$apply$mcVI$sp$86.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5Fold$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5Fold$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5Fold$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5Fold$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5Fold$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldBaseline$1$$anonfun$apply$mcVI$sp$19.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldBaseline$1$$anonfun$apply$mcVI$sp$75.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldBaseline$1$$anonfun$apply$mcVI$sp$76.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldBaseline$1$$anonfun$apply$mcVI$sp$77.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldBaseline$1$$anonfun$apply$mcVI$sp$78.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldBaseline$1$$anonfun$apply$mcVI$sp$79.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldBaseline$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldBaseline$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldBaseline$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldBaseline$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldModelThomas$1$$anonfun$apply$mcVI$sp$17$$anonfun$apply$mcVI$sp$72.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldModelThomas$1$$anonfun$apply$mcVI$sp$17.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldModelThomas$1$$anonfun$apply$mcVI$sp$71.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldModelThomas$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldModelThomas$2$$anonfun$apply$mcVI$sp$18$$anonfun$apply$mcVI$sp$74.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldModelThomas$2$$anonfun$apply$mcVI$sp$18.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldModelThomas$2$$anonfun$apply$mcVI$sp$73.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldModelThomas$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldModelThomas$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldModelThomasRandomForest$1$$anonfun$apply$mcVI$sp$15$$anonfun$apply$mcVI$sp$69.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldModelThomasRandomForest$1$$anonfun$apply$mcVI$sp$15.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldModelThomasRandomForest$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldModelThomasRandomForest$2$$anonfun$apply$mcVI$sp$16$$anonfun$apply$mcVI$sp$70.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldModelThomasRandomForest$2$$anonfun$apply$mcVI$sp$16.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldModelThomasRandomForest$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classify5FoldModelThomasRandomForest$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyAPI$1$$anonfun$apply$mcVI$sp$87$$anonfun$apply$130.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyAPI$1$$anonfun$apply$mcVI$sp$87$$anonfun$apply$131.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyAPI$1$$anonfun$apply$mcVI$sp$87.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyAPI$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyAPI$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyAPI$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyAPI$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyAPI$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyAPI$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBaselines$1$$anonfun$apply$mcVI$sp$36.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBaselines$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBaselinesFolds$1$$anonfun$apply$mcVI$sp$1$$anonfun$apply$mcVI$sp$35.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBaselinesFolds$1$$anonfun$apply$mcVI$sp$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBaselinesFolds$1$$anonfun$apply$mcVI$sp$34.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBaselinesFolds$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBaselinesFolds$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBasic$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBasic$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBasic$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBasic$4$$anonfun$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBasic$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBasic$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBasic$6$$anonfun$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBasic$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBasic$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBasic$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBasic$9.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBasicCombine$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBasicCombine$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBasicCombine$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyBasicCombine$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyFacebookPush$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyRFderedactie$1$$anonfun$apply$mcVI$sp$80$$anonfun$apply$126.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyRFderedactie$1$$anonfun$apply$mcVI$sp$80$$anonfun$apply$127.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyRFderedactie$1$$anonfun$apply$mcVI$sp$80.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyRFderedactie$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyRFderedactie$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyTestBaselines$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyTestBaselines$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyTestBaselines$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyTestBaselines$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyTestBaselines$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyTestBaselines$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyTestBaselines$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyTestBaselines$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyTestBaselines$9.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyTraining$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyTraining$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyTraining$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyTraining$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyTraining$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyTraining$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$classifyTraining$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$cleanDeredactie$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$cleanNewsmonkey$1$$anonfun$apply$85.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$cleanNewsmonkey$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$clusterBaselines$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$clusterBaselines$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$clusterBaselines$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$clusterBaselines$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValue$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValue$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValue$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValue$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$10.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$11.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$12.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$13.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$14.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$15.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$16.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$17.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$18.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$19.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$20.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$21.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$22.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$23.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$24.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$25.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$26.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$27.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$28.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$29.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$30.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$31.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$32.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$33.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$34.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$35.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$36.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$37.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$38.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$39.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$40.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$41.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$42.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$43.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$44.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$45.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$46.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$47.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$48.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$49.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$50.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$51.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$52.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$53.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$54.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$55.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$56.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$57.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$58.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$59.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$60.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$61.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$62.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$63.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$64.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$65.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$66.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$67.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$68.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$69.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$70.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$71.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$72.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$73.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$74.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$75.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$76.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$core$Main$$getFeatureValueAverages$9.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNorm$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNorm$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNorm$3$$anonfun$apply$49$$anonfun$apply$mcVD$sp$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNorm$3$$anonfun$apply$49$$anonfun$apply$mcVD$sp$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNorm$3$$anonfun$apply$49.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNorm$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNorm2$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNorm2$2$$anonfun$apply$115.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNorm2$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$2$$anonfun$apply$100.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$2$$anonfun$apply$101.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$2$$anonfun$apply$102$$anonfun$apply$50$$anonfun$apply$mcVD$sp$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$2$$anonfun$apply$102$$anonfun$apply$50$$anonfun$apply$mcVD$sp$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$2$$anonfun$apply$102$$anonfun$apply$50.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$2$$anonfun$apply$102.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$2$$anonfun$apply$99.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$3$$anonfun$apply$103.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$3$$anonfun$apply$104.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$3$$anonfun$apply$105.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$3$$anonfun$apply$106$$anonfun$apply$51$$anonfun$apply$mcVD$sp$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$3$$anonfun$apply$106$$anonfun$apply$51$$anonfun$apply$mcVD$sp$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$3$$anonfun$apply$106$$anonfun$apply$51.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$3$$anonfun$apply$106.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent2$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent2$2$$anonfun$apply$107.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent2$2$$anonfun$apply$108.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent2$2$$anonfun$apply$109$$anonfun$apply$110.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent2$2$$anonfun$apply$109.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent2$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent2$3$$anonfun$apply$111.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent2$3$$anonfun$apply$112.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent2$3$$anonfun$apply$113$$anonfun$apply$114.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent2$3$$anonfun$apply$113.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitLogNormPerComponent2$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitModelThomas$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitModelThomas$2$$anonfun$apply$116$$anonfun$apply$117.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitModelThomas$2$$anonfun$apply$116$$anonfun$apply$118.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitModelThomas$2$$anonfun$apply$116$$anonfun$apply$119.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitModelThomas$2$$anonfun$apply$116.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitModelThomas$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitModelThomas$3$$anonfun$apply$120$$anonfun$apply$121.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitModelThomas$3$$anonfun$apply$120$$anonfun$apply$122.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitModelThomas$3$$anonfun$apply$120$$anonfun$apply$123.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitModelThomas$3$$anonfun$apply$120.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$curveFitModelThomas$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$entityExtraction$1$$anonfun$apply$90.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$entityExtraction$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitLogNorm$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitLogNorm$2$$anonfun$apply$31.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitLogNorm$2$$anonfun$apply$32.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitLogNorm$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitLogNorm$3$$anonfun$apply$33.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitLogNorm$3$$anonfun$apply$34.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitLogNorm$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitLogNormPerComponent$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitLogNormPerComponent$2$$anonfun$apply$35.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitLogNormPerComponent$2$$anonfun$apply$36.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitLogNormPerComponent$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitLogNormPerComponent$3$$anonfun$apply$37.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitLogNormPerComponent$3$$anonfun$apply$38.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitLogNormPerComponent$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitModelThomas$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitModelThomas$2$$anonfun$apply$39.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitModelThomas$2$$anonfun$apply$40.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateCurveFitModelThomas$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateModelSignificant$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateModelSignificant$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateModelSignificant$3$$anonfun$apply$mcVI$sp$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateModelSignificant$3$$anonfun$apply$mcVI$sp$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateModelSignificant$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateModelSignificant$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateModelSignificant$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5Fold$1$$anonfun$apply$mcVI$sp$11$$anonfun$apply$mcVI$sp$58.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5Fold$1$$anonfun$apply$mcVI$sp$11.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5Fold$1$$anonfun$apply$mcVI$sp$56.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5Fold$1$$anonfun$apply$mcVI$sp$57.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5Fold$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5Fold$2$$anonfun$apply$mcVI$sp$59.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5Fold$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5Fold$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldBaseline$1$$anonfun$apply$mcVI$sp$3$$anonfun$apply$mcVI$sp$39.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldBaseline$1$$anonfun$apply$mcVI$sp$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldBaseline$1$$anonfun$apply$mcVI$sp$37.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldBaseline$1$$anonfun$apply$mcVI$sp$38.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldBaseline$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldBaseline$2$$anonfun$apply$mcVI$sp$40.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldBaseline$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldBaseline$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldModelThomas$1$$anonfun$apply$mcVI$sp$10$$anonfun$apply$mcVI$sp$54.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldModelThomas$1$$anonfun$apply$mcVI$sp$10.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldModelThomas$1$$anonfun$apply$mcVI$sp$52.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldModelThomas$1$$anonfun$apply$mcVI$sp$53.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldModelThomas$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldModelThomas$2$$anonfun$apply$mcVI$sp$55.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldModelThomas$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldModelThomas$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldModelThomasRandomForest$1$$anonfun$apply$mcVI$sp$49.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldModelThomasRandomForest$1$$anonfun$apply$mcVI$sp$9$$anonfun$apply$mcVI$sp$50.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldModelThomasRandomForest$1$$anonfun$apply$mcVI$sp$9.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldModelThomasRandomForest$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldModelThomasRandomForest$2$$anonfun$apply$mcVI$sp$51.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldModelThomasRandomForest$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluatePredictions5FoldModelThomasRandomForest$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateSignificant$1$$anonfun$apply$mcVI$sp$45.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateSignificant$1$$anonfun$apply$mcVI$sp$46.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateSignificant$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateSignificant$2$$anonfun$apply$mcVI$sp$47.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateSignificant$2$$anonfun$apply$mcVI$sp$48.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateSignificant$2$$anonfun$apply$mcVI$sp$6$$anonfun$apply$mcVI$sp$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateSignificant$2$$anonfun$apply$mcVI$sp$6$$anonfun$apply$mcVI$sp$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateSignificant$2$$anonfun$apply$mcVI$sp$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateSignificant$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateSignificant$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateSignificant$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateSignificant$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateSignificant$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTestBaselines$1$$anonfun$apply$mcVI$sp$41.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTestBaselines$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTestBaselines$10.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTestBaselines$2$$anonfun$apply$mcVI$sp$42.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTestBaselines$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTestBaselines$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTestBaselines$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTestBaselines$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTestBaselines$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTestBaselines$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTestBaselines$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTestBaselines$9.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTraining$1$$anonfun$apply$mcVI$sp$43.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTraining$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTraining$10.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTraining$2$$anonfun$apply$mcVI$sp$44.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTraining$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTraining$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTraining$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTraining$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTraining$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTraining$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTraining$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$evaluateTraining$9.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getBasicStats$1$$anonfun$apply$14.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getBasicStats$1$$anonfun$apply$15.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getBasicStats$1$$anonfun$apply$16.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getBasicStats$1$$anonfun$apply$17.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getBasicStats$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getBasicStats$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getBasicStats$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getBasicStats$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getBasicStats$5$$anonfun$apply$82.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getBasicStats$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getBasicStats$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getBasicStats$7$$anonfun$apply$83.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getBasicStats$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getBasicStats$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getBasicStats$9$$anonfun$apply$84.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getBasicStats$9.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getDeredactieMonitoredData$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getDeredactieMonitoredData$2$$anonfun$20.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getDeredactieMonitoredData$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getDeredactieMonitoredData$3$$anonfun$21.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getDeredactieMonitoredData$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getDeredactieMonitoredData$4$$anonfun$22.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getDeredactieMonitoredData$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getDeredactieMonitoredData$5$$anonfun$23.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getDeredactieMonitoredData$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getDeredactieMonitoredData$6$$anonfun$24.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getDeredactieMonitoredData$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getExampleArticles$1$$anonfun$25.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getExampleArticles$1$$anonfun$26.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getExampleArticles$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getExampleArticles$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getExampleArticles$3$$anonfun$apply$77.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getExampleArticles$3$$anonfun$apply$78.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getExampleArticles$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getFeatureNamesTraining$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getFeatureNamesTraining$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getFeatureNamesTraining$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getFeatureNamesTraining$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getFeatureNamesTraining$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getFeatures$1$$anonfun$apply$mcVI$sp$29.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getFeatures$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getIdsAndPopularity$1$$anonfun$apply$86$$anonfun$28.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getIdsAndPopularity$1$$anonfun$apply$86.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getIdsAndPopularity$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getIdsAndPopularity$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getManualFeaturesNewsmonkey$1$$anonfun$29.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getManualFeaturesNewsmonkey$1$$anonfun$apply$87.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getManualFeaturesNewsmonkey$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getManualFeaturesNewsmonkey$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getManualFeaturesNewsmonkey$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$2$$anonfun$12.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$3$$anonfun$13.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$4$$anonfun$14.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$5$$anonfun$15.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$6$$anonfun$16.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$7$$anonfun$17.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$8$$anonfun$18.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$9$$anonfun$19.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getNewsmonkeyMonitoredData$9.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$1$$anonfun$apply$79$$anonfun$apply$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$1$$anonfun$apply$79.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$4$$anonfun$apply$11.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$4$$anonfun$apply$12.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$4$$anonfun$apply$13.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$4$$anonfun$apply$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$4$$anonfun$apply$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$4$$anonfun$apply$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$4$$anonfun$apply$80$$anonfun$apply$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$4$$anonfun$apply$80$$anonfun$apply$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$4$$anonfun$apply$80$$anonfun$apply$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$4$$anonfun$apply$80.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$4$$anonfun$apply$81$$anonfun$apply$10.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$4$$anonfun$apply$81$$anonfun$apply$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$4$$anonfun$apply$81$$anonfun$apply$9.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$4$$anonfun$apply$81.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getSocialPageFeatures$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getStats$1$$anonfun$apply$57.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getStats$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getStats$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getTrainingAndTestsetByTime$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getTrainingAndTestsetByTime$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$getTrainingAndTestsetByTime$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$manualAnnotateEroticTitles$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$manualAnnotateEroticTitles$2$$anonfun$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$manualAnnotateEroticTitles$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$manualAnnotateEroticTitles$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$manualAnnotateEroticTitles$4$$anonfun$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$manualAnnotateEroticTitles$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$manualAnnotateEroticTitles$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$manualAnnotateEroticTitles$6$$anonfun$apply$89.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$manualAnnotateEroticTitles$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$manualAnnotateEroticTitles$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$manualBaseline$1$$anonfun$apply$88.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$manualBaseline$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$mergeDatasets$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$mergeDatasets$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$mergeDatasets$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$mergeDatasets$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$mergeDatasets$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$mergeDatasets$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$mergeDatasets$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$mergeDatasets$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$mergeDatasets$9.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$mergeFeatures$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$mergeFeatures$2$$anonfun$27.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$mergeFeatures$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$mergeFeatures$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveDeredactie$1$$anonfun$apply$25.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveDeredactie$1$$anonfun$apply$26.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveDeredactie$1$$anonfun$apply$27.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveDeredactie$1$$anonfun$apply$91.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveDeredactie$1$$anonfun$apply$92.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveDeredactie$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveDeredactie$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveDeredactie$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveDeredactie$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveDeredactie$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveFitLogNorm$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveFitLogNorm$2$$anonfun$apply$29.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveFitLogNorm$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveFitLogNormPerComponent$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveFitLogNormPerComponent$2$$anonfun$apply$30.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveFitLogNormPerComponent$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveFitModelThomas$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveFitModelThomas$2$$anonfun$apply$28.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotCurveFitModelThomas$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotGraphs$1$$anonfun$apply$20.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$plotGraphs$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityExamples$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityExamples$2$$anonfun$apply$mcVI$sp$20.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityExamples$2$$anonfun$apply$mcVI$sp$21.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityExamples$2$$anonfun$apply$mcVI$sp$22.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityExamples$2$$anonfun$apply$mcVI$sp$23.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityExamples$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityExamples$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityExamples$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityExamples$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityExamples$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityExamples$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityExamples$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityExamples$9$$anonfun$apply$52.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityExamples$9.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerDay$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerDay$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerDay$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$10.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$11$$anonfun$apply$55$$anonfun$apply$mcVI$sp$26.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$11$$anonfun$apply$55.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$11.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$12.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$13.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$3$$anonfun$apply$53$$anonfun$apply$mcVI$sp$24.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$3$$anonfun$apply$53.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$7$$anonfun$apply$54$$anonfun$apply$mcVI$sp$25.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$7$$anonfun$apply$54.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$popularityPerHour$9.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$predictionSeries$1$$anonfun$apply$mcVI$sp$30.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$predictionSeries$1$$anonfun$apply$mcVI$sp$31.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$predictionSeries$1$$anonfun$apply$mcVI$sp$32.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$predictionSeries$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$predictionSeries$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$predictionSeries$3$$anonfun$apply$18.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$predictionSeries$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$predictionSeriesFacebookPush$1$$anonfun$apply$mcVI$sp$33.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$predictionSeriesFacebookPush$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$predictionSeriesFacebookPush$2$$anonfun$apply$19.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$predictionSeriesFacebookPush$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$readAlphas$1$$anonfun$apply$mcVI$sp$28.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$readAlphas$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$saveMaps$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$saveMaps$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$saveMaps$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$saveMaps$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$saveMaps$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$saveMaps$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$saveMapsRF$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$saveMapsRF$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$saveMapsRF$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$saveMapsRF$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$saveMapsRF$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$saveMapsRF$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$1$$anonfun$apply$mcVI$sp$12$$anonfun$apply$mcVI$sp$61.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$1$$anonfun$apply$mcVI$sp$12.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$1$$anonfun$apply$mcVI$sp$60.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$1$$anonfun$apply$mcVI$sp$62$$anonfun$apply$22.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$1$$anonfun$apply$mcVI$sp$62.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$2$$anonfun$34.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$2$$anonfun$apply$mcVI$sp$13$$anonfun$apply$mcVI$sp$64.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$2$$anonfun$apply$mcVI$sp$13.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$2$$anonfun$apply$mcVI$sp$63.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$2$$anonfun$apply$mcVI$sp$65$$anonfun$apply$23.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$2$$anonfun$apply$mcVI$sp$65.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$3$$anonfun$35.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$3$$anonfun$apply$mcVI$sp$14$$anonfun$apply$mcVI$sp$67.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$3$$anonfun$apply$mcVI$sp$14.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$3$$anonfun$apply$mcVI$sp$66.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$3$$anonfun$apply$mcVI$sp$68$$anonfun$apply$24.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$3$$anonfun$apply$mcVI$sp$68.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictions5Fold$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictionsRF$1$$anonfun$apply$21.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictionsRF$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$savePredictionsRF$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$1$$anonfun$apply$mcVI$sp$89.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$10.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$11.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$4$$anonfun$56.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$4$$anonfun$apply$58.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$4$$anonfun$apply$59.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$4$$anonfun$apply$60.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$5$$anonfun$apply$133.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$set5Fold$9.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNorm$1$$anonfun$apply$93.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNorm$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$10$$anonfun$apply$98.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$10.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$11$$anonfun$36.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$11$$anonfun$37.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$11$$anonfun$apply$41.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$11$$anonfun$apply$42.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$11$$anonfun$apply$43.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$11$$anonfun$apply$44.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$11.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$2$$anonfun$apply$94.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$4$$anonfun$apply$95.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$6$$anonfun$apply$96.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$7.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$8$$anonfun$apply$97.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$8.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitLogNormPerComponent$9.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$1$$anonfun$38.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$2$$anonfun$39.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$3$$anonfun$40.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$4$$anonfun$41.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$4.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$5$$anonfun$42.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$5.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$6$$anonfun$43.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$6$$anonfun$44.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$6$$anonfun$apply$45.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$6$$anonfun$apply$46.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$6$$anonfun$apply$47.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$6$$anonfun$apply$48.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setCurveFitModelThomas$6.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setPredictedBaseline$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setPredictedBaseline$2$$anonfun$apply$mcVI$sp$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setPredictedBaseline$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setPredictedBaseline$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setRelatedArticles$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setRelatedArticles$2$$anonfun$apply$132$$anonfun$53.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setRelatedArticles$2$$anonfun$apply$132.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setRelatedArticles$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$setTestset$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$statisticsPaper$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$statisticsPaper$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$statisticsPaper$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$std$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$std$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$std$3.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$testRFderedactie$1$$anonfun$apply$mcVI$sp$81$$anonfun$apply$128.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$testRFderedactie$1$$anonfun$apply$mcVI$sp$81$$anonfun$apply$129.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$testRFderedactie$1$$anonfun$apply$mcVI$sp$81.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$testRFderedactie$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$testRFderedactie$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$zipflaw$1.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$zipflaw$2.class
 create mode 100755 providence-prediction/bin/core/Main$$anonfun$zipflaw$3.class
 create mode 100755 providence-prediction/bin/core/Main$.class
 create mode 100755 providence-prediction/bin/core/Main$delayedInit$body.class
 create mode 100755 providence-prediction/bin/core/Main.class
 create mode 100755 providence-prediction/bin/dao/ArticleDAO$$anonfun$read$1$$anonfun$apply$1.class
 create mode 100755 providence-prediction/bin/dao/ArticleDAO$$anonfun$read$1$$anonfun$apply$2.class
 create mode 100755 providence-prediction/bin/dao/ArticleDAO$$anonfun$read$1$$anonfun$apply$3.class
 create mode 100755 providence-prediction/bin/dao/ArticleDAO$$anonfun$read$1$$anonfun$apply$4.class
 create mode 100755 providence-prediction/bin/dao/ArticleDAO$$anonfun$read$1$$anonfun$apply$5.class
 create mode 100755 providence-prediction/bin/dao/ArticleDAO$$anonfun$read$1$$anonfun$apply$6.class
 create mode 100755 providence-prediction/bin/dao/ArticleDAO$$anonfun$read$1$$anonfun$apply$7.class
 create mode 100755 providence-prediction/bin/dao/ArticleDAO$$anonfun$read$1.class
 create mode 100755 providence-prediction/bin/dao/ArticleDAO$$anonfun$write$1.class
 create mode 100755 providence-prediction/bin/dao/ArticleDAO$.class
 create mode 100755 providence-prediction/bin/dao/ArticleDAO.class
 create mode 100755 providence-prediction/bin/dao/FacebookPagePopularityDAO$$anonfun$read$1.class
 create mode 100755 providence-prediction/bin/dao/FacebookPagePopularityDAO$$anonfun$write$1.class
 create mode 100755 providence-prediction/bin/dao/FacebookPagePopularityDAO$.class
 create mode 100755 providence-prediction/bin/dao/FacebookPagePopularityDAO.class
 create mode 100755 providence-prediction/bin/dao/FacebookPopularitiesDAO$$anonfun$read$1$$anonfun$apply$1.class
 create mode 100755 providence-prediction/bin/dao/FacebookPopularitiesDAO$$anonfun$read$1.class
 create mode 100755 providence-prediction/bin/dao/FacebookPopularitiesDAO$$anonfun$write$1.class
 create mode 100755 providence-prediction/bin/dao/FacebookPopularitiesDAO$.class
 create mode 100755 providence-prediction/bin/dao/FacebookPopularitiesDAO.class
 create mode 100755 providence-prediction/bin/dao/FacebookPopularityDAO$$anonfun$read$1.class
 create mode 100755 providence-prediction/bin/dao/FacebookPopularityDAO$$anonfun$write$1.class
 create mode 100755 providence-prediction/bin/dao/FacebookPopularityDAO$.class
 create mode 100755 providence-prediction/bin/dao/FacebookPopularityDAO.class
 create mode 100755 providence-prediction/bin/dao/FeatureDAO$$anonfun$read$1.class
 create mode 100755 providence-prediction/bin/dao/FeatureDAO$$anonfun$write$1.class
 create mode 100755 providence-prediction/bin/dao/FeatureDAO$$anonfun$write$2.class
 create mode 100755 providence-prediction/bin/dao/FeatureDAO$.class
 create mode 100755 providence-prediction/bin/dao/FeatureDAO.class
 create mode 100755 providence-prediction/bin/dao/ReadDAO.class
 create mode 100755 providence-prediction/bin/dao/TwitterPagePopularityDAO$$anonfun$read$1.class
 create mode 100755 providence-prediction/bin/dao/TwitterPagePopularityDAO$$anonfun$write$1.class
 create mode 100755 providence-prediction/bin/dao/TwitterPagePopularityDAO$.class
 create mode 100755 providence-prediction/bin/dao/TwitterPagePopularityDAO.class
 create mode 100755 providence-prediction/bin/dao/TwitterPopularitiesDAO$$anonfun$read$1$$anonfun$apply$1.class
 create mode 100755 providence-prediction/bin/dao/TwitterPopularitiesDAO$$anonfun$read$1.class
 create mode 100755 providence-prediction/bin/dao/TwitterPopularitiesDAO$$anonfun$write$1.class
 create mode 100755 providence-prediction/bin/dao/TwitterPopularitiesDAO$.class
 create mode 100755 providence-prediction/bin/dao/TwitterPopularitiesDAO.class
 create mode 100755 providence-prediction/bin/dao/TwitterPopularityDAO$$anonfun$read$1.class
 create mode 100755 providence-prediction/bin/dao/TwitterPopularityDAO$$anonfun$write$1.class
 create mode 100755 providence-prediction/bin/dao/TwitterPopularityDAO$.class
 create mode 100755 providence-prediction/bin/dao/TwitterPopularityDAO.class
 create mode 100755 providence-prediction/bin/dao/ViewPopularitiesDAO$$anonfun$read$1$$anonfun$apply$1.class
 create mode 100755 providence-prediction/bin/dao/ViewPopularitiesDAO$$anonfun$read$1$$anonfun$apply$2.class
 create mode 100755 providence-prediction/bin/dao/ViewPopularitiesDAO$$anonfun$read$1$$anonfun$apply$3.class
 create mode 100755 providence-prediction/bin/dao/ViewPopularitiesDAO$$anonfun$read$1$$anonfun$apply$4.class
 create mode 100755 providence-prediction/bin/dao/ViewPopularitiesDAO$$anonfun$read$1.class
 create mode 100755 providence-prediction/bin/dao/ViewPopularitiesDAO$$anonfun$write$1.class
 create mode 100755 providence-prediction/bin/dao/ViewPopularitiesDAO$.class
 create mode 100755 providence-prediction/bin/dao/ViewPopularitiesDAO.class
 create mode 100755 providence-prediction/bin/dao/WriteDAO.class
 create mode 100755 providence-prediction/bin/entities/Article$$anonfun$entityToString$1.class
 create mode 100755 providence-prediction/bin/entities/Article$$anonfun$entityToString$2.class
 create mode 100755 providence-prediction/bin/entities/Article$$anonfun$entityToString$3.class
 create mode 100755 providence-prediction/bin/entities/Article$$anonfun$entityToString$4.class
 create mode 100755 providence-prediction/bin/entities/Article$$anonfun$entityToString$5.class
 create mode 100755 providence-prediction/bin/entities/Article$$anonfun$entityToString$6.class
 create mode 100755 providence-prediction/bin/entities/Article.class
 create mode 100755 providence-prediction/bin/entities/ArticleFeatures.class
 create mode 100755 providence-prediction/bin/entities/ArticleView.class
 create mode 100755 providence-prediction/bin/entities/CEDLinearDoubleViralityModel.class
 create mode 100755 providence-prediction/bin/entities/CEDLinearMultipleViralityModel$$anonfun$getValue$1.class
 create mode 100755 providence-prediction/bin/entities/CEDLinearMultipleViralityModel$$anonfun$getValuePrint$1.class
 create mode 100755 providence-prediction/bin/entities/CEDLinearMultipleViralityModel.class
 create mode 100755 providence-prediction/bin/entities/CEDLinearSleepViralityModel.class
 create mode 100755 providence-prediction/bin/entities/CEDLinearViralityModel.class
 create mode 100755 providence-prediction/bin/entities/CEDViralityModel.class
 create mode 100755 providence-prediction/bin/entities/FacebookPagePopularity$$anonfun$toText$1.class
 create mode 100755 providence-prediction/bin/entities/FacebookPagePopularity$$anonfun$toText$2.class
 create mode 100755 providence-prediction/bin/entities/FacebookPagePopularity.class
 create mode 100755 providence-prediction/bin/entities/FacebookPopularities$$anonfun$toText$1.class
 create mode 100755 providence-prediction/bin/entities/FacebookPopularities.class
 create mode 100755 providence-prediction/bin/entities/FacebookPopularity.class
 create mode 100755 providence-prediction/bin/entities/Feature.class
 create mode 100755 providence-prediction/bin/entities/HTLinearMultipleViralityModel$$anonfun$getValue$1.class
 create mode 100755 providence-prediction/bin/entities/HTLinearMultipleViralityModel.class
 create mode 100755 providence-prediction/bin/entities/HTViralityModel.class
 create mode 100755 providence-prediction/bin/entities/Log.class
 create mode 100755 providence-prediction/bin/entities/NamedEntity.class
 create mode 100755 providence-prediction/bin/entities/QueryType$.class
 create mode 100755 providence-prediction/bin/entities/QueryType.class
 create mode 100755 providence-prediction/bin/entities/SigmoidViralityModel.class
 create mode 100755 providence-prediction/bin/entities/TwitterPagePopularity.class
 create mode 100755 providence-prediction/bin/entities/TwitterPopularities$$anonfun$toText$1.class
 create mode 100755 providence-prediction/bin/entities/TwitterPopularities.class
 create mode 100755 providence-prediction/bin/entities/TwitterPopularity$$anonfun$toText$1.class
 create mode 100755 providence-prediction/bin/entities/TwitterPopularity.class
 create mode 100755 providence-prediction/bin/entities/ViewPopularities$$anonfun$toText$1.class
 create mode 100755 providence-prediction/bin/entities/ViewPopularities$$anonfun$toText$2.class
 create mode 100755 providence-prediction/bin/entities/ViewPopularities$$anonfun$toText$3.class
 create mode 100755 providence-prediction/bin/entities/ViewPopularities.class
 create mode 100755 providence-prediction/bin/entities/ViralityModel$$anonfun$calculateEstimatedValues$1.class
 create mode 100755 providence-prediction/bin/entities/ViralityModel$$anonfun$calculateMeanSquaredError$1.class
 create mode 100755 providence-prediction/bin/entities/ViralityModel$$anonfun$calculateMeanSquaredError$2.class
 create mode 100755 providence-prediction/bin/entities/ViralityModel.class
 create mode 100755 providence-prediction/bin/featuresextractors/ArticleFeaturesExtractor.class
 create mode 100755 providence-prediction/bin/featuresextractors/DeredactieArticleFeaturesExtractor.class
 create mode 100755 providence-prediction/bin/featuresextractors/DutchEntityExtractor.class
 create mode 100755 providence-prediction/bin/featuresextractors/EntityExtractor.class
 create mode 100755 providence-prediction/bin/featuresextractors/FeaturesExtractor.class
 create mode 100755 providence-prediction/bin/featuresextractors/HtmlArticleFeaturesExtractor.class
 create mode 100755 providence-prediction/bin/featuresextractors/NewsmonkeyArticleFeaturesExtractor.class
 create mode 100755 providence-prediction/bin/http/HTMLreceiver.class
 create mode 100755 providence-prediction/bin/http/ScalaHtmlReceiver.class
 create mode 100755 providence-prediction/bin/jsonparsers/ArticleViewParser.class
 create mode 100755 providence-prediction/bin/jsonparsers/DeredactieUrlParser.class
 create mode 100755 providence-prediction/bin/jsonparsers/NewsmonkeyUrlParser.class
 create mode 100755 providence-prediction/bin/jsonparsers/UrlParser.class
 create mode 100755 providence-prediction/bin/runjava/RunJava.class
 create mode 100755 providence-prediction/bin/socialmedia/Facebook$UserList.class
 create mode 100755 providence-prediction/bin/socialmedia/Facebook.class
 create mode 100755 providence-prediction/bin/socialmedia/FacebookWebRequestor.class
 create mode 100755 providence-prediction/bin/socialmedia/Twitter$TwitterUser.class
 create mode 100755 providence-prediction/bin/socialmedia/Twitter.class
 create mode 100755 providence-prediction/lib/commons-codec-1.9.jar
 create mode 100755 providence-prediction/lib/commons-collections-3.2.1.jar
 create mode 100755 providence-prediction/lib/commons-io-2.4.jar
 create mode 100755 providence-prediction/lib/commons-lang3-3.3.2.jar
 create mode 100755 providence-prediction/lib/commons-lang3-3.4.jar
 create mode 100755 providence-prediction/lib/commons-logging-1.1.1.jar
 create mode 100755 providence-prediction/lib/commons-logging-1.2.jar
 create mode 100755 providence-prediction/lib/cssparser-0.9.15.jar
 create mode 100755 providence-prediction/lib/htmlunit-2.16.jar
 create mode 100755 providence-prediction/lib/htmlunit-core-js-2.16.jar
 create mode 100755 providence-prediction/lib/httpclient-4.2.5.jar
 create mode 100755 providence-prediction/lib/httpclient-4.4.1.jar
 create mode 100755 providence-prediction/lib/httpclient-cache-4.2.5.jar
 create mode 100755 providence-prediction/lib/httpcore-4.2.4.jar
 create mode 100755 providence-prediction/lib/httpcore-4.4.1.jar
 create mode 100755 providence-prediction/lib/httpmime-4.2.5.jar
 create mode 100755 providence-prediction/lib/httpmime-4.4.1.jar
 create mode 100755 providence-prediction/lib/jetty-io-9.2.10.v20150310.jar
 create mode 100755 providence-prediction/lib/jetty-util-9.2.10.v20150310.jar
 create mode 100755 providence-prediction/lib/joda-convert-1.3.1.jar
 create mode 100755 providence-prediction/lib/joda-time-2.6.jar
 create mode 100755 providence-prediction/lib/json-simple-1.1.1.jar
 create mode 100755 providence-prediction/lib/mediahaven-analytics-api.jar
 create mode 100755 providence-prediction/lib/nekohtml-1.9.22.jar
 create mode 100755 providence-prediction/lib/org.scala-lang.scala-library_2.11.7.v20150622-112736-1fbce4612c.jar
 create mode 100755 providence-prediction/lib/restfb-1.7.0.jar
 create mode 100755 providence-prediction/lib/sac-1.3.jar
 create mode 100755 providence-prediction/lib/serializer-2.7.1.jar
 create mode 100755 providence-prediction/lib/twitter4j-core-4.0.3.jar
 create mode 100755 providence-prediction/lib/websocket-api-9.2.10.v20150310.jar
 create mode 100755 providence-prediction/lib/websocket-client-9.2.10.v20150310.jar
 create mode 100755 providence-prediction/lib/websocket-common-9.2.10.v20150310.jar
 create mode 100755 providence-prediction/lib/weka-3-6-12.jar
 create mode 100755 providence-prediction/lib/weka-3-7-12.jar
 create mode 100755 providence-prediction/lib/xalan-2.7.1.jar
 create mode 100755 providence-prediction/lib/xercesImpl-2.11.0.jar
 create mode 100755 providence-prediction/lib/xml-apis-1.4.01.jar
 create mode 100755 providence-prediction/python/_DS_Store
 create mode 100755 providence-prediction/python/rf/_DS_Store
 create mode 100755 providence-prediction/python/rf/deredactie-views/_DS_Store
 create mode 100755 providence-prediction/python/rf/deredactie-views/models.py
 create mode 100755 providence-prediction/src/_DS_Store
 create mode 100755 providence-prediction/src/classification/_DS_Store
 create mode 100755 providence-prediction/src/classification/model/ModelThomas.scala
 create mode 100755 providence-prediction/src/classification/python/Python.scala
 create mode 100755 providence-prediction/src/classification/svm/ProcessData.scala
 create mode 100755 providence-prediction/src/classification/svm/ProcessDataAPI.scala
 create mode 100755 providence-prediction/src/classification/svm/ProcessDataBasic.scala
 create mode 100755 providence-prediction/src/classification/svm/ProcessDataNewsmonkey.scala
 create mode 100755 providence-prediction/src/classification/svm/ProcessDataRF.scala
 create mode 100755 providence-prediction/src/classification/svm/SVMlinear.scala
 create mode 100755 providence-prediction/src/classification/svm/liblinear/ArraySorter.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/DoubleArrayPointer.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/FeatureNode.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/Function.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/IntArrayPointer.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/InvalidInputDataException.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/L2R_L2_SvcFunction.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/L2R_LrFunction.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/Linear.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/Model.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/Parameter.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/Predict.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/PredictOnline.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/Problem.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/README.md
 create mode 100755 providence-prediction/src/classification/svm/liblinear/Record.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/SolverMCSVM_CS.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/SolverType.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/Train.java
 create mode 100755 providence-prediction/src/classification/svm/liblinear/Tron.java
 create mode 100755 providence-prediction/src/classification/weka/Weka.scala
 create mode 100755 providence-prediction/src/classification/weka/WekaClassifier.scala
 create mode 100755 providence-prediction/src/core/Config.scala
 create mode 100755 providence-prediction/src/core/Main.scala
 create mode 100755 providence-prediction/src/dao/ArticleDAO.scala
 create mode 100755 providence-prediction/src/dao/FacebookPagePopularityDAO.scala
 create mode 100755 providence-prediction/src/dao/FacebookPopularitiesDAO.scala
 create mode 100755 providence-prediction/src/dao/FacebookPopularityDAO.scala
 create mode 100755 providence-prediction/src/dao/FeatureDAO.scala
 create mode 100755 providence-prediction/src/dao/ReadDAO.scala
 create mode 100755 providence-prediction/src/dao/TwitterPagePopularityDAO.scala
 create mode 100755 providence-prediction/src/dao/TwitterPopularitiesDAO.scala
 create mode 100755 providence-prediction/src/dao/TwitterPopularityDAO.scala
 create mode 100755 providence-prediction/src/dao/ViewPopularitiesDAO.scala
 create mode 100755 providence-prediction/src/dao/WriteDAO.scala
 create mode 100755 providence-prediction/src/entities/Article.scala
 create mode 100755 providence-prediction/src/entities/ArticleFeatures.scala
 create mode 100755 providence-prediction/src/entities/ArticleView.scala
 create mode 100755 providence-prediction/src/entities/FacebookPagePopularity.scala
 create mode 100755 providence-prediction/src/entities/FacebookPopularities.scala
 create mode 100755 providence-prediction/src/entities/FacebookPopularity.scala
 create mode 100755 providence-prediction/src/entities/Feature.scala
 create mode 100755 providence-prediction/src/entities/Log.scala
 create mode 100755 providence-prediction/src/entities/NamedEntity.scala
 create mode 100755 providence-prediction/src/entities/QueryType.scala
 create mode 100755 providence-prediction/src/entities/TwitterPagePopularity.scala
 create mode 100755 providence-prediction/src/entities/TwitterPopularities.scala
 create mode 100755 providence-prediction/src/entities/TwitterPopularity.scala
 create mode 100755 providence-prediction/src/entities/ViewPopularities.scala
 create mode 100755 providence-prediction/src/entities/ViralityModel.scala
 create mode 100755 providence-prediction/src/featuresextractors/ArticleFeaturesExtractor.java
 create mode 100755 providence-prediction/src/featuresextractors/DeredactieArticleFeaturesExtractor.java
 create mode 100755 providence-prediction/src/featuresextractors/DutchEntityExtractor.java
 create mode 100755 providence-prediction/src/featuresextractors/EntityExtractor.java
 create mode 100755 providence-prediction/src/featuresextractors/FeaturesExtractor.java
 create mode 100755 providence-prediction/src/featuresextractors/HtmlArticleFeaturesExtractor.java
 create mode 100755 providence-prediction/src/featuresextractors/NewsmonkeyArticleFeaturesExtractor.java
 create mode 100755 providence-prediction/src/http/HTMLreceiver.java
 create mode 100755 providence-prediction/src/http/ScalaHtmlReceiver.scala
 create mode 100755 providence-prediction/src/jsonparsers/ArticleViewParser.java
 create mode 100755 providence-prediction/src/jsonparsers/DeredactieUrlParser.java
 create mode 100755 providence-prediction/src/jsonparsers/NewsmonkeyUrlParser.java
 create mode 100755 providence-prediction/src/jsonparsers/UrlParser.java
 create mode 100755 providence-prediction/src/runjava/RunJava.java
 create mode 100755 providence-prediction/src/socialmedia/Facebook.java
 create mode 100755 providence-prediction/src/socialmedia/FacebookWebRequestor.java
 create mode 100755 providence-prediction/src/socialmedia/Twitter.java
paularmandsmbp.rto.be 02:58:15 (master) ~/dev_habitat/providence$ git commit
On branch master
nothing to commit, working directory clean
paularmandsmbp.rto.be 02:58:30 (master) ~/dev_habitat/providence$ git add .
paularmandsmbp.rto.be 02:58:50 (master) ~/dev_habitat/providence$ ll
total 24
 0 drwxr-xr-x@ 10 paularmand  staff   340B Nov 24 14:57 .
 0 drwxr-xr-x@ 12 paularmand  staff   408B Nov 24 14:57 ..
16 -rw-r--r--@  1 paularmand  staff   6.0K Nov 24 14:57 .DS_Store
 0 drwxr-xr-x@ 13 paularmand  staff   442B Nov 24 14:58 .git
 0 drwxr-xr-x@  8 paularmand  staff   272B Nov 24 14:54 .idea
 0 drwxr-xr-x@  6 paularmand  staff   204B Nov 24 13:37 PROVIstorm
 8 -rwxr-xr-x@  1 paularmand  staff   525B Nov 24 03:41 README.txt
 0 drwxr-xr-x@ 19 paularmand  staff   646B Nov 24 13:17 providence-api
 0 drwxr-xr-x@ 24 paularmand  staff   816B Nov 24 13:43 providence-play
 0 drwxr-xr-x@ 25 paularmand  staff   850B Nov 24 13:38 providence-prediction
paularmandsmbp.rto.be 02:58:54 (master) ~/dev_habitat/providence$ git config user.name "Paul-Armand Verhaegen"
paularmandsmbp.rto.be 02:59:15 (master) ~/dev_habitat/providence$ git config user.email "paul-armand.verhaegen@innovatie.vrt.be"
paularmandsmbp.rto.be 02:59:24 (master) ~/dev_habitat/providence$ git commit -m "first commit"
On branch master
nothing to commit, working directory clean
paularmandsmbp.rto.be 02:59:35 (master) ~/dev_habitat/providence$ git push origin master
Counting objects: 3876, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3678/3678), done.
Writing objects: 100% (3876/3876), 89.18 MiB | 5.14 MiB/s, done.
Total 3876 (delta 1087), reused 0 (delta 0)
To git@gitlab.com:vrtoeni/providence.git
 * [new branch]      master -> master
paularmandsmbp.rto.be 03:00:12 (master) ~/dev_habitat/providence$ lua
Lua 5.2.4  Copyright (C) 1994-2015 Lua.org, PUC-Rio
> local url = "http://radioplus.be/#/radio1/herbeluister/3d5c6f56-31bf-11e4-96d0-00163edf75b7/084910c1-b0a4-11e6-bf83-00163edf48dd/"
> string.find(url, "htt")
stdin:1: bad argument #1 to 'find' (string expected, got nil)
stack traceback:
	[C]: in function 'find'
	stdin:1: in main chunk
	[C]: in ?
> usl
>> 
>> 
paularmandsmbp.rto.be 04:58:25 (master) ~/dev_habitat/providence$ lua
Lua 5.2.4  Copyright (C) 1994-2015 Lua.org, PUC-Rio
> local url = "http://radioplus.be/#/radio1/herbeluister/3d5c6f56-31bf-11e4-96d0-00163edf75b7/084910c1-b0a4-11e6-bf83-00163edf48dd/"
> url = "http://radioplus.be/#/radio1/herbeluister/3d5c6f56-31bf-11e4-96d0-00163edf75b7/084910c1-b0a4-11e6-bf83-00163edf48dd/"
> string.find(url, "htt")
> = string.find(url, "htt")
1	3
> return  string.find(url, "ht-")
1	1
> return  string.find(url, "http%.")
nil
> return  string.find(url, "http.")
1	5
> return  string.find(url, "/.")
6	7
> return  string.find(url, "/[%d%a]")
7	8
> return  string.find(url, "/[%da-f]")
42	43
> return  string.find(url, "/[%da-f]{2}")
nil
> return  string.find(url, "/[%da-f]*%-[%da-f]*%-[%da-f]*%-[%da-f]*%-[%da-f]/")
nil
> return  string.find(url, "/[%da-f]*%-")
42	51
> return  string.find(url, "/[%da-f]*%-[%da-f]")
42	52
> return  string.find(url, "/[%da-f]*%-[%da-f]*")
42	55
> return  string.find(url, "/[%da-f]*%-[%da-f]*%-")
42	56
> return  string.find(url, "/[%da-f]*%-[%da-f]*%-[%da-f]*%-[%da-f]*")
42	65
> return  string.find(url, "/[%da-f]*%-[%da-f]*%-[%da-f]*%-[%da-f]*%-")
42	66
> return  string.find(url, "/[%da-f]*%-[%da-f]*%-[%da-f]*%-[%da-f]*%-[%da-f]")
42	67
> return  string.find(url, "/[%da-f]*%-[%da-f]*%-[%da-f]*%-[%da-f]*%-[%da-f]*")
42	78
> return  string.find(url, "/[%da-f]*%-[%da-f]*%-[%da-f]*%-[%da-f]*%-[%da-f]*/")
42	79
> return  string.find(url, "/[%da-f]*%-[%da-f]*%-[%da-f]*%-[%da-f]*%-[%da-f]*/")
42	79
> collection_index_start, collection_index_end = string.find(url, "/[%d]*%.")
> print collection_index_start
stdin:1: syntax error near 'collection_index_start'
> = collection_index_start
nil
> collection_index_end
>> 
>> 
>> 
>>   
>> + 1
stdin:6: syntax error near '+'
> = collection_index_start
nil
> return  collection_index_end
nil
> = string.sub(url, nil, nil)
stdin:1: bad argument #2 to 'sub' (number expected, got nil)
stack traceback:
	[C]: in function 'sub'
	stdin:1: in main chunk
	[C]: in ?
> 
paularmandsmbp.rto.be 09:18:00 (master) ~/dev_habitat/providence$ ifconfig
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=3<RXCSUM,TXCSUM>
	inet6 ::1 prefixlen 128 
	inet 127.0.0.1 netmask 0xff000000 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=1<PERFORMNUD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
en0: flags=8823<UP,BROADCAST,SMART,SIMPLEX,MULTICAST> mtu 1500
	ether f4:5c:89:8b:61:a7 
	nd6 options=1<PERFORMNUD>
	media: autoselect (<unknown type>)
	status: inactive
en1: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:00 
	media: autoselect <full-duplex>
	status: inactive
en2: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:01 
	media: autoselect <full-duplex>
	status: inactive
p2p0: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 2304
	ether 06:5c:89:8b:61:a7 
	media: autoselect
	status: inactive
awdl0: flags=8902<BROADCAST,PROMISC,SIMPLEX,MULTICAST> mtu 1484
	ether b2:1e:28:47:97:ec 
	nd6 options=1<PERFORMNUD>
	media: autoselect
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether f6:5c:89:b8:b1:00 
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 6 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 7 priority 0 path cost 0
	nd6 options=1<PERFORMNUD>
	media: <unknown type>
	status: inactive
utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1500
	inet 192.168.102.50 --> 192.168.102.49 netmask 0xffffffff 
en4: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=10b<RXCSUM,TXCSUM,VLAN_HWTAGGING,AV>
	ether 38:c9:86:24:35:0b 
	inet6 fe80::3ac9:86ff:fe24:350b%en4 prefixlen 64 scopeid 0x5 
	nd6 options=1<PERFORMNUD>
	media: autoselect (100baseTX <full-duplex,flow-control>)
	status: active
paularmandsmbp.rto.be 09:18:04 (master) ~/dev_habitat/providence$ ifconfig
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=3<RXCSUM,TXCSUM>
	inet6 ::1 prefixlen 128 
	inet 127.0.0.1 netmask 0xff000000 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=1<PERFORMNUD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
en0: flags=8823<UP,BROADCAST,SMART,SIMPLEX,MULTICAST> mtu 1500
	ether f4:5c:89:8b:61:a7 
	nd6 options=1<PERFORMNUD>
	media: autoselect (<unknown type>)
	status: inactive
en1: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:00 
	media: autoselect <full-duplex>
	status: inactive
en2: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:01 
	media: autoselect <full-duplex>
	status: inactive
p2p0: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 2304
	ether 06:5c:89:8b:61:a7 
	media: autoselect
	status: inactive
awdl0: flags=8902<BROADCAST,PROMISC,SIMPLEX,MULTICAST> mtu 1484
	ether b2:1e:28:47:97:ec 
	nd6 options=1<PERFORMNUD>
	media: autoselect
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether f6:5c:89:b8:b1:00 
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 6 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 7 priority 0 path cost 0
	nd6 options=1<PERFORMNUD>
	media: <unknown type>
	status: inactive
utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1500
	inet 192.168.102.50 --> 192.168.102.49 netmask 0xffffffff 
en4: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=10b<RXCSUM,TXCSUM,VLAN_HWTAGGING,AV>
	ether 38:c9:86:24:35:0b 
	inet6 fe80::3ac9:86ff:fe24:350b%en4 prefixlen 64 scopeid 0x5 
	nd6 options=1<PERFORMNUD>
	media: autoselect (100baseTX <full-duplex,flow-control>)
	status: active
paularmandsmbp.rto.be 09:19:31 (master) ~/dev_habitat/providence$ ifconfig
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=3<RXCSUM,TXCSUM>
	inet6 ::1 prefixlen 128 
	inet 127.0.0.1 netmask 0xff000000 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=1<PERFORMNUD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
en0: flags=8823<UP,BROADCAST,SMART,SIMPLEX,MULTICAST> mtu 1500
	ether f4:5c:89:8b:61:a7 
	nd6 options=1<PERFORMNUD>
	media: autoselect (<unknown type>)
	status: inactive
en1: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:00 
	media: autoselect <full-duplex>
	status: inactive
en2: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:01 
	media: autoselect <full-duplex>
	status: inactive
p2p0: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 2304
	ether 06:5c:89:8b:61:a7 
	media: autoselect
	status: inactive
awdl0: flags=8902<BROADCAST,PROMISC,SIMPLEX,MULTICAST> mtu 1484
	ether b2:1e:28:47:97:ec 
	nd6 options=1<PERFORMNUD>
	media: autoselect
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether f6:5c:89:b8:b1:00 
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 6 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 7 priority 0 path cost 0
	nd6 options=1<PERFORMNUD>
	media: <unknown type>
	status: inactive
utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1500
	inet 192.168.102.50 --> 192.168.102.49 netmask 0xffffffff 
en4: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=10b<RXCSUM,TXCSUM,VLAN_HWTAGGING,AV>
	ether 38:c9:86:24:35:0b 
	inet6 fe80::3ac9:86ff:fe24:350b%en4 prefixlen 64 scopeid 0x5 
	nd6 options=1<PERFORMNUD>
	media: autoselect (100baseTX <full-duplex,flow-control>)
	status: active
paularmandsmbp.rto.be 09:19:34 (master) ~/dev_habitat/providence$ ifconfig
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=3<RXCSUM,TXCSUM>
	inet6 ::1 prefixlen 128 
	inet 127.0.0.1 netmask 0xff000000 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=1<PERFORMNUD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
en0: flags=8823<UP,BROADCAST,SMART,SIMPLEX,MULTICAST> mtu 1500
	ether f4:5c:89:8b:61:a7 
	nd6 options=1<PERFORMNUD>
	media: autoselect (<unknown type>)
	status: inactive
en1: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:00 
	media: autoselect <full-duplex>
	status: inactive
en2: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:01 
	media: autoselect <full-duplex>
	status: inactive
p2p0: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 2304
	ether 06:5c:89:8b:61:a7 
	media: autoselect
	status: inactive
awdl0: flags=8902<BROADCAST,PROMISC,SIMPLEX,MULTICAST> mtu 1484
	ether b2:1e:28:47:97:ec 
	nd6 options=1<PERFORMNUD>
	media: autoselect
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether f6:5c:89:b8:b1:00 
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 6 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 7 priority 0 path cost 0
	nd6 options=1<PERFORMNUD>
	media: <unknown type>
	status: inactive
utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1500
	inet 192.168.102.50 --> 192.168.102.49 netmask 0xffffffff 
en4: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=10b<RXCSUM,TXCSUM,VLAN_HWTAGGING,AV>
	ether 38:c9:86:24:35:0b 
	inet6 fe80::3ac9:86ff:fe24:350b%en4 prefixlen 64 scopeid 0x5 
	inet 169.254.142.151 netmask 0xffff0000 broadcast 169.254.255.255
	nd6 options=1<PERFORMNUD>
	media: autoselect (100baseTX <full-duplex,flow-control>)
	status: active
paularmandsmbp.rto.be 09:19:46 (master) ~/dev_habitat/providence$ ifconfig
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=3<RXCSUM,TXCSUM>
	inet6 ::1 prefixlen 128 
	inet 127.0.0.1 netmask 0xff000000 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=1<PERFORMNUD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
en0: flags=8823<UP,BROADCAST,SMART,SIMPLEX,MULTICAST> mtu 1500
	ether f4:5c:89:8b:61:a7 
	nd6 options=1<PERFORMNUD>
	media: autoselect (<unknown type>)
	status: inactive
en1: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:00 
	media: autoselect <full-duplex>
	status: inactive
en2: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:01 
	media: autoselect <full-duplex>
	status: inactive
p2p0: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 2304
	ether 06:5c:89:8b:61:a7 
	media: autoselect
	status: inactive
awdl0: flags=8902<BROADCAST,PROMISC,SIMPLEX,MULTICAST> mtu 1484
	ether b2:1e:28:47:97:ec 
	nd6 options=1<PERFORMNUD>
	media: autoselect
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether f6:5c:89:b8:b1:00 
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 6 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 7 priority 0 path cost 0
	nd6 options=1<PERFORMNUD>
	media: <unknown type>
	status: inactive
en4: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=10b<RXCSUM,TXCSUM,VLAN_HWTAGGING,AV>
	ether 38:c9:86:24:35:0b 
	inet6 fe80::3ac9:86ff:fe24:350b%en4 prefixlen 64 scopeid 0x5 
	inet 169.254.142.151 netmask 0xffff0000 broadcast 169.254.255.255
	nd6 options=1<PERFORMNUD>
	media: autoselect (100baseTX <full-duplex,flow-control>)
	status: active
paularmandsmbp.rto.be 09:20:22 (master) ~/dev_habitat/providence$ netstat 
Active Internet connections
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)    
tcp4       0      0  192.168.1.100.52330    40.127.129.109.https   ESTABLISHED
tcp4       0      0  192.168.1.100.52088    40.127.129.109.https   ESTABLISHED
tcp4       0    412  192.168.1.100.52086    52.90.4.230.https      FIN_WAIT_1 
tcp4       0    412  192.168.1.100.52084    107.21.74.105.https    FIN_WAIT_1 
tcp4       0    412  192.168.1.100.52082    54.242.95.213.https    FIN_WAIT_1 
tcp4       0    412  192.168.1.100.52081    54.225.22.47.https     FIN_WAIT_1 
tcp4       0    412  192.168.1.100.52080    52.90.64.91.https      FIN_WAIT_1 
tcp4       0    472  192.168.1.100.52079    52.90.4.230.https      FIN_WAIT_1 
tcp4       0    412  192.168.1.100.52078    54.172.82.211.https    FIN_WAIT_1 
tcp4       0      0  192.168.1.100.52073    91.190.219.39.12350    ESTABLISHED
tcp4       0      0  192.168.1.100.52071    191.239.211.246.https  ESTABLISHED
tcp4       0      0  192.168.1.100.51772    52.55.159.190.https    CLOSE_WAIT 
tcp4       0      0  10.1.28.245.51294      191.233.95.169.https   ESTABLISHED
tcp4      31      0  10.1.28.245.51165      45.58.74.129.https     CLOSE_WAIT 
tcp4       0      0  10.114.100.163.63374   91.190.218.51.http     ESTABLISHED
tcp4       0      0  10.114.100.163.63097   91.190.219.40.http     ESTABLISHED
tcp4       0      0  10.114.100.163.62375   91.190.218.63.http     ESTABLISHED
tcp4       0      0  192.168.1.101.64808    217.70.184.11.imap     ESTABLISHED
udp4       0      0  *.bootpc               *.*                               
udp4       0      0  *.29447                *.*                               
udp4       0      0  192.168.102.50.ntp     *.*                               
udp4       0      0  192.168.1.100.ntp      *.*                               
^C
paularmandsmbp.rto.be 09:21:43 (master) ~/dev_habitat/providence$ nmap 
Nmap 7.12 ( https://nmap.org )
Usage: nmap [Scan Type(s)] [Options] {target specification}
TARGET SPECIFICATION:
  Can pass hostnames, IP addresses, networks, etc.
  Ex: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
  -iL <inputfilename>: Input from list of hosts/networks
  -iR <num hosts>: Choose random targets
  --exclude <host1[,host2][,host3],...>: Exclude hosts/networks
  --excludefile <exclude_file>: Exclude list from file
HOST DISCOVERY:
  -sL: List Scan - simply list targets to scan
  -sn: Ping Scan - disable port scan
  -Pn: Treat all hosts as online -- skip host discovery
  -PS/PA/PU/PY[portlist]: TCP SYN/ACK, UDP or SCTP discovery to given ports
  -PE/PP/PM: ICMP echo, timestamp, and netmask request discovery probes
  -PO[protocol list]: IP Protocol Ping
  -n/-R: Never do DNS resolution/Always resolve [default: sometimes]
  --dns-servers <serv1[,serv2],...>: Specify custom DNS servers
  --system-dns: Use OS's DNS resolver
  --traceroute: Trace hop path to each host
SCAN TECHNIQUES:
  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
  -sU: UDP Scan
  -sN/sF/sX: TCP Null, FIN, and Xmas scans
  --scanflags <flags>: Customize TCP scan flags
  -sI <zombie host[:probeport]>: Idle scan
  -sY/sZ: SCTP INIT/COOKIE-ECHO scans
  -sO: IP protocol scan
  -b <FTP relay host>: FTP bounce scan
PORT SPECIFICATION AND SCAN ORDER:
  -p <port ranges>: Only scan specified ports
    Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
  --exclude-ports <port ranges>: Exclude the specified ports from scanning
  -F: Fast mode - Scan fewer ports than the default scan
  -r: Scan ports consecutively - don't randomize
  --top-ports <number>: Scan <number> most common ports
  --port-ratio <ratio>: Scan ports more common than <ratio>
SERVICE/VERSION DETECTION:
  -sV: Probe open ports to determine service/version info
  --version-intensity <level>: Set from 0 (light) to 9 (try all probes)
  --version-light: Limit to most likely probes (intensity 2)
  --version-all: Try every single probe (intensity 9)
  --version-trace: Show detailed version scan activity (for debugging)
SCRIPT SCAN:
  -sC: equivalent to --script=default
  --script=<Lua scripts>: <Lua scripts> is a comma separated list of
           directories, script-files or script-categories
  --script-args=<n1=v1,[n2=v2,...]>: provide arguments to scripts
  --script-args-file=filename: provide NSE script args in a file
  --script-trace: Show all data sent and received
  --script-updatedb: Update the script database.
  --script-help=<Lua scripts>: Show help about scripts.
           <Lua scripts> is a comma-separated list of script-files or
           script-categories.
OS DETECTION:
  -O: Enable OS detection
  --osscan-limit: Limit OS detection to promising targets
  --osscan-guess: Guess OS more aggressively
TIMING AND PERFORMANCE:
  Options which take <time> are in seconds, or append 'ms' (milliseconds),
  's' (seconds), 'm' (minutes), or 'h' (hours) to the value (e.g. 30m).
  -T<0-5>: Set timing template (higher is faster)
  --min-hostgroup/max-hostgroup <size>: Parallel host scan group sizes
  --min-parallelism/max-parallelism <numprobes>: Probe parallelization
  --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>: Specifies
      probe round trip time.
  --max-retries <tries>: Caps number of port scan probe retransmissions.
  --host-timeout <time>: Give up on target after this long
  --scan-delay/--max-scan-delay <time>: Adjust delay between probes
  --min-rate <number>: Send packets no slower than <number> per second
  --max-rate <number>: Send packets no faster than <number> per second
FIREWALL/IDS EVASION AND SPOOFING:
  -f; --mtu <val>: fragment packets (optionally w/given MTU)
  -D <decoy1,decoy2[,ME],...>: Cloak a scan with decoys
  -S <IP_Address>: Spoof source address
  -e <iface>: Use specified interface
  -g/--source-port <portnum>: Use given port number
  --proxies <url1,[url2],...>: Relay connections through HTTP/SOCKS4 proxies
  --data <hex string>: Append a custom payload to sent packets
  --data-string <string>: Append a custom ASCII string to sent packets
  --data-length <num>: Append random data to sent packets
  --ip-options <options>: Send packets with specified ip options
  --ttl <val>: Set IP time-to-live field
  --spoof-mac <mac address/prefix/vendor name>: Spoof your MAC address
  --badsum: Send packets with a bogus TCP/UDP/SCTP checksum
OUTPUT:
  -oN/-oX/-oS/-oG <file>: Output scan in normal, XML, s|<rIpt kIddi3,
     and Grepable format, respectively, to the given filename.
  -oA <basename>: Output in the three major formats at once
  -v: Increase verbosity level (use -vv or more for greater effect)
  -d: Increase debugging level (use -dd or more for greater effect)
  --reason: Display the reason a port is in a particular state
  --open: Only show open (or possibly open) ports
  --packet-trace: Show all packets sent and received
  --iflist: Print host interfaces and routes (for debugging)
  --append-output: Append to rather than clobber specified output files
  --resume <filename>: Resume an aborted scan
  --stylesheet <path/URL>: XSL stylesheet to transform XML output to HTML
  --webxml: Reference stylesheet from Nmap.Org for more portable XML
  --no-stylesheet: Prevent associating of XSL stylesheet w/XML output
MISC:
  -6: Enable IPv6 scanning
  -A: Enable OS detection, version detection, script scanning, and traceroute
  --datadir <dirname>: Specify custom Nmap data file location
  --send-eth/--send-ip: Send using raw ethernet frames or IP packets
  --privileged: Assume that the user is fully privileged
  --unprivileged: Assume the user lacks raw socket privileges
  -V: Print version number
  -h: Print this help summary page.
EXAMPLES:
  nmap -v -A scanme.nmap.org
  nmap -v -sn 192.168.0.0/16 10.0.0.0/8
  nmap -v -iR 10000 -Pn -p 80
SEE THE MAN PAGE (https://nmap.org/book/man.html) FOR MORE OPTIONS AND EXAMPLES
paularmandsmbp.rto.be 09:27:18 (master) ~/dev_habitat/providence$ ifconfig
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=3<RXCSUM,TXCSUM>
	inet6 ::1 prefixlen 128 
	inet 127.0.0.1 netmask 0xff000000 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=1<PERFORMNUD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether f4:5c:89:8b:61:a7 
	inet6 fe80::f65c:89ff:fe8b:61a7%en0 prefixlen 64 scopeid 0x4 
	inet 192.168.1.100 netmask 0xffffff00 broadcast 192.168.1.255
	nd6 options=1<PERFORMNUD>
	media: autoselect
	status: active
en1: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:00 
	media: autoselect <full-duplex>
	status: inactive
en2: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:01 
	media: autoselect <full-duplex>
	status: inactive
p2p0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 2304
	ether 06:5c:89:8b:61:a7 
	media: autoselect
	status: inactive
awdl0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1484
	ether b2:1e:28:47:97:ec 
	inet6 fe80::b01e:28ff:fe47:97ec%awdl0 prefixlen 64 scopeid 0x9 
	nd6 options=1<PERFORMNUD>
	media: autoselect
	status: active
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether f6:5c:89:b8:b1:00 
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 6 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 7 priority 0 path cost 0
	nd6 options=1<PERFORMNUD>
	media: <unknown type>
	status: inactive
en4: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=10b<RXCSUM,TXCSUM,VLAN_HWTAGGING,AV>
	ether 38:c9:86:24:35:0b 
	inet6 fe80::3ac9:86ff:fe24:350b%en4 prefixlen 64 scopeid 0x5 
	inet 169.254.142.151 netmask 0xffff0000 broadcast 169.254.255.255
	nd6 options=1<PERFORMNUD>
	media: autoselect (100baseTX <full-duplex,flow-control>)
	status: active
paularmandsmbp.rto.be 09:28:26 (master) ~/dev_habitat/providence$ nmap 169.254/16

Starting Nmap 7.12 ( https://nmap.org ) at 2016-11-24 21:28 CET

paularmandsmbp.rto.be 09:29:39 (master) ~/dev_habitat/providence$ nmap -p 22 --open -sV 169.254/16

Starting Nmap 7.12 ( https://nmap.org ) at 2016-11-24 21:29 CET
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
Strange SO_ERROR from connection to 169.0.10.15 (50 - 'Network is down') -- bailing scan
QUITTING!
paularmandsmbp.rto.be 09:31:55 (master) ~/dev_habitat/providence$ nmap 169.254/16

Starting Nmap 7.12 ( https://nmap.org ) at 2016-11-24 21:31 CET
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers

paularmandsmbp.rto.be 09:32:00 (master) ~/dev_habitat/providence$ nmap -p 22 --open -sV 169.254/16

Starting Nmap 7.12 ( https://nmap.org ) at 2016-11-24 21:32 CET
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap done: 65536 IP addresses (0 hosts up) scanned in 5.39 seconds
paularmandsmbp.rto.be 09:32:13 (master) ~/dev_habitat/providence$ ifconfig
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=3<RXCSUM,TXCSUM>
	inet6 ::1 prefixlen 128 
	inet 127.0.0.1 netmask 0xff000000 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=1<PERFORMNUD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
en0: flags=8823<UP,BROADCAST,SMART,SIMPLEX,MULTICAST> mtu 1500
	ether f4:5c:89:8b:61:a7 
	nd6 options=1<PERFORMNUD>
	media: autoselect (<unknown type>)
	status: inactive
en1: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:00 
	media: autoselect <full-duplex>
	status: inactive
en2: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:01 
	media: autoselect <full-duplex>
	status: inactive
p2p0: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 2304
	ether 06:5c:89:8b:61:a7 
	media: autoselect
	status: inactive
awdl0: flags=8902<BROADCAST,PROMISC,SIMPLEX,MULTICAST> mtu 1484
	ether b2:1e:28:47:97:ec 
	nd6 options=1<PERFORMNUD>
	media: autoselect
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether f6:5c:89:b8:b1:00 
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 6 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 7 priority 0 path cost 0
	nd6 options=1<PERFORMNUD>
	media: <unknown type>
	status: inactive
en4: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=10b<RXCSUM,TXCSUM,VLAN_HWTAGGING,AV>
	ether 38:c9:86:24:35:0b 
	inet6 fe80::3ac9:86ff:fe24:350b%en4 prefixlen 64 scopeid 0x5 
	inet 169.254.142.151 netmask 0xffff0000 broadcast 169.254.255.255
	nd6 options=1<PERFORMNUD>
	media: autoselect (100baseTX <full-duplex,flow-control>)
	status: active
paularmandsmbp.rto.be 09:32:27 (master) ~/dev_habitat/providence$ nmap -p 80 --open -sV 169.254/16

Starting Nmap 7.12 ( https://nmap.org ) at 2016-11-24 21:32 CET
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap done: 65536 IP addresses (0 hosts up) scanned in 2.05 seconds
paularmandsmbp.rto.be 09:32:45 (master) ~/dev_habitat/providence$ nmap -p 8080 --open -sV 169.254/16

Starting Nmap 7.12 ( https://nmap.org ) at 2016-11-24 21:32 CET
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap done: 65536 IP addresses (0 hosts up) scanned in 2.32 seconds
paularmandsmbp.rto.be 09:32:55 (master) ~/dev_habitat/providence$ nmap -p 443 --open -sV 169.254/16

Starting Nmap 7.12 ( https://nmap.org ) at 2016-11-24 21:33 CET
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap done: 65536 IP addresses (0 hosts up) scanned in 2.19 seconds
paularmandsmbp.rto.be 09:33:08 (master) ~/dev_habitat/providence$ ifconfig
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=3<RXCSUM,TXCSUM>
	inet6 ::1 prefixlen 128 
	inet 127.0.0.1 netmask 0xff000000 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=1<PERFORMNUD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
en0: flags=8823<UP,BROADCAST,SMART,SIMPLEX,MULTICAST> mtu 1500
	ether f4:5c:89:8b:61:a7 
	nd6 options=1<PERFORMNUD>
	media: autoselect (<unknown type>)
	status: inactive
en1: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:00 
	media: autoselect <full-duplex>
	status: inactive
en2: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:01 
	media: autoselect <full-duplex>
	status: inactive
p2p0: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 2304
	ether 06:5c:89:8b:61:a7 
	media: autoselect
	status: inactive
awdl0: flags=8902<BROADCAST,PROMISC,SIMPLEX,MULTICAST> mtu 1484
	ether b2:1e:28:47:97:ec 
	nd6 options=1<PERFORMNUD>
	media: autoselect
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether f6:5c:89:b8:b1:00 
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 6 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 7 priority 0 path cost 0
	nd6 options=1<PERFORMNUD>
	media: <unknown type>
	status: inactive
en4: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=10b<RXCSUM,TXCSUM,VLAN_HWTAGGING,AV>
	ether 38:c9:86:24:35:0b 
	inet6 fe80::3ac9:86ff:fe24:350b%en4 prefixlen 64 scopeid 0x5 
	nd6 options=1<PERFORMNUD>
	media: autoselect (100baseTX <full-duplex,flow-control>)
	status: active
paularmandsmbp.rto.be 09:34:49 (master) ~/dev_habitat/providence$ ifconfig
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=3<RXCSUM,TXCSUM>
	inet6 ::1 prefixlen 128 
	inet 127.0.0.1 netmask 0xff000000 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=1<PERFORMNUD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
en0: flags=8823<UP,BROADCAST,SMART,SIMPLEX,MULTICAST> mtu 1500
	ether f4:5c:89:8b:61:a7 
	nd6 options=1<PERFORMNUD>
	media: autoselect (<unknown type>)
	status: inactive
en1: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:00 
	media: autoselect <full-duplex>
	status: inactive
en2: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:01 
	media: autoselect <full-duplex>
	status: inactive
p2p0: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 2304
	ether 06:5c:89:8b:61:a7 
	media: autoselect
	status: inactive
awdl0: flags=8902<BROADCAST,PROMISC,SIMPLEX,MULTICAST> mtu 1484
	ether b2:1e:28:47:97:ec 
	nd6 options=1<PERFORMNUD>
	media: autoselect
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether f6:5c:89:b8:b1:00 
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 6 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 7 priority 0 path cost 0
	nd6 options=1<PERFORMNUD>
	media: <unknown type>
	status: inactive
en4: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=10b<RXCSUM,TXCSUM,VLAN_HWTAGGING,AV>
	ether 38:c9:86:24:35:0b 
	inet6 fe80::3ac9:86ff:fe24:350b%en4 prefixlen 64 scopeid 0x5 
	nd6 options=1<PERFORMNUD>
	media: autoselect (100baseTX <full-duplex,flow-control>)
	status: active
paularmandsmbp.rto.be 09:34:52 (master) ~/dev_habitat/providence$ ifconfig
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=3<RXCSUM,TXCSUM>
	inet6 ::1 prefixlen 128 
	inet 127.0.0.1 netmask 0xff000000 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=1<PERFORMNUD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
en0: flags=8823<UP,BROADCAST,SMART,SIMPLEX,MULTICAST> mtu 1500
	ether f4:5c:89:8b:61:a7 
	nd6 options=1<PERFORMNUD>
	media: autoselect (<unknown type>)
	status: inactive
en1: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:00 
	media: autoselect <full-duplex>
	status: inactive
en2: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 4a:00:04:ae:e3:01 
	media: autoselect <full-duplex>
	status: inactive
p2p0: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 2304
	ether 06:5c:89:8b:61:a7 
	media: autoselect
	status: inactive
awdl0: flags=8902<BROADCAST,PROMISC,SIMPLEX,MULTICAST> mtu 1484
	ether b2:1e:28:47:97:ec 
	nd6 options=1<PERFORMNUD>
	media: autoselect
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether f6:5c:89:b8:b1:00 
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 6 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 7 priority 0 path cost 0
	nd6 options=1<PERFORMNUD>
	media: <unknown type>
	status: inactive
en4: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=10b<RXCSUM,TXCSUM,VLAN_HWTAGGING,AV>
	ether 38:c9:86:24:35:0b 
	inet6 fe80::3ac9:86ff:fe24:350b%en4 prefixlen 64 scopeid 0x5 
	inet 192.168.1.100 netmask 0xffff0000 broadcast 192.168.255.255
	nd6 options=1<PERFORMNUD>
	media: autoselect (100baseTX <full-duplex,flow-control>)
	status: active
paularmandsmbp.rto.be 09:36:16 (master) ~/dev_habitat/providence$ ping 192.168.1.138
PING 192.168.1.138 (192.168.1.138): 56 data bytes
Request timeout for icmp_seq 0
Request timeout for icmp_seq 1
^C
--- 192.168.1.138 ping statistics ---
3 packets transmitted, 0 packets received, 100.0% packet loss
paularmandsmbp.rto.be 09:36:29 (master) ~/dev_habitat/providence$ ping 192.168.1.137
PING 192.168.1.137 (192.168.1.137): 56 data bytes
Request timeout for icmp_seq 0
Request timeout for icmp_seq 1
^C
--- 192.168.1.137 ping statistics ---
3 packets transmitted, 0 packets received, 100.0% packet loss
paularmandsmbp.rto.be 09:36:33 (master) ~/dev_habitat/providence$ nmap -p 22 --open -sV 192.168/16

Starting Nmap 7.12 ( https://nmap.org ) at 2016-11-24 21:36 CET
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap done: 65536 IP addresses (0 hosts up) scanned in 2.23 seconds
paularmandsmbp.rto.be 09:36:52 (master) ~/dev_habitat/providence$ nmap -p 22 --open -sV 192.168/16

Starting Nmap 7.12 ( https://nmap.org ) at 2016-11-24 21:45 CET

paularmandsmbp.rto.be 09:45:45 (master) ~/dev_habitat/providence$ nmap -p 22 --open -sV 192.168.1/24

Starting Nmap 7.12 ( https://nmap.org ) at 2016-11-24 21:45 CET

paularmandsmbp.rto.be 09:46:56 (master) ~/dev_habitat/providence$ ssh pi@192.168.1.137
^C
paularmandsmbp.rto.be 09:48:04 (master) ~/dev_habitat/providence$ ssh pi@192.168.1.138
ssh: connect to host 192.168.1.138 port 22: Operation timed out
paularmandsmbp.rto.be 09:49:22 (master) ~/dev_habitat/providence$ ssh pi@192.168.1.106
The authenticity of host '192.168.1.106 (192.168.1.106)' can't be established.
ECDSA key fingerprint is SHA256:SaVo4WsZepfkeUAqUrx52VL5DrqhQGd05HEg3kUXCpk.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.1.106' (ECDSA) to the list of known hosts.

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Nov 23 22:17:09 2016
(cv) pi@raspberrypi:~ $ cd engine/
(cv) pi@raspberrypi:~/engine $ cd scratchpad/
(cv) pi@raspberrypi:~/engine/scratchpad $ ll
total 668
  4 drwxr-xr-x 2 pi pi   4096 Nov 23 22:05 .
  4 drwxr-xr-x 3 pi pi   4096 Nov 23 20:23 ..
448 -rw-r--r-- 1 pi pi 457797 Nov 23 22:05 foo.jpg
200 -rw-r--r-- 1 pi pi 202376 Nov 23 22:05 foo_contours.jpg
  4 -rw-r--r-- 1 pi pi    201 Nov 23 20:23 test1.py
  4 -rw-r--r-- 1 pi pi    898 Nov 23 20:23 test2.py
  4 -rw-r--r-- 1 pi pi    841 Nov 23 22:05 test3_contours.py
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test3_contours.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 
OpenCV Error: Assertion failed (scn == 3 || scn == 4) in cvtColor, file /home/pi/opencv-3.1.0/modules/imgproc/src/color.cpp, line 8000
Traceback (most recent call last):
  File "test4_video.py", line 11, in <module>
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.error: /home/pi/opencv-3.1.0/modules/imgproc/src/color.cpp:8000: error: (-215) scn == 3 || scn == 4 in function cvtColor

(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:1548): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.

(Frame:1548): Gtk-WARNING **: cannot open display: 
(cv) pi@raspberrypi:~/engine/scratchpad $ exit
logout
Connection to 192.168.1.106 closed.
paularmandsmbp.rto.be 10:07:28 (master) ~/dev_habitat/providence$ ssh -X pi@192.168.1.106

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Nov 24 20:49:36 2016 from 192.168.1.100
(cv) pi@raspberrypi:~ $ cd engine/scratchpad/
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:1636): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
^CTraceback (most recent call last):
  File "test4_video.py", line 24, in <module>
    key = cv2.waitKey(1) & 0xFF
KeyboardInterrupt
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:1683): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
^CTraceback (most recent call last):
  File "test4_video.py", line 32, in <module>
    key = cv2.waitKey(1) & 0xFF
KeyboardInterrupt
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:1704): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
^CTraceback (most recent call last):
  File "test4_video.py", line 33, in <module>
    key = cv2.waitKey(1) & 0xFF
KeyboardInterrupt
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 
Traceback (most recent call last):
  File "test4_video.py", line 23, in <module>
    ret,thresh = cv2.threshold(imgray,127,255,0)
NameError: name 'imgray' is not defined
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:1741): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
^CTraceback (most recent call last):
  File "test4_video.py", line 33, in <module>
    key = cv2.waitKey(1) & 0xFF
KeyboardInterrupt
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:1760): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
^CTraceback (most recent call last):
  File "test4_video.py", line 33, in <module>
    key = cv2.waitKey(1) & 0xFF
KeyboardInterrupt
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:1781): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.

(Frame:1781): Gtk-WARNING **: cannot open display: localhost:10.0
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:1799): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.

(Frame:1799): Gtk-WARNING **: cannot open display: localhost:10.0
(cv) pi@raspberrypi:~/engine/scratchpad $ exit
logout
Connection to 192.168.1.106 closed.
paularmandsmbp.rto.be 10:30:41 (master) ~/dev_habitat/providence$ ssh -X pi@192.168.1.106

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Nov 24 21:07:38 2016 from 192.168.1.100
(cv) pi@raspberrypi:~ $ cd engine/scratchpad/
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:1893): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
^CTraceback (most recent call last):
  File "test4_video.py", line 36, in <module>
    key = cv2.waitKey(1) & 0xFF
KeyboardInterrupt
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 
Traceback (most recent call last):
  File "test4_video.py", line 29, in <module>
    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
NameError: name 'thresh' is not defined
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:1930): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
^CTraceback (most recent call last):
  File "test4_video.py", line 35, in <module>
    key = cv2.waitKey(1) & 0xFF
KeyboardInterrupt
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:1949): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
^CTraceback (most recent call last):
  File "test4_video.py", line 35, in <module>
    key = cv2.waitKey(1) & 0xFF
KeyboardInterrupt
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 
Traceback (most recent call last):
  File "test4_video.py", line 29, in <module>
    image, contours, hierarchy = cv2.findContours(image,CV_RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
NameError: name 'CV_RETR_LIST' is not defined
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 
Traceback (most recent call last):
  File "test4_video.py", line 29, in <module>
    image, contours, hierarchy = cv2.findContours(image,cv.CV_RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
NameError: name 'cv' is not defined
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 
Traceback (most recent call last):
  File "test4_video.py", line 29, in <module>
    image, contours, hierarchy = cv2.findContours(image,cv2.CV_RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
AttributeError: 'module' object has no attribute 'CV_RETR_LIST'
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:2023): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
^CTraceback (most recent call last):
  File "test4_video.py", line 29, in <module>
    image, contours, hierarchy = cv2.findContours(image,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
KeyboardInterrupt
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:2044): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
^CTraceback (most recent call last):
  File "test4_video.py", line 35, in <module>
    key = cv2.waitKey(1) & 0xFF
KeyboardInterrupt
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:2063): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
^CTraceback (most recent call last):
  File "test4_video.py", line 35, in <module>
    key = cv2.waitKey(1) & 0xFF
KeyboardInterrupt
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:2081): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
^CTraceback (most recent call last):
  File "test4_video.py", line 35, in <module>
    key = cv2.waitKey(1) & 0xFF
KeyboardInterrupt
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:2102): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
^CTraceback (most recent call last):
  File "test4_video.py", line 35, in <module>
    key = cv2.waitKey(1) & 0xFF
KeyboardInterrupt
(cv) pi@raspberrypi:~/engine/scratchpad $ pip install imutils
Collecting imutils
  Downloading imutils-0.3.6.tar.gz
Building wheels for collected packages: imutils
  Running setup.py bdist_wheel for imutils ... done
  Stored in directory: /home/pi/.cache/pip/wheels/d2/ea/1b/9c3ae9376e71e98207c1886f1de79cb460399320a23903b562
Successfully built imutils
Installing collected packages: imutils
Successfully installed imutils-0.3.6
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test5_speedup.py
(cv) pi@raspberrypi:~/engine/scratchpad $ python test5_speedup.py 
  File "test5_speedup.py", line 29
    from __future__ import print_function
SyntaxError: from __future__ imports must occur at the beginning of the file
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test5_speedup.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test5_speedup.py 
  File "test5_speedup.py", line 28
    from __future__ import print_function
SyntaxError: from __future__ imports must occur at the beginning of the file
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test5_speedup.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test5_speedup.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test5_speedup.py 
  File "test5_speedup.py", line 28
    from __future__ import print_function
SyntaxError: from __future__ imports must occur at the beginning of the file
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test5_speedup.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test5_speedup.py 
  File "test5_speedup.py", line 29
    from __future__ import print_function
SyntaxError: from __future__ imports must occur at the beginning of the file
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test5_speedup.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test5_speedup.py 
[INFO] sampling frames from `picamera` module...
[INFO] elasped time: 3.49
[INFO] approx. FPS: 28.92
[INFO] sampling THREADED frames from `picamera` module...
[INFO] elasped time: 0.42
[INFO] approx. FPS: 240.45
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test5_speedup.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_speedup.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:2221): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.

(Frame:2221): Gtk-WARNING **: cannot open display: localhost:10.0
(cv) pi@raspberrypi:~/engine/scratchpad $ exit
logout
Connection to 192.168.1.106 closed.
paularmandsmbp.rto.be 11:28:18 (master) ~/dev_habitat/providence$ ssh -X pi@192.168.1.106

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Nov 24 21:30:43 2016 from 192.168.1.100
(cv) pi@raspberrypi:~ $ cd engine/scratchpad/
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:2311): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
^CTraceback (most recent call last):
  File "test4_video.py", line 35, in <module>
    key = cv2.waitKey(1) & 0xFF
KeyboardInterrupt
(cv) pi@raspberrypi:~/engine/scratchpad $ cd engine/scratchpad/
-bash: cd: engine/scratchpad/: No such file or directory
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:2339): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
^CTraceback (most recent call last):
  File "test4_video.py", line 35, in <module>
    key = cv2.waitKey(1) & 0xFF
KeyboardInterrupt
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 
(cv) pi@raspberrypi:~/engine/scratchpad $ python test4_video.py 

(process:2359): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
^CTraceback (most recent call last):
  File "test4_video.py", line 31, in <module>
    cv2.drawContours(image_orig,contours,-1,(255,255,255),3)    
KeyboardInterrupt
(cv) pi@raspberrypi:~/engine/scratchpad $ ll
total 676
  4 drwxr-xr-x 2 pi pi   4096 Nov 24 22:35 .
  4 drwxr-xr-x 3 pi pi   4096 Nov 23 20:23 ..
448 -rw-r--r-- 1 pi pi 457797 Nov 23 22:05 foo.jpg
200 -rw-r--r-- 1 pi pi 202376 Nov 23 22:05 foo_contours.jpg
  4 -rw-r--r-- 1 pi pi    201 Nov 23 20:23 test1.py
  4 -rw-r--r-- 1 pi pi    898 Nov 23 20:23 test2.py
  4 -rw-r--r-- 1 pi pi    841 Nov 23 22:05 test3_contours.py
  4 -rw-r--r-- 1 pi pi   1349 Nov 24 22:35 test4_video.py
  4 -rw-r--r-- 1 pi pi   2766 Nov 24 22:16 test5_speedup.py
(cv) pi@raspberrypi:~/engine/scratchpad $ vi test4_video.py 

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# configuration
THRESHOLD_MIN = 50

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image_orig = frame.array

    image = cv2.cvtColor(image_orig,cv2.COLOR_BGR2GRAY)
    ret,image = cv2.threshold(image,THRESHOLD_MIN,255,cv2.THRESH_BINARY_INV)

    # cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]]) ->  image, contours, hierarchy
    image, contours, hierarchy = cv2.findContours(image,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(image_orig,contours,-1,(255,255,255),3)

    # show the frame
    cv2.imshow("Frame", image_orig)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break