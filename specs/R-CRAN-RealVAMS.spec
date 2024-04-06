%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RealVAMS
%global packver   0.4-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate VAM Fitting

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-numDeriv 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Fits a multivariate value-added model (VAM), see Broatch, Green, and Karl
(2018) <doi:10.32614/RJ-2018-033> and Broatch and Lohr (2012)
<doi:10.3102/1076998610396900>, with normally distributed test scores and
a binary outcome indicator. A pseudo-likelihood approach, Wolfinger (1993)
<doi:10.1080/00949659308811554>, is used for the estimation of this joint
generalized linear mixed model.  The inner loop of the pseudo-likelihood
routine (estimation of a linear mixed model) occurs in the framework of
the EM algorithm presented by Karl, Yang, and Lohr (2013)
<DOI:10.1016/j.csda.2012.10.004>. This material is based upon work
supported by the National Science Foundation under grants DRL-1336027 and
DRL-1336265.

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
