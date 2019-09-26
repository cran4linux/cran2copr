%global packname  GERGM
%global packver   0.13.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.0
Release:          1%{?dist}
Summary:          Estimation and Fit Diagnostics for Generalized ExponentialRandom Graph Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-slackr 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-plyr 
Requires:         R-parallel 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-slackr 
Requires:         R-CRAN-matrixcalc 

%description
Estimation and diagnosis of the convergence of Generalized Exponential
Random Graph Models via Gibbs sampling or Metropolis Hastings with
exponential down weighting.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
