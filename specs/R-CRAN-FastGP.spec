%global __brp_check_rpaths %{nil}
%global packname  FastGP
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Efficiently Using Gaussian Processes with Rcpp and RcppEigen

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-rbenchmark 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-rbenchmark 
Requires:         R-stats 

%description
Contains Rcpp and RcppEigen implementations of matrix operations useful
for Gaussian process models, such as the inversion of a symmetric Toeplitz
matrix, sampling from multivariate normal distributions, evaluation of the
log-density of a multivariate normal vector, and Bayesian inference for
latent variable Gaussian process models with elliptical slice sampling
(Murray, Adams, and MacKay 2010).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
