%global __brp_check_rpaths %{nil}
%global packname  magicLamp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          'WeMo Switch' Smart Plug Utilities

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 1.3.4
BuildRequires:    R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-tibble >= 1.3.4
Requires:         R-CRAN-httr >= 1.3.1

%description
Set of utility functions to interact with 'WeMo Switch', a smart plug that
can be remotely controlled via wifi. The provided functions make it
possible to turn one or more 'WeMo Switch' plugs on and off in a
scriptable fashion. More information about 'WeMo Switch' can be found at
<http://www.belkin.com/us/p/P-F7C027/>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
