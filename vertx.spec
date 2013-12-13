%define _base vert.x 
%define _hash aeb7b36a15e67f3d15afaadb48bcf3b9819906c9

Name: %{_base} 
Version: 2.1M1 
Release: 1%{?dist} 
Summary: Vert.x is a server-side Java environment that uses an asynchronous event-driven model. 
Packager: Fernando Jordan Silva <fjordan@aubay.es> 
Group: Development/Libraries 
License: MIT License 
URL: http://vertx.io 
Source0: http://dl.bintray.com/vertx/downloads/%{_base}-%{version}.tar.gz 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-tmp 
BuildRequires: tar 
BuildRequires: gzip

%description 
Vert.x is a lightweight, high performance application platform for the JVM that's designed for modern mobile, web, and enterprise applications. 

%prep 
rm -rf $RPM_SOURCE_DIR/%{_base}-%{version}
rm -rf $RPM_SOURCE_DIR/%{_base}-%{version}.tar.gz
pushd $RPM_SOURCE_DIR 
[ -f %{_hash}?filename=%{_base}-%{version}.tar.gz ] && mv %{_hash}?filename=%{_base}-%{version}.tar.gz %{_base}-%{version}.tar.gz
popd 

%build 
pushd $RPM_SOURCE_DIR 
tar zxvf %{_base}-%{version}.tar.gz 
popd 

%install 
rm -rf $RPM_BUILD_ROOT 
mkdir -p $RPM_BUILD_ROOT%{_prefix}/%{_base}
cp -Rp $RPM_SOURCE_DIR/%{_base}-%{version}/* $RPM_BUILD_ROOT%{_prefix}/%{_base}

%post
cd /usr/bin
ln -s %{_prefix}/%{_base}/bin/vertx /usr/bin/vertx
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
%defattr(755,root,root,-) 
%{_prefix}/%{_base} 

%changelog 
* Fri Nov 29 2013 Fernando Jordan <fjordansilva@gmail.com> 
- Initial version
