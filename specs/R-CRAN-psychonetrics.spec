%global packname  psychonetrics
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}
Summary:          Structural Equation Modeling and Confirmatory Network Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-VCA 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-crayon 
Requires:         R-methods 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-matrixcalc 
Requires:         R-Matrix 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-glasso 
Requires:         R-mgcv 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-VCA 
Requires:         R-CRAN-pbapply 
Requires:         R-parallel 
Requires:         R-CRAN-magrittr 

%description
Multi-group (dynamical) structural equation models in combination with
confirmatory network models from cross-sectional, time-series and panel
data. Allows for confirmatory testing and fit as well as exploratory model
search.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
