%define module hyperframe

Name:		python-%{module}
Version:	6.1.0
Release:	1
Summary:	HTTP/2 framing layer for Python
Group:		Development/Python
License:	MIT
URL:		https://github.com/python-hyper/hyperframe
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
This library contains the HTTP/2 framing code used in the hyper project.
It provides a pure-Python codebase that is capable of decoding a binary
stream into HTTP/2 frames.

This library is used directly by hyper and a number of other projects
to provide HTTP/2 frame decoding logic.

%files
%doc CONTRIBUTORS.rst README.rst
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}.dist-info
