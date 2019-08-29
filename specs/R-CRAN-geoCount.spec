%global packname  geoCount
%global packver   1.150120
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.150120
Release:          1%{?dist}
Summary:          Analysis and Modeling for Geostatistical Count Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
Requires:         gsl
BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildRequires:    R-CRAN-Rcpp >= 0.9.4
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.9.4

%description
This package provides a variety of functions to analyze and model
geostatistical count data with generalized linear spatial models,
including 1) simulate and visualize the data; 2) posterior sampling with
robust MCMC algorithms (in serial or parallel way); 3) perform prediction
for unsampled locations; 4) conduct Bayesian model checking procedure to
evaluate the goodness of fitting; 5) conduct transformed residual checking
procedure. In the package, seamlessly embedded C++ programs and parallel
computing techniques are implemented to speed up the computing processes.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
