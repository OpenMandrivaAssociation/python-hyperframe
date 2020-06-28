%define module	hyperframe

Name:		python-%{module}
Version:	5.2.0
Release:	%mkrel 3
Summary:	HTTP/2 framing layer for Python
Group:		Development/Python
License:	MIT
URL:		http://hyper.rtfd.org/
Source0:	https://pypi.io/packages/source/h/hyperframe/%{module}-%{version}.tar.gz
BuildArch:	noarch

%description
This library contains the HTTP/2 framing code used in the hyper project.
It provides a pure-Python codebase that is capable of decoding a binary
stream into HTTP/2 frames.

This library is used directly by hyper and a number of other projects
to provide HTTP/2 frame decoding logic.

%package -n	python3-%{module}
Summary:	HTTP/2 framing layer for Python 3
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}

%description -n	python3-%{module}
This library contains the HTTP/2 framing code used in the hyper project.
It provides a pure-Python codebase that is capable of decoding a binary
stream into HTTP/2 frames.

This library is used directly by hyper and a number of other projects
to provide HTTP/2 frame decoding logic.

This is the Python 3 version of the package.

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%doc CONTRIBUTORS.rst HISTORY.rst LICENSE README.rst
%{python3_sitelib}/%{module}/
%{python3_sitelib}/%{module}-%{version}-py%{python3_version}.egg-info/
