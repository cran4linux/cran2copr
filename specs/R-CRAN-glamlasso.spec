%global __brp_check_rpaths %{nil}
%global packname  glamlasso
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
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
Efficient design matrix free lasso penalized estimation in large scale 2
and 3-dimensional generalized linear array model framework. The procedure
is based on the gdpg algorithm from Lund et al. (2017)
<doi:10.1080/10618600.2017.1279548>. Currently Lasso or Smoothly Clipped
Absolute Deviation (SCAD) penalized estimation is possible for the
following models: The Gaussian model with identity link, the Binomial
model with logit link, the Poisson model with log link and the Gamma model
with log link. It is also possible to include a component in the model
with non-tensor design e.g an intercept. Also provided are functions,
glamlassoRR() and glamlassoS(), fitting special cases of GLAMs.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
