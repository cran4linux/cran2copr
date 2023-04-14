%global __brp_check_rpaths %{nil}
%global packname  iopsych
%global packver   0.90.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.90.1
Release:          3%{?dist}%{?buildtag}
Summary:          Methods for Industrial/Organizational Psychology

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm >= 1.0
BuildRequires:    R-CRAN-mco >= 1.0
BuildRequires:    R-stats >= 1.0
Requires:         R-CRAN-mvtnorm >= 1.0
Requires:         R-CRAN-mco >= 1.0
Requires:         R-stats >= 1.0

%description
Collection of functions for IO Psychologists.

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
