%global packname  DDPGPSurv
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          DDP-GP Survival Analysis

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-MASS 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-mc2d 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-MASS 
Requires:         R-survival 
Requires:         R-CRAN-mc2d 
Requires:         R-CRAN-mvnfast 

%description
A nonparametric Bayesian approach to survival analysis. The functions
perform inference via MCMC simulations from the posterior distributions
for a Dependent Dirichlet Process-Gaussian Process prior. To maximize
computational efficiency, some of the computations are performed in
'Rcpp'.

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
%{rlibdir}/%{packname}/libs
