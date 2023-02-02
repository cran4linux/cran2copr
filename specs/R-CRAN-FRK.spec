%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FRK
%global packver   2.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Fixed Rank Kriging

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Hmisc >= 4.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-CRAN-sparseinv 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Hmisc >= 4.1
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spacetime 
Requires:         R-CRAN-sparseinv 
Requires:         R-CRAN-statmod 
Requires:         R-stats 
Requires:         R-CRAN-TMB 
Requires:         R-utils 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 

%description
A tool for spatial/spatio-temporal modelling and prediction with large
datasets. The approach models the field, and hence the covariance
function, using a set of basis functions. This fixed-rank basis-function
representation facilitates the modelling of big data, and the method
naturally allows for non-stationary, anisotropic covariance functions.
Discretisation of the spatial domain into so-called basic areal units
(BAUs) facilitates the use of observations with varying support (i.e.,
both point-referenced and areal supports, potentially simultaneously), and
prediction over arbitrary user-specified regions. `FRK` also supports
inference over various manifolds, including the 2D plane and 3D sphere,
and it provides helper functions to model, fit, predict, and plot with
relative ease. Version 2.0.0 and above also supports the modelling of
non-Gaussian data (e.g., Poisson, binomial, negative-binomial, gamma, and
inverse-Gaussian) by employing a generalised linear mixed model (GLMM)
framework.  Zammit-Mangion and Cressie <doi:10.18637/jss.v098.i04>
describe `FRK` in a Gaussian setting, and detail its use of basis
functions and BAUs, while Sainsbury-Dale et al. <arXiv:2110.02507>
describe `FRK` in a non-Gaussian setting; two vignettes are available that
summarise these papers and provide additional examples.

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
