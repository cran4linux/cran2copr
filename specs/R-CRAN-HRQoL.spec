%global packname  HRQoL
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Health Related Quality of Life Analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fmsb 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-fmsb 
Requires:         R-CRAN-car 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-numDeriv 
Requires:         R-Matrix 

%description
Offers tools and modelling approaches for binomial data with
overdispersion, with particular interest in Health Related Quality of Life
(HRQoL) questionnaires regression analysis.

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
%{rlibdir}/%{packname}/INDEX
