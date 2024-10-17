%define module	hyperframe

Name:		python-%{module}
Version:	6.0.1
Release:	4
Summary:	HTTP/2 framing layer for Python
Group:		Development/Python
License:	MIT
URL:		https://hyper.rtfd.org/
Source0:	https://pypi.io/packages/source/h/hyperframe/%{module}-%{version}.tar.gz

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}

BuildArch:	noarch

%description
This library contains the HTTP/2 framing code used in the hyper project.
It provides a pure-Python codebase that is capable of decoding a binary
stream into HTTP/2 frames.

This library is used directly by hyper and a number of other projects
to provide HTTP/2 frame decoding logic.

%files
%doc CONTRIBUTORS.rst LICENSE README.rst
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}-py%{python_version}.egg-info/

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py_build

%install
%py_install
