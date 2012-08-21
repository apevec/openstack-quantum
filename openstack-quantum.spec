#
# This is 2012.1 essex release
#

Name:		openstack-quantum
Version:	2012.1
Release:	8%{?dist}
Summary:	Virtual network service for OpenStack (quantum)

Group:		Applications/System
License:	ASL 2.0
URL:		http://launchpad.net/quantum/

Source0:	http://tarballs.openstack.org/quantum/quantum-2012.1~20120715.784.tar.gz
Source1:	quantum.logrotate
Source2:	quantum-sudoers
Source4:	quantum-server-setup
Source5:	quantum-node-setup

Source10:	quantum-server.init
Source20:	quantum-server.upstart
Source11:	quantum-linuxbridge-agent.init
Source21:	quantum-linuxbridge-agent.upstart
Source12:	quantum-openvswitch-agent.init
Source22:	quantum-openvswitch-agent.upstart
Source13:	quantum-ryu-agent.init
Source23:	quantum-ryu-agent.upstart

# This is EPEL specific and not upstream
Patch100:         openstack-quantum-newdeps.patch

BuildArch:	noarch

BuildRequires:	python2-devel
BuildRequires:	python-setuptools
# Build require these parallel versions
# as setup.py build imports quantum.openstack.common.setup
# which will then check for these
BuildRequires:	python-sqlalchemy0.7
BuildRequires:	python-webob1.0
BuildRequires:	python-paste-deploy1.5
BuildRequires:	python-routes1.12
BuildRequires:	dos2unix

Requires:	python-quantum = %{version}-%{release}
Requires:	openstack-utils

Requires(post):   chkconfig
Requires(postun): initscripts
Requires(preun):  chkconfig
Requires(preun):  initscripts
Requires(pre):    shadow-utils


%description
Quantum is a virtual network service for Openstack, and a part of
Netstack. Just like OpenStack Nova provides an API to dynamically
request and configure virtual servers, Quantum provides an API to
dynamically request and configure virtual networks. These networks
connect "interfaces" from other OpenStack services (e.g., virtual NICs
from Nova VMs). The Quantum API supports extensions to provide
advanced network capabilities (e.g., QoS, ACLs, network monitoring,
etc.)


%package -n python-quantum
Summary:	Quantum Python libraries
Group:		Applications/System

Requires:	python-quantumclient >= %{version}
Requires:	MySQL-python
Requires:	python-configobj
Requires:	python-eventlet
Requires:	python-lxml
Requires:	python-gflags
Requires:	python-anyjson
Requires:	python-paste-deploy1.5
Requires:	python-routes1.12
Requires:	python-sqlalchemy0.7
Requires:	python-webob1.0


%description -n python-quantum
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum Python library.


%package -n openstack-quantum-cisco
Summary:	Quantum Cisco plugin
Group:		Applications/System

Requires:	openstack-quantum = %{version}-%{release}


%description -n openstack-quantum-cisco
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum plugin that implements virtual
networks using Cisco UCS and Nexus.


%package -n openstack-quantum-linuxbridge
Summary:	Quantum linuxbridge plugin
Group:		Applications/System

Requires:	openstack-quantum = %{version}-%{release}
Requires:	bridge-utils
Requires:	sudo


%description -n openstack-quantum-linuxbridge
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum plugin that implements virtual
networks as VLANs using Linux bridging.


%package -n openstack-quantum-nicira
Summary:	Quantum Nicira plugin
Group:		Applications/System

Requires:	openstack-quantum = %{version}-%{release}


%description -n openstack-quantum-nicira
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum plugin that implements virtual
networks using Nicira NVP.


%package -n openstack-quantum-openvswitch
Summary:	Quantum openvswitch plugin
Group:		Applications/System

Requires:	openstack-quantum = %{version}-%{release}
Requires:	sudo


%description -n openstack-quantum-openvswitch
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum plugin that implements virtual
networks using Open vSwitch.


%package -n openstack-quantum-ryu
Summary:	Quantum ryu plugin
Group:		Applications/System

Requires:	openstack-quantum = %{version}-%{release}
Requires:	sudo


%description -n openstack-quantum-ryu
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum plugin that implements virtual
networks using the Ryu Network Operating System.


%prep
%setup -q -n quantum-%{version}

# Apply EPEL patch
%patch100 -p1

find quantum -name \*.py -exec sed -i '/\/usr\/bin\/env python/d' {} \;

chmod 644 quantum/plugins/cisco/README
dos2unix quantum/plugins/cisco/README


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Remove unused files
rm -rf %{buildroot}%{python_sitelib}/bin
rm -rf %{buildroot}%{python_sitelib}/doc
rm -rf %{buildroot}%{python_sitelib}/tools
rm -rf %{buildroot}%{python_sitelib}/quantum/tests
rm -rf %{buildroot}%{python_sitelib}/quantum/plugins/*/tests
rm -f %{buildroot}%{python_sitelib}/quantum/plugins/*/run_tests.*
rm %{buildroot}/usr/etc/quantum/quantum.conf.test
rm %{buildroot}/usr/etc/init.d/quantum-server

# Install execs (using hand-coded rather than generated versions)
install -p -D -m 755 bin/quantum-server %{buildroot}%{_bindir}/quantum-server
install -p -D -m 755 bin/quantum-linuxbridge-agent %{buildroot}%{_bindir}/quantum-linuxbridge-agent
install -p -D -m 755 bin/quantum-openvswitch-agent %{buildroot}%{_bindir}/quantum-openvswitch-agent
install -p -D -m 755 bin/quantum-ryu-agent %{buildroot}%{_bindir}/quantum-ryu-agent
install -p -D -m 755 bin/quantum-rootwrap %{buildroot}%{_bindir}/quantum-rootwrap

# Move config files to proper location
install -d -m 755 %{buildroot}%{_sysconfdir}/quantum
mv %{buildroot}/usr/etc/quantum/* %{buildroot}%{_sysconfdir}/quantum
chmod 640  %{buildroot}%{_sysconfdir}/quantum/plugins/*/*.ini

# Configure plugin agents to use quantum-rootwrap
for f in %{buildroot}%{_sysconfdir}/quantum/plugins/*/*.ini; do
    sed -i 's/root_helper = sudo/root_helper = sudo quantum-rootwrap/g' $f
done

# Install logrotate
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-quantum

# Install sudoers
install -p -D -m 440 %{SOURCE2} %{buildroot}%{_sysconfdir}/sudoers.d/quantum

# Install sysv init scripts
install -p -D -m 755 %{SOURCE10} %{buildroot}%{_initrddir}/quantum-server
install -p -D -m 755 %{SOURCE11} %{buildroot}%{_initrddir}/quantum-linuxbridge-agent
install -p -D -m 755 %{SOURCE12} %{buildroot}%{_initrddir}/quantum-openvswitch-agent
install -p -D -m 755 %{SOURCE13} %{buildroot}%{_initrddir}/quantum-ryu-agent

# Setup directories
install -d -m 755 %{buildroot}%{_datadir}/quantum
install -d -m 755 %{buildroot}%{_sharedstatedir}/quantum
install -d -m 755 %{buildroot}%{_localstatedir}/log/quantum
install -d -m 755 %{buildroot}%{_localstatedir}/run/quantum

# Install setup helper scripts
install -p -D -m 755 %{SOURCE4} %{buildroot}%{_bindir}/quantum-server-setup
install -p -D -m 755 %{SOURCE5} %{buildroot}%{_bindir}/quantum-node-setup

# Install upstart jobs examples
install -p -m 644 %{SOURCE20} %{buildroot}%{_datadir}/quantum/
install -p -m 644 %{SOURCE21} %{buildroot}%{_datadir}/quantum/
install -p -m 644 %{SOURCE22} %{buildroot}%{_datadir}/quantum/
install -p -m 644 %{SOURCE23} %{buildroot}%{_datadir}/quantum/

%pre
getent group quantum >/dev/null || groupadd -r quantum --gid 164
getent passwd quantum >/dev/null || \
    useradd --uid 164 -r -g quantum -d %{_sharedstatedir}/quantum -s /sbin/nologin \
    -c "OpenStack Quantum Daemons" quantum
exit 0


%post
if [ $1 -eq 1 ] ; then
    # Initial installation
    /sbin/chkconfig --add quantum-server
fi

%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /sbin/service quantum-server stop >/dev/null 2>&1
    /sbin/chkconfig --del quantum-server
fi

%postun
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /sbin/service quantum-server condrestart >/dev/null 2>&1 || :
fi


%post -n openstack-quantum-linuxbridge
if [ $1 -eq 1 ] ; then
    # Initial installation
    /sbin/chkconfig --add quantum-linuxbridge-agent
fi

%preun -n openstack-quantum-linuxbridge
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /sbin/service quantum-linuxbridge-agent stop >/dev/null 2>&1
    /sbin/chkconfig --del quantum-linuxbridge-agent
fi

%postun -n openstack-quantum-linuxbridge
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /sbin/service quantum-linuxbridge-agent condrestart >/dev/null 2>&1 || :
fi


%post -n openstack-quantum-openvswitch
if [ $1 -eq 1 ] ; then
    # Initial installation
    /sbin/chkconfig --add quantum-openvswitch-agent
fi

%preun -n openstack-quantum-openvswitch
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /sbin/service quantum-openvswitch-agent stop >/dev/null 2>&1
    /sbin/chkconfig --del quantum-openvswitch-agent
fi

%postun -n openstack-quantum-openvswitch
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /sbin/service quantum-openvswitch-agent condrestart >/dev/null 2>&1 || :
fi


%post -n openstack-quantum-ryu
if [ $1 -eq 1 ] ; then
    # Initial installation
    /sbin/chkconfig --add quantum-ryu-agent
fi

%preun -n openstack-quantum-ryu
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /sbin/service quantum-ryu-agent stop >/dev/null 2>&1
    /sbin/chkconfig --del quantum-ryu-agent
fi

%postun -n openstack-quantum-ryu
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /sbin/service quantum-ryu-agent condrestart >/dev/null 2>&1 || :
fi


%files
%doc LICENSE
%doc README
%{_bindir}/quantum-server
%{_bindir}/quantum-rootwrap
%{_bindir}/quantum-server-setup
%{_bindir}/quantum-node-setup
%{_initrddir}/quantum-server
%dir %{_datadir}/quantum
%{_datadir}/quantum/quantum-server.upstart
%dir %{_sysconfdir}/quantum
%config(noreplace) %{_sysconfdir}/quantum/quantum.conf
%config(noreplace) %{_sysconfdir}/quantum/plugins.ini
%dir %{_sysconfdir}/quantum/plugins
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%config(noreplace) %{_sysconfdir}/sudoers.d/quantum
%dir %attr(0755, quantum, quantum) %{_sharedstatedir}/quantum
%dir %attr(0755, quantum, quantum) %{_localstatedir}/log/quantum
%dir %attr(0755, quantum, quantum) %{_localstatedir}/run/quantum


%files -n python-quantum
# note that %%{python_sitelib}/quantum is owned by python-quantumclient
%doc LICENSE
%doc README
%{python_sitelib}/quantum/*
%exclude %{python_sitelib}/quantum/extensions/_credential_view.py*
%exclude %{python_sitelib}/quantum/extensions/portprofile.py*
%exclude %{python_sitelib}/quantum/extensions/novatenant.py*
%exclude %{python_sitelib}/quantum/extensions/credential.py*
%exclude %{python_sitelib}/quantum/extensions/_novatenant_view.py*
%exclude %{python_sitelib}/quantum/extensions/multiport.py*
%exclude %{python_sitelib}/quantum/extensions/_pprofiles.py*
%exclude %{python_sitelib}/quantum/extensions/qos.py*
%exclude %{python_sitelib}/quantum/extensions/_qos_view.py*
%exclude %{python_sitelib}/quantum/plugins/cisco
%exclude %{python_sitelib}/quantum/plugins/linuxbridge
%exclude %{python_sitelib}/quantum/plugins/nicira
%exclude %{python_sitelib}/quantum/plugins/openvswitch
%exclude %{python_sitelib}/quantum/plugins/ryu
%exclude %{python_sitelib}/quantum/rootwrap/*-agent.py*
%{python_sitelib}/quantum-%%{version}-*.egg-info


%files -n openstack-quantum-cisco
%doc LICENSE
%doc quantum/plugins/cisco/README
%{python_sitelib}/quantum/extensions/_credential_view.py*
%{python_sitelib}/quantum/extensions/portprofile.py*
%{python_sitelib}/quantum/extensions/novatenant.py*
%{python_sitelib}/quantum/extensions/credential.py*
%{python_sitelib}/quantum/extensions/_novatenant_view.py*
%{python_sitelib}/quantum/extensions/multiport.py*
%{python_sitelib}/quantum/extensions/_pprofiles.py*
%{python_sitelib}/quantum/extensions/qos.py*
%{python_sitelib}/quantum/extensions/_qos_view.py*
%{python_sitelib}/quantum/plugins/cisco
%dir %{_sysconfdir}/quantum/plugins/cisco
%config(noreplace) %attr(-, root, quantum) %{_sysconfdir}/quantum/plugins/cisco/*.ini


%files -n openstack-quantum-linuxbridge
%doc LICENSE
%doc quantum/plugins/linuxbridge/README
%{_bindir}/quantum-linuxbridge-agent
%{_initrddir}/quantum-linuxbridge-agent
%{_datadir}/quantum/quantum-linuxbridge-agent.upstart
%{python_sitelib}/quantum/plugins/linuxbridge
%{python_sitelib}/quantum/rootwrap/linuxbridge-agent.py*
%dir %{_sysconfdir}/quantum/plugins/linuxbridge
%config(noreplace) %attr(-, root, quantum) %{_sysconfdir}/quantum/plugins/linuxbridge/*.ini


%files -n openstack-quantum-nicira
%doc LICENSE
%doc quantum/plugins/nicira/nicira_nvp_plugin/README
%{python_sitelib}/quantum/plugins/nicira
%dir %{_sysconfdir}/quantum/plugins/nicira
%config(noreplace) %attr(-, root, quantum) %{_sysconfdir}/quantum/plugins/nicira/*.ini


%files -n openstack-quantum-openvswitch
%doc LICENSE
%doc quantum/plugins/openvswitch/README
%{_bindir}/quantum-openvswitch-agent
%{_initrddir}/quantum-openvswitch-agent
%{_datadir}/quantum/quantum-openvswitch-agent.upstart
%{python_sitelib}/quantum/plugins/openvswitch
%{python_sitelib}/quantum/rootwrap/openvswitch-agent.py*
%dir %{_sysconfdir}/quantum/plugins/openvswitch
%config(noreplace) %attr(-, root, quantum) %{_sysconfdir}/quantum/plugins/openvswitch/*.ini


%files -n openstack-quantum-ryu
%doc LICENSE
%doc quantum/plugins/ryu/README
%{_bindir}/quantum-ryu-agent
%{_initrddir}/quantum-ryu-agent
%{_datadir}/quantum/quantum-ryu-agent.upstart
%{python_sitelib}/quantum/plugins/ryu
%{python_sitelib}/quantum/rootwrap/ryu-agent.py*
%dir %{_sysconfdir}/quantum/plugins/ryu
%config(noreplace) %attr(-, root, quantum) %{_sysconfdir}/quantum/plugins/ryu/*.ini


%changelog
* Tue Aug 21 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-8
- fix database config generated by install scripts (#847785)

* Wed Jul 25 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-6
- Update to 20120715 essex stable branch snapshot

* Mon May 28 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-5
- Fix helper scripts to use the always available openstack-config util

* Mon May 07 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-4
- Fix handling of the mysql service in quantum-server-setup

* Tue May 01 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-3
- Start the services later in the boot sequence

* Wed Apr 25 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-2
- Use parallel installed versions of python-routes and python-paste-deploy

* Thu Apr 12 2012 Pádraig Brady <pbrady@redhat.com> - 2012.1-1
- Initial essex release
