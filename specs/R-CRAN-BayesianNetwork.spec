%global packname  BayesianNetwork
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Bayesian Network Modeling and Analysis

License:          Apache License | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-CRAN-heatmaply 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rintrojs 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinytest 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-bnlearn 
Requires:         R-CRAN-heatmaply 
Requires:         R-lattice 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rintrojs 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinytest 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-testthat 

%description
A 'Shiny' web application for creating interactive Bayesian Network
models, learning the structure and parameters of Bayesian networks, and
utilities for classic network analysis.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/bn
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/images
%doc %{rlibdir}/%{packname}/paper
%{rlibdir}/%{packname}/INDEX
