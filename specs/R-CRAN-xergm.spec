%global packname  xergm
%global packver   1.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.3
Release:          1%{?dist}
Summary:          Extensions of Exponential Random Graph Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-btergm >= 1.9.3
BuildRequires:    R-CRAN-xergm.common >= 1.7.7
BuildRequires:    R-CRAN-tnam >= 1.6.5
BuildRequires:    R-CRAN-rem >= 1.2.8
BuildRequires:    R-CRAN-GERGM >= 0.13.0
BuildRequires:    R-utils 
Requires:         R-CRAN-btergm >= 1.9.3
Requires:         R-CRAN-xergm.common >= 1.7.7
Requires:         R-CRAN-tnam >= 1.6.5
Requires:         R-CRAN-rem >= 1.2.8
Requires:         R-CRAN-GERGM >= 0.13.0
Requires:         R-utils 

%description
Extensions of Exponential Random Graph Models (ERGM): Temporal Exponential
Random Graph Models (TERGM), Generalized Exponential Random Graph Models
(GERGM), Temporal Network Autocorrelation Models (TNAM), and Relational
Event Models (REM). This package acts as a meta-package for several
sub-packages on which it depends.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
