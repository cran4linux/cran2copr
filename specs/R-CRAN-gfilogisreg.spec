%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gfilogisreg
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Fiducial Inference for Binary Logistic Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-spatstat >= 2.0.0
BuildRequires:    R-CRAN-rcdd 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-EigenR 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-roptim 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-spatstat >= 2.0.0
Requires:         R-CRAN-rcdd 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-EigenR 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 

%description
Fiducial framework for the logistic regression model. The fiducial
distribution of the parameters of the logistic regression is simulated,
allowing to perform statistical inference on any parameter of interest.
The algorithm is taken from Jessi Cisewski's PhD thesis: Jessi Cisewski
(2012), "Generalized fiducial inference for mixed linear models".

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
