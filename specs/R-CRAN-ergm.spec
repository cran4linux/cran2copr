%global packname  ergm
%global packver   3.10.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.10.4
Release:          1%{?dist}
Summary:          Fit, Simulate and Diagnose Exponential-Family Models forNetworks

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    openmpi-devel
Requires:         openmpi
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-MASS >= 7.3.51.4
BuildRequires:    R-CRAN-lpSolve >= 5.6.13
BuildRequires:    R-CRAN-statnet.common >= 4.3.0
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-Matrix >= 1.2.17
BuildRequires:    R-CRAN-network >= 1.15
BuildRequires:    R-CRAN-robustbase >= 0.93.5
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-coda >= 0.19.2
BuildRequires:    R-CRAN-trust >= 0.1.7
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
Requires:         R-MASS >= 7.3.51.4
Requires:         R-CRAN-lpSolve >= 5.6.13
Requires:         R-CRAN-statnet.common >= 4.3.0
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-Matrix >= 1.2.17
Requires:         R-CRAN-network >= 1.15
Requires:         R-CRAN-robustbase >= 0.93.5
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-coda >= 0.19.2
Requires:         R-CRAN-trust >= 0.1.7
Requires:         R-parallel 
Requires:         R-methods 

%description
An integrated set of tools to analyze and simulate networks based on
exponential-family random graph models (ERGMs). 'ergm' is a part of the
Statnet suite of packages for network analysis.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
