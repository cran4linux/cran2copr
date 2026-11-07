%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mzimp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Zero-Inflated Mixed Poisson Regression for Multivariate Count Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-VineCopula 
BuildRequires:    R-CRAN-codetools 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-pkgload 
BuildRequires:    R-CRAN-ps 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-VineCopula 
Requires:         R-CRAN-codetools 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-pkgload 
Requires:         R-CRAN-ps 
Requires:         R-CRAN-randtoolbox 

%description
Fits and selects zero-inflated mixed Poisson models for multivariate count
regression. Supports multiple mixing distributions and variance
specifications for flexible marginal modeling, while allowing dependence
in the structural-zero components and latent mixing intensities to be
modeled separately through copulas. The methodology is described in Nguyen
(2026) <doi:10.48550/arXiv.2608.12732>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
