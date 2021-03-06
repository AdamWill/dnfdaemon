%global pkg_ver 1.0

Name:           local-pkg
Version:        %{pkg_ver}
Release:        1%{?dist}
Summary:        bar test package for dnf-daemon testing (search key words : yum plugin )

License:        GPLv2+
URL:            https://github.com/timlau/yum-daemon
Source0:        source.tar.gz
BuildArch:      noarch

%description
bar test package for dnf-daemon testing

%prep
%setup -q -n source


%build
# Nothing to build

%install
# Nothing to install

%files
%doc README

%changelog
* Mon Mar 10 2014 Tim Lauridsen <timlau@fedoraproject.org>
- Initial RPM
