%define reldate 20090702
%define reltype C
# may be one of: C (current), R (release), S (stable)

Name: hpt
Version: 1.9.%{reldate}%{reltype}
Release: 1
Group: Applications/FTN
Summary: HPT - the Husky Project tosser
URL: http://husky.sf.net
License: GPL
Requires: fidoconf >= 1.9, smapi >= 2.5, areafix >= 1.9
Source: %{name}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
HPT is the FTN tosser from the Husky Project.

%prep
%setup -q -n %{name}

%build
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_prefix}/*