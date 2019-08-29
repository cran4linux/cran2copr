%global packname  blavaan
%global packver   0.3-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}
Summary:          Bayesian Latent Variable Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-rstan >= 2.19.2
BuildRequires:    R-CRAN-StanHeaders >= 2.18.1
BuildRequires:    R-CRAN-loo >= 2.0
BuildRequires:    R-CRAN-BH >= 1.69.0
BuildRequires:    R-CRAN-rstantools >= 1.5.0
BuildRequires:    R-CRAN-lavaan >= 0.6.4
BuildRequires:    R-CRAN-nonnest2 >= 0.5.2
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-mnormt 
Requires:         R-CRAN-rstan >= 2.19.2
Requires:         R-CRAN-loo >= 2.0
Requires:         R-CRAN-rstantools >= 1.5.0
Requires:         R-CRAN-lavaan >= 0.6.4
Requires:         R-CRAN-nonnest2 >= 0.5.2
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-mnormt 

%description
Fit a variety of Bayesian latent variable models, including confirmatory
factor analysis, structural equation models, and latent growth curve
models.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/stanfuns
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
