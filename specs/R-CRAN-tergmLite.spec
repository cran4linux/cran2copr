%global packname  tergmLite
%global packver   2.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.7
Release:          3%{?dist}
Summary:          Fast Simulation of Simple Temporal Exponential Random GraphModels

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-statnet.common >= 4.3.0
BuildRequires:    R-CRAN-tergm >= 3.6.1
BuildRequires:    R-CRAN-ergm >= 3.10.4
BuildRequires:    R-CRAN-network >= 1.16.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-statnet.common >= 4.3.0
Requires:         R-CRAN-tergm >= 3.6.1
Requires:         R-CRAN-ergm >= 3.10.4
Requires:         R-CRAN-network >= 1.16.0
Requires:         R-CRAN-Rcpp 

%description
Provides functions for the computationally efficient simulation of dynamic
networks estimated with the statistical framework of temporal exponential
random graph models, implemented in the 'tergm' package.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/EpiModelHIV.R
%doc %{rlibdir}/%{packname}/ergm_getmodel.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
