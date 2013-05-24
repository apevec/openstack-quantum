#
# This is 2013.1 release
#
%global release_name grizzly

Name:		openstack-quantum
Version:	2013.1.1
Release:	3%{?dist}
Summary:	OpenStack Networking Service

Group:		Applications/System
License:	ASL 2.0
URL:		http://launchpad.net/quantum/

Source0:	http://launchpad.net/quantum/%{release_name}/%{version}/+download/quantum-%{version}.tar.gz
Source1:	quantum.logrotate
Source2:	quantum-sudoers
Source4:	quantum-server-setup
Source5:	quantum-node-setup
Source6:	quantum-dhcp-setup
Source7:	quantum-l3-setup

Source10:	quantum-server.init
Source20:	quantum-server.upstart
Source11:	quantum-linuxbridge-agent.init
Source21:	quantum-linuxbridge-agent.upstart
Source12:	quantum-openvswitch-agent.init
Source22:	quantum-openvswitch-agent.upstart
Source13:	quantum-ryu-agent.init
Source23:	quantum-ryu-agent.upstart
Source14:	quantum-nec-agent.init
Source24:	quantum-nec-agent.upstart
Source15:	quantum-dhcp-agent.init
Source25:	quantum-dhcp-agent.upstart
Source16:	quantum-l3-agent.init
Source26:	quantum-l3-agent.upstart
Source17:	quantum-metadata-agent.init
Source27:	quantum-metadata-agent.upstart
Source18:	quantum-ovs-cleanup.init
Source28:	quantum-ovs-cleanup.upstart
Source19:	quantum-lbaas-agent.init
Source29:	quantum-lbaas-agent.upstart

#
# patches_base=2013.1.1
#
Patch0001: 0001-use-parallel-installed-versions-in-RHEL6.patch
Patch0002: 0002-dhcp-agent-make-dnsmasq-tags-work-with-RHEL-6.patch
Patch0003: 0003-Create-veth-peer-in-namespace.patch
Patch0004: 0004-Add-kill-metadata-rootwrap-filter-to-support-RHEL.patch

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
Requires:       python-keystone

Requires(post):   chkconfig
Requires(postun): initscripts
Requires(preun):  chkconfig
Requires(preun):  initscripts
Requires(pre):    shadow-utils

# dnsmasq is not a hard requirement, but is currently the only option
# when quantum-dhcp-agent is deployed.
Requires:	dnsmasq


%description
Quantum is a virtual network service for Openstack. Just like
OpenStack Nova provides an API to dynamically request and configure
virtual servers, Quantum provides an API to dynamically request and
configure virtual networks. These networks connect "interfaces" from
other OpenStack services (e.g., virtual NICs from Nova VMs). The
Quantum API supports extensions to provide advanced network
capabilities (e.g., QoS, ACLs, network monitoring, etc.)


%package -n python-quantum
Summary:	Quantum Python libraries
Group:		Applications/System

Requires:	MySQL-python
Requires:	python-alembic
Requires:	python-amqplib
Requires:	python-anyjson
Requires:	python-eventlet
Requires:	python-greenlet
Requires:	python-httplib2
Requires:	python-iso8601
Requires:	python-kombu
Requires:	python-lxml
Requires:	python-paste-deploy1.5
Requires:	python-routes1.12
Requires:	python-sqlalchemy0.7
Requires:	python-webob1.0
Requires:	python-netaddr
Requires:	python-oslo-config
Requires:	python-qpid
Requires:	python-quantumclient >= 1:2.1.10
Requires:	sudo

%description -n python-quantum
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum Python library.


%package -n openstack-quantum-bigswitch
Summary:	Quantum Big Switch plugin
Group:		Applications/System

Requires:	openstack-quantum = %{version}-%{release}


%description -n openstack-quantum-bigswitch
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum plugin that implements virtual
networks using the FloodLight Openflow Controller or the Big Switch
Networks Controller.


%package -n openstack-quantum-brocade
Summary:	Quantum Brocade plugin
Group:		Applications/System

Requires:	openstack-quantum = %{version}-%{release}


%description -n openstack-quantum-brocade
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum plugin that implements virtual
networks using Brocade VCS switches running NOS.


%package -n openstack-quantum-cisco
Summary:	Quantum Cisco plugin
Group:		Applications/System

Requires:	openstack-quantum = %{version}-%{release}
Requires:	python-configobj


%description -n openstack-quantum-cisco
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum plugin that implements virtual
networks using Cisco UCS and Nexus.


%package -n openstack-quantum-hyperv
Summary:	Quantum Hyper-V plugin
Group:		Applications/System

Requires:	openstack-quantum = %{version}-%{release}


%description -n openstack-quantum-hyperv
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum plugin that implements virtual
networks using Microsoft Hyper-V.


%package -n openstack-quantum-linuxbridge
Summary:	Quantum linuxbridge plugin
Group:		Applications/System

Requires:	bridge-utils
Requires:	openstack-quantum = %{version}-%{release}
Requires:	python-pyudev


%description -n openstack-quantum-linuxbridge
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum plugin that implements virtual
networks as VLANs using Linux bridging.


%package -n openstack-quantum-midonet
Summary:	Quantum MidoNet plugin
Group:		Applications/System

Requires:	openstack-quantum = %{version}-%{release}


%description -n openstack-quantum-midonet
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum plugin that implements virtual
networks using MidoNet from Midokura.


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
Requires:	openvswitch


%description -n openstack-quantum-openvswitch
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum plugin that implements virtual
networks using Open vSwitch.


%package -n openstack-quantum-plumgrid
Summary:	Quantum PLUMgrid plugin
Group:		Applications/System

Requires:	openstack-quantum = %{version}-%{release}


%description -n openstack-quantum-plumgrid
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum plugin that implements virtual
networks using the PLUMgrid platform.


%package -n openstack-quantum-ryu
Summary:	Quantum Ryu plugin
Group:		Applications/System

Requires:	openstack-quantum = %{version}-%{release}


%description -n openstack-quantum-ryu
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum plugin that implements virtual
networks using the Ryu Network Operating System.


%package -n openstack-quantum-nec
Summary:	Quantum NEC plugin
Group:		Applications/System

Requires:	openstack-quantum = %{version}-%{release}


%description -n openstack-quantum-nec
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum plugin that implements virtual
networks using the NEC OpenFlow controller.


%package -n openstack-quantum-metaplugin
Summary:	Quantum meta plugin
Group:		Applications/System

Requires:	openstack-quantum = %{version}-%{release}


%description -n openstack-quantum-metaplugin
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the quantum plugin that implements virtual
networks using multiple other quantum plugins.


%prep
%setup -q -n quantum-%{version}

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1

sed -i 's/%{version}/%{version}/' PKG-INFO

find quantum -name \*.py -exec sed -i '/\/usr\/bin\/env python/d' {} \;

# Remove bundled egg-info
rm -rf quantum.egg-info

# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

chmod 644 quantum/plugins/cisco/README

# Adjust configuration file content
sed -i 's/debug = True/debug = False/' etc/quantum.conf
sed -i 's/\# auth_strategy = keystone/auth_strategy = noauth/' etc/quantum.conf


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
rm %{buildroot}/usr/etc/init.d/quantum-server

# Install execs (using hand-coded rather than generated versions)
install -p -D -m 755 bin/quantum-check-nvp-config %{buildroot}%{_bindir}/quantum-check-nvp-config
install -p -D -m 755 bin/quantum-db-manage %{buildroot}%{_bindir}/quantum-db-manage
install -p -D -m 755 bin/quantum-debug %{buildroot}%{_bindir}/quantum-debug
install -p -D -m 755 bin/quantum-dhcp-agent %{buildroot}%{_bindir}/quantum-dhcp-agent
install -p -D -m 755 bin/quantum-dhcp-agent-dnsmasq-lease-update %{buildroot}%{_bindir}/quantum-dhcp-agent-dnsmasq-lease-update
install -p -D -m 755 bin/quantum-l3-agent %{buildroot}%{_bindir}/quantum-l3-agent
install -p -D -m 755 bin/quantum-lbaas-agent %{buildroot}%{_bindir}/quantum-lbaas-agent
install -p -D -m 755 bin/quantum-linuxbridge-agent %{buildroot}%{_bindir}/quantum-linuxbridge-agent
install -p -D -m 755 bin/quantum-metadata-agent %{buildroot}%{_bindir}/quantum-metadata-agent
install -p -D -m 755 bin/quantum-nec-agent %{buildroot}%{_bindir}/quantum-nec-agent
install -p -D -m 755 bin/quantum-netns-cleanup %{buildroot}%{_bindir}/quantum-netns-cleanup
install -p -D -m 755 bin/quantum-ns-metadata-proxy %{buildroot}%{_bindir}/quantum-ns-metadata-proxy
install -p -D -m 755 bin/quantum-openvswitch-agent %{buildroot}%{_bindir}/quantum-openvswitch-agent
install -p -D -m 755 bin/quantum-ovs-cleanup %{buildroot}%{_bindir}/quantum-ovs-cleanup
install -p -D -m 755 bin/quantum-rootwrap %{buildroot}%{_bindir}/quantum-rootwrap
install -p -D -m 755 bin/quantum-ryu-agent %{buildroot}%{_bindir}/quantum-ryu-agent
install -p -D -m 755 bin/quantum-server %{buildroot}%{_bindir}/quantum-server
install -p -D -m 755 bin/quantum-usage-audit %{buildroot}%{_bindir}/quantum-usage-audit

# Move rootwrap files to proper location
install -d -m 755 %{buildroot}%{_datarootdir}/quantum/rootwrap
mv %{buildroot}/usr/etc/quantum/rootwrap.d/*.filters %{buildroot}%{_datarootdir}/quantum/rootwrap

# Move config files to proper location
install -d -m 755 %{buildroot}%{_sysconfdir}/quantum
mv %{buildroot}/usr/etc/quantum/* %{buildroot}%{_sysconfdir}/quantum
chmod 640  %{buildroot}%{_sysconfdir}/quantum/plugins/*/*.ini

# Configure agents to use quantum-rootwrap
sed -i 's/^root_helper.*/root_helper = sudo quantum-rootwrap \/etc\/quantum\/rootwrap.conf/g' %{buildroot}%{_sysconfdir}/quantum/quantum.conf

# Configure quantum-dhcp-agent state_path
sed -i 's/state_path = \/opt\/stack\/data/state_path = \/var\/lib\/quantum/' %{buildroot}%{_sysconfdir}/quantum/dhcp_agent.ini

# Install logrotate
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-quantum

# Install sudoers
install -p -D -m 440 %{SOURCE2} %{buildroot}%{_sysconfdir}/sudoers.d/quantum

# Install sysv init scripts
install -p -D -m 755 %{SOURCE10} %{buildroot}%{_initrddir}/quantum-server
install -p -D -m 755 %{SOURCE11} %{buildroot}%{_initrddir}/quantum-linuxbridge-agent
install -p -D -m 755 %{SOURCE12} %{buildroot}%{_initrddir}/quantum-openvswitch-agent
install -p -D -m 755 %{SOURCE13} %{buildroot}%{_initrddir}/quantum-ryu-agent
install -p -D -m 755 %{SOURCE14} %{buildroot}%{_initrddir}/quantum-nec-agent
install -p -D -m 755 %{SOURCE15} %{buildroot}%{_initrddir}/quantum-dhcp-agent
install -p -D -m 755 %{SOURCE16} %{buildroot}%{_initrddir}/quantum-l3-agent
install -p -D -m 755 %{SOURCE17} %{buildroot}%{_initrddir}/quantum-metadata-agent
install -p -D -m 755 %{SOURCE18} %{buildroot}%{_initrddir}/quantum-ovs-cleanup
install -p -D -m 755 %{SOURCE19} %{buildroot}%{_initrddir}/quantum-lbaas-agent

# Setup directories
install -d -m 755 %{buildroot}%{_datadir}/quantum
install -d -m 755 %{buildroot}%{_sharedstatedir}/quantum
install -d -m 755 %{buildroot}%{_localstatedir}/log/quantum
install -d -m 755 %{buildroot}%{_localstatedir}/run/quantum

# Install setup helper scripts
install -p -D -m 755 %{SOURCE4} %{buildroot}%{_bindir}/quantum-server-setup
install -p -D -m 755 %{SOURCE5} %{buildroot}%{_bindir}/quantum-node-setup
install -p -D -m 755 %{SOURCE6} %{buildroot}%{_bindir}/quantum-dhcp-setup
install -p -D -m 755 %{SOURCE7} %{buildroot}%{_bindir}/quantum-l3-setup

# Install upstart jobs examples
install -p -m 644 %{SOURCE20} %{buildroot}%{_datadir}/quantum/
install -p -m 644 %{SOURCE21} %{buildroot}%{_datadir}/quantum/
install -p -m 644 %{SOURCE22} %{buildroot}%{_datadir}/quantum/
install -p -m 644 %{SOURCE23} %{buildroot}%{_datadir}/quantum/
install -p -m 644 %{SOURCE24} %{buildroot}%{_datadir}/quantum/
install -p -m 644 %{SOURCE25} %{buildroot}%{_datadir}/quantum/
install -p -m 644 %{SOURCE26} %{buildroot}%{_datadir}/quantum/
install -p -m 644 %{SOURCE27} %{buildroot}%{_datadir}/quantum/
install -p -m 644 %{SOURCE28} %{buildroot}%{_datadir}/quantum/
install -p -m 644 %{SOURCE29} %{buildroot}%{_datadir}/quantum/

# Install version info file
cat > %{buildroot}%{_sysconfdir}/quantum/release <<EOF
[Quantum]
vendor = Fedora Project
product = OpenStack Quantum
package = %{release}
EOF

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
    /sbin/service quantum-dhcp-agent stop >/dev/null 2>&1
    /sbin/chkconfig --del quantum-dhcp-agent
    /sbin/service quantum-l3-agent stop >/dev/null 2>&1
    /sbin/chkconfig --del quantum-l3-agent
	/sbin/service quantum-metadata-agent stop >/dev/null 2>&1
	/sbin/chkconfig --del quantum-metadata-agent
	/sbin/service quantum-lbaas-agent stop >/dev/null 2>&1
	/sbin/chkconfig --del quantum-lbaas-agent
fi

%postun
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /sbin/service quantum-server condrestart >/dev/null 2>&1 || :
    /sbin/service quantum-dhcp-agent condrestart >/dev/null 2>&1 || :
    /sbin/service quantum-l3-agent condrestart >/dev/null 2>&1 || :
    /sbin/service quantum-metadata-agent condrestart >/dev/null 2>&1 || :
    /sbin/service quantum-lbaas-agent condrestart >/dev/null 2>&1 || :
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


%preun -n openstack-quantum-nec
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /sbin/service quantum-nec-agent stop >/dev/null 2>&1
    /sbin/chkconfig --del quantum-nec-agent
fi


%postun -n openstack-quantum-nec
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /sbin/service quantum-nec-agent condrestart >/dev/null 2>&1 || :
fi


%files
%doc LICENSE
%doc README
%{_bindir}/quantum-db-manage
%{_bindir}/quantum-debug
%{_bindir}/quantum-dhcp-agent
%{_bindir}/quantum-dhcp-agent-dnsmasq-lease-update
%{_bindir}/quantum-dhcp-setup
%{_bindir}/quantum-l3-agent
%{_bindir}/quantum-l3-setup
%{_bindir}/quantum-lbaas-agent
%{_bindir}/quantum-metadata-agent
%{_bindir}/quantum-netns-cleanup
%{_bindir}/quantum-node-setup
%{_bindir}/quantum-ns-metadata-proxy
%{_bindir}/quantum-rootwrap
%{_bindir}/quantum-server
%{_bindir}/quantum-server-setup
%{_bindir}/quantum-usage-audit
%{_initrddir}/quantum-server
%{_initrddir}/quantum-dhcp-agent
%{_initrddir}/quantum-l3-agent
%{_initrddir}/quantum-metadata-agent
%{_initrddir}/quantum-ovs-cleanup
%{_initrddir}/quantum-lbaas-agent
%dir %{_datadir}/quantum
%{_datadir}/quantum/quantum-server.upstart
%{_datadir}/quantum/quantum-dhcp-agent.upstart
%{_datadir}/quantum/quantum-metadata-agent.upstart
%{_datadir}/quantum/quantum-l3-agent.upstart
%{_datadir}/quantum/quantum-lbaas-agent.upstart
%dir %{_sysconfdir}/quantum
%{_sysconfdir}/quantum/release
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/api-paste.ini
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/dhcp_agent.ini
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/l3_agent.ini
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/metadata_agent.ini
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/lbaas_agent.ini
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/policy.json
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/quantum.conf
%config(noreplace) %{_sysconfdir}/quantum/rootwrap.conf
%dir %{_sysconfdir}/quantum/plugins
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%config(noreplace) %{_sysconfdir}/sudoers.d/quantum
%dir %attr(0755, quantum, quantum) %{_sharedstatedir}/quantum
%dir %attr(0755, quantum, quantum) %{_localstatedir}/log/quantum
%dir %attr(0755, quantum, quantum) %{_localstatedir}/run/quantum
%dir %{_datarootdir}/quantum/rootwrap
%{_datarootdir}/quantum/rootwrap/dhcp.filters
%{_datarootdir}/quantum/rootwrap/iptables-firewall.filters
%{_datarootdir}/quantum/rootwrap/l3.filters
%{_datarootdir}/quantum/rootwrap/lbaas-haproxy.filters


%files -n python-quantum
%doc LICENSE
%doc README
%{python_sitelib}/quantum
%exclude %{python_sitelib}/quantum/plugins/bigswitch
%exclude %{python_sitelib}/quantum/plugins/brocade
%exclude %{python_sitelib}/quantum/plugins/cisco
%exclude %{python_sitelib}/quantum/plugins/hyperv
%exclude %{python_sitelib}/quantum/plugins/linuxbridge
%exclude %{python_sitelib}/quantum/plugins/metaplugin
%exclude %{python_sitelib}/quantum/plugins/midonet
%exclude %{python_sitelib}/quantum/plugins/nec
%exclude %{python_sitelib}/quantum/plugins/nicira
%exclude %{python_sitelib}/quantum/plugins/openvswitch
%exclude %{python_sitelib}/quantum/plugins/plumgrid
%exclude %{python_sitelib}/quantum/plugins/ryu
%{python_sitelib}/quantum-%%{version}-*.egg-info


%files -n openstack-quantum-bigswitch
%doc LICENSE
%doc quantum/plugins/bigswitch/README
%{python_sitelib}/quantum/plugins/bigswitch
%dir %{_sysconfdir}/quantum/plugins/bigswitch
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/plugins/bigswitch/*.ini


%files -n openstack-quantum-brocade
%doc LICENSE
%doc quantum/plugins/brocade/README.md
%{python_sitelib}/quantum/plugins/brocade
%dir %{_sysconfdir}/quantum/plugins/brocade
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/plugins/brocade/*.ini


%files -n openstack-quantum-cisco
%doc LICENSE
%doc quantum/plugins/cisco/README
%{python_sitelib}/quantum/plugins/cisco
%dir %{_sysconfdir}/quantum/plugins/cisco
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/plugins/cisco/*.ini


%files -n openstack-quantum-hyperv
%doc LICENSE
#%%doc quantum/plugins/hyperv/README
%{python_sitelib}/quantum/plugins/hyperv
%dir %{_sysconfdir}/quantum/plugins/hyperv
%exclude %{python_sitelib}/quantum/plugins/hyperv/agent
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/plugins/hyperv/*.ini


%files -n openstack-quantum-linuxbridge
%doc LICENSE
%doc quantum/plugins/linuxbridge/README
%{_bindir}/quantum-linuxbridge-agent
%{_initrddir}/quantum-linuxbridge-agent
%{_datadir}/quantum/quantum-linuxbridge-agent.upstart
%{python_sitelib}/quantum/plugins/linuxbridge
%{_datarootdir}/quantum/rootwrap/linuxbridge-plugin.filters
%dir %{_sysconfdir}/quantum/plugins/linuxbridge
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/plugins/linuxbridge/*.ini


%files -n openstack-quantum-midonet
%doc LICENSE
#%%doc quantum/plugins/midonet/README
%{python_sitelib}/quantum/plugins/midonet
%dir %{_sysconfdir}/quantum/plugins/midonet
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/plugins/midonet/*.ini


%files -n openstack-quantum-nicira
%doc LICENSE
%doc quantum/plugins/nicira/nicira_nvp_plugin/README
%{_bindir}/quantum-check-nvp-config
%{python_sitelib}/quantum/plugins/nicira
%dir %{_sysconfdir}/quantum/plugins/nicira
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/plugins/nicira/*.ini


%files -n openstack-quantum-openvswitch
%doc LICENSE
%doc quantum/plugins/openvswitch/README
%{_bindir}/quantum-openvswitch-agent
%{_bindir}/quantum-ovs-cleanup
%{_initrddir}/quantum-openvswitch-agent
%{_datadir}/quantum/quantum-openvswitch-agent.upstart
%{_initrddir}/quantum-ovs-cleanup
%{_datadir}/quantum/quantum-ovs-cleanup.upstart
%{python_sitelib}/quantum/plugins/openvswitch
%{_datarootdir}/quantum/rootwrap/openvswitch-plugin.filters
%dir %{_sysconfdir}/quantum/plugins/openvswitch
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/plugins/openvswitch/*.ini


%files -n openstack-quantum-plumgrid
%doc LICENSE
%doc quantum/plugins/plumgrid/README
%{python_sitelib}/quantum/plugins/plumgrid
%dir %{_sysconfdir}/quantum/plugins/plumgrid
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/plugins/plumgrid/*.ini


%files -n openstack-quantum-ryu
%doc LICENSE
%doc quantum/plugins/ryu/README
%{_bindir}/quantum-ryu-agent
%{_initrddir}/quantum-ryu-agent
%{_datadir}/quantum/quantum-ryu-agent.upstart
%{python_sitelib}/quantum/plugins/ryu
%{_datarootdir}/quantum/rootwrap/ryu-plugin.filters
%dir %{_sysconfdir}/quantum/plugins/ryu
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/plugins/ryu/*.ini


%files -n openstack-quantum-nec
%doc LICENSE
%doc quantum/plugins/nec/README
%{_bindir}/quantum-nec-agent
%{_initrddir}/quantum-nec-agent
%{_datadir}/quantum/quantum-nec-agent.upstart
%{python_sitelib}/quantum/plugins/nec
%{_datarootdir}/quantum/rootwrap/nec-plugin.filters
%dir %{_sysconfdir}/quantum/plugins/nec
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/plugins/nec/*.ini


%files -n openstack-quantum-metaplugin
%doc LICENSE
%doc quantum/plugins/metaplugin/README
%{python_sitelib}/quantum/plugins/metaplugin
%dir %{_sysconfdir}/quantum/plugins/metaplugin
%config(noreplace) %attr(0640, root, quantum) %{_sysconfdir}/quantum/plugins/metaplugin/*.ini


%changelog
* Tue May 22 2013 Gary Kotton <gkotton@redhat.com> - 2013.1.1-3
- Updates to work with namespaces
- Fix kill-metadata rootwrap filter

* Mon May 13 2013 Gary Kotton <gkotton@redhat.com> - 2013.1.1-2
- Update to grizzly stable release 2013.1.1
- Update install scripts to configure security groups
- Update install scripts to remove virtual interface configurations

* Mon Apr 29 2013 Pádraig Brady <pbrady@redhat.com> 2013.1-3
- Fix quantum-ovs-cleanup.init to reference the correct config files

* Wed Apr  4 2013 Gary Kotton <gkotton@redhat.com> - 2013.1-1
- Update to grizzly release

* Wed Apr  4 2013 Gary Kotton <gkotton@redhat.com> - 2013.1-0.7.rc3
- Update to grizzly rc3
- Update rootwrap (bug 947793)
- Update l3-agent-setup to support qpid (bug 947532)
- Update l3-agent-setup to support metadata-agent credentials
- Update keystone authentication details (bug 947776)

* Tue Mar 26 2013 Terry Wilson <twilson@redhat.com> - 2013.1-0.6.rc2
- Update to grizzly rc2

* Tue Mar 12 2013 Pádraig Brady <P@draigBrady.Com> - 2013.1-0.5.g3
- Relax the dependency requirements on sqlalchemy

* Mon Feb 25 2013 Robert Kukura <rkukura@redhat.com> - 2013.1-0.4.g3
- Update to grizzly milestone 3
- Add brocade, hyperv, midonet, and plumgrid plugins as sub-packages
- Remove cisco files that were eliminated
- Add quantum-check-nvp-config
- Include patch for https://code.launchpad.net/bugs/1132889
- Require python-oslo-config
- Require compatible version of python-sqlalchemy
- Various spec file improvements

* Thu Feb 14 2013 Robert Kukura <rkukura@redhat.com> - 2013.1-0.3.g2
- Update to grizzly milestone 2
- Add quantum-db-manage, quantum-metadata-agent,
  quantum-ns-metadata-proxy, quantum-ovs-cleanup, and
  quantum-usage-audit executables
- Add systemd units for quantum-metadata-agent and quantum-ovs-cleanup
- Fix /etc/quantum/policy.json permissions (bug 877600)
- Require dnsmasq (bug 890041)
- Add the version info file
- Remove python-lxml dependency
- Add python-alembic dependency

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.1-0.2.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Martin Magr <mmagr@redhat.com> - 2012.2.1-1
- Added python-keystone requirement

* Wed Dec  5 2012 Robert Kukura <rkukura@redhat.com> - 2013.1-0.1.g1
- Update to grizzly milestone 1
- Require python-quantumclient >= 1:2.1.10
- Remove unneeded rpc control_exchange patch
- Add bigswitch plugin as sub-package
- Work around bigswitch conf file missing from setup.py

* Mon Dec  3 2012 Robert Kukura <rkukura@redhat.com> - 2012.2.1-1
- Update to folsom stable 2012.2.1
- Add upstream patch: Fix rpc control_exchange regression.
- Remove workaround for missing l3_agent.ini

* Thu Nov 01 2012 Alan Pevec <apevec@redhat.com> 2012.2-2
- l3_agent not disabling namespace use lp#1060559

* Fri Sep 28 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-1
- Update to folsom final
- Require python-quantumclient >= 1:2.1.1

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
