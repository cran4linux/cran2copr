%global packname  simexaft
%global packver   1.0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7.1
Release:          1%{?dist}
Summary:          simexaft

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-survival 
Requires:         R-CRAN-mvtnorm 
Requires:         R-survival 

%description
Implement of the Simulation-Extrapolation (SIMEX) algorithm for the
accelerated failure time (AFT) with covariates subject to measurement
error.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
