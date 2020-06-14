%global packname  glamlasso
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          2%{?dist}
Summary:          Penalization in Large Scale Generalized Linear Array Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.2

%description
Functions capable of performing efficient design matrix free penalized
estimation in large scale 2 and 3-dimensional generalized linear array
model framework. The generic glamlasso() function solves the penalized
maximum likelihood estimation (PMLE) problem in a pure generalized linear
array model (GLAM) as well as in a GLAM containing a non-tensor component.
Currently Lasso or Smoothly Clipped Absolute Deviation (SCAD) penalized
estimation is possible for the followings models: The Gaussian model with
identity link, the Binomial model with logit link, the Poisson model with
log link and the Gamma model with log link. Furthermore this package also
contains two functions that can be used to fit special cases of GLAMs, see
glamlassoRR() and glamlassoS(). The procedure underlying these functions
is based on the gdpg algorithm from Lund et al. (2017)
<doi:10.1080/10618600.2017.1279548>.

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
