Example of site-specific configuration for TE-based test suites
===============================================================

Site-specific configuration may contain sensitive information about
internal network, number of test configurations, regressions schedule
etc and, therefore, is kept private.

The repository provides an example of site-specific configuration with
the best practices on how to define it. It may be used as a reference to
create your site-specific configuration.


# Generic files

``logger.conf`` contains recommended polling and rotation parameters and
defines live log listeners which should be disabled by default. See
listener **name** and **url** parameters which must be customized in
your case. Many log listeners may be defined.


# Test rigs definitions

Test rigs definitions are located in ``run`` and ``env`` directories.

Names of files in ``run`` directory match test configurations names
passed as ``--cfg=`` command-line option when you run testing.
Format of the file is a simple list of command-line options to be
passed to ``run.sh`` (and ``dispatcher.sh`` afterwards).

Files in ``env`` directory contain definitions of Bash environment
variables. Temporary (internal) variables used by helper scripts
should not be exported. Variables which are used in RCF and CS
configuration files must be exported.

By default it is assumed that SSH is already setup to provide
password-less access to test hosts. However, if required, environment
variables are supported to tune SSH ports, users, keys and proxy.
See ``ts-conf/rcf.conf`` for details.

Also it is assumed that password-less sudo if allowed for the user on
test hosts.

The following test configuration examples are available.


## frodo-sam - two hosts back-to-back with 2-ports NIC in each host

The configuration is internally defined in terms of host #1 (**frodo**) and
host #2 (**sam**) to make two configurations:

 1. **frodo** (see ``run/frodo``, use ``--cfg=frodo``) where NIC at **frodo**
    is used as *DUT* and NIC at **sam** is used as *Tester*.
    Helper script ``scripts/iut.h1`` does corresponding translation from
    H1/H2 to IUT/TST1 terminology.

 2. **sam** (see ``run/sam``, use ``--cfg=sam``) where NIC at **sam**
    is used as *DUT* and NIC at **frodo** is used as *Tester*.
    Helper script ``scripts/iut.h2`` does corresponding translation from
    H1/H2 to IUT/TST1 terminology.


## merry-pippin - two hosts back-to-back with three 2-ports NICs in each host

The configuration is internally defined in terms of host #1 (**merry**) and
host #2 (**pippin**) to make six configurations (two for each NIC pair):

 1. **merry-e810** (see ``run/merry-e810``, use ``--cfg=merry-e810``) -
    two Intel E810 NICs back-to-back at **merry** as *DUT* and
    **pippin** as *Tester*.

 2. **merry-mcx5** (see ``run/merry-mcx5``, use ``--cfg=merry-mcx5``) -
    two Mellanox ConnectX-5 NICs back-to-back at **merry** as *DUT* and
    **pippin** as *Tester*.

 3. **merry-x710** (see ``run/merry-x710``, use ``--cfg=merry-x710``) -
    two Intel E810 NICs back-to-back at **merry** as *DUT* and
    **pippin** as *Tester*.

 4. **pippin-e810** (see ``run/pippin-e810``, use ``--cfg=pippin-e810``) -
    two Intel E810 NICs back-to-back at **pippin** as *DUT* and
    **merry** as *Tester*.

 5. **pippin-mcx5** (see ``run/pippin-mcx5``, use ``--cfg=pippin-mcx5``) -
    two Mellanox ConnectX-5 NICs back-to-back at **pippin** as *DUT* and
    **merry** as *Tester*.

 6. **pippin-x710** (see ``run/pippin-x710``, use ``--cfg=pippin-x710``) -
    two Intel E810 NICs back-to-back at **pippin** as *DUT* and
    **merry** as *Tester*.


## bilbo1-bilbo2 - two virtual machines back-to-back

The configuration is internally defined in terms of host #1 (**bilbo1**) and
host #2 (**bilbo2**) to make two configurations:

 1. **bilbo1** (see ``run/bilbo1``, use ``--cfg=bilbo1``) where NIC at
    **bilbo1** is used as *DUT* and NIC at **bilbo2** is used as *Tester*.

 2. **bilbo2** (see ``run/bilbo2``, use ``--cfg=bilbo2``) where NIC at
    **bilbo2** is used as *DUT* and NIC at **bilbo1** is used as *Tester*.

These configurations use auxiliary host **bilbo** to listen to netconsole
kernel logs from **bilbo1** and **bilbo2**. Test agent on **bilbo** runs
under login user and does not require password-less sudo.

Note that different PCI device (not virtio-net) should be used for
management network used for control traffic.
