Vert.x rpm spec
===============
##1. Distro support

Tested working on:

* RHEL 6 x86_64

##2. How to install

###2.1. Scripted installation

    $ cd <git repo dir>
    $ ./build.sh
    $ sudo yum install ~/rpmbuild/RPMS/x86_64/vertx-X.X.X-X.el6.x86_64.rpm --nogpgcheck

###2.2. Manual installation

####2.2.1. RHEL/CentOS/SL/OL 6

    $ sudo yum install -y rpm-build rpmdevtools
    $ rpmdev-setuptree
    $ cp <git repo dir>/vertx.spec ~/rpmbuild/SPECS/
    $ spectool -g -R ~/rpmbuild/SPECS/vertx.spec
    $ rpmbuild --clean -ba ~/rpmbuild/SPECS/vertx.spec
    $ sudo yum install ~/rpmbuild/RPMS/x86_64/vertx-X.X.X-X.el6.x86_64.rpm --nogpgcheck

####2.2.2. RHEL/CentOS/SL/OL 5

when you try to build on el5, must enable the EPEL repository.

    $ sudo rpm -ivh http://dl.fedoraproject.org/pub/epel/5/x86_64/epel-release-5-4.noarch.rpm
    $ sudo yum install -y rpm-build rpmdevtools
    $ mkdir ~/rpmbuild
    $ cd ~/rpmbuild
    $ rpmdev-setuptree
    $ cp <git repo dir>/vertx.spec ~/rpmbuild/SPECS/
    $ spectool -g -R ~/rpmbuild/SPECS/vertx.spec
    $ rpmbuild --clean -ba ~/rpmbuild/SPECS/vertx.spec
    $ sudo yum install ~/rpmbuild/RPMS/x86_64/vertx-X.X.X-X.x86_64.rpm --nogpgcheck