%define _base vert.x 
%define _hash f880cb78b116f27c303021d2eaa8e6fd00c2850b

# human-readable/info tags
Name: %{_base}
Version: 3.4.1
Release: 1%{?dist}
Summary: Vert.x is a server-side Java environment that uses an asynchronous event-driven model.
Packager: Fernando Jordan Silva <fjordan@aubay.es>
Group: Development/Libraries
License: MIT License
URL: http://vertx.io/
# functional tags
Source0: http://dl.bintray.com/vertx/downloads/%{_base}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-tmp
BuildRequires: tar
BuildRequires: gzip

%define _prefix /opt

%description
Vert.x is a lightweight, high performance application platform for the JVM that's designed for modern mobile, web, and enterprise applications.

%pre
getent group vertx >/dev/null || groupadd -r vertx
getent passwd vertx >/dev/null || useradd -r -g vertx -s /sbin/nologin -c "Vert.x service account" vertx
exit 0

%prep
rm -rf $RPM_SOURCE_DIR/%{_base}-%{version}
pushd $RPM_SOURCE_DIR 
[ -f %{_hash}?filename=%{_base}-%{version}.tar.gz ] && mv %{_hash}?filename=%{_base}-%{version}.tar.gz %{_base}-%{version}.tar.gz
popd 

%build 
pushd $RPM_SOURCE_DIR 
tar zxvf %{_base}-%{version}.tar.gz 
ln -s vertx/ %{_base}-%{version}
popd 

%install 
rm -rf $RPM_BUILD_ROOT 
mkdir -p $RPM_BUILD_ROOT%{_prefix}/%{_base}
cp -Rp $RPM_SOURCE_DIR/%{_base}-%{version}/* $RPM_BUILD_ROOT%{_prefix}/%{_base}

%post
[ -d /usr/local/bin ] || mkdir -p /usr/local/bin
ln -s %{_prefix}/%{_base}/bin/vertx /usr/local/bin/vertx
echo "[INFO] Done"

%preun
if [ $1 == 0 ]; then
   rm -Rf /usr/bin/vertx
   echo "[INFO] Done"
fi

%clean 
rm -rf $RPM_BUILD_ROOT 
rm -rf $RPM_SOURCE_DIR/%{_base}-%{version} 

%files 
%defattr(755,vertx,vertx,-) 
%{_prefix}/%{_base} 

%changelog 
* Fri Apr 14 2017 Mark Hudson <markhu@gmail.com>
- handle changed directory structure in newer tarballs
* Thu Jan 09 2014 Fernando Jordan <fjordansilva@gmail.com>
- Added vertx user and group to the system.
* Wed Dec 11 2013 Fernando Jordan <fjordansilva@gmail.com>
- Updated to Vert.x version 2.1M2
* Fri Nov 29 2013 Fernando Jordan <fjordansilva@gmail.com> 
- Initial version
