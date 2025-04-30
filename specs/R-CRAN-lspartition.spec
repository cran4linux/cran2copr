%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lspartition
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Estimation and Inference Procedures using Partitioning-Based Least Squares Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-dplyr 

%description
Tools for statistical analysis using partitioning-based least squares
regression as described in Cattaneo, Farrell and Feng (2020a,
<doi:10.48550/arXiv.1804.04916>) and Cattaneo, Farrell and Feng (2020b,
<doi:10.48550/arXiv.1906.00202>): lsprobust() for nonparametric point
estimation of regression functions and their derivatives and for robust
bias-corrected (pointwise and uniform) inference; lspkselect() for
data-driven selection of the IMSE-optimal number of knots;
lsprobust.plot() for regression plots with robust confidence intervals and
confidence bands; lsplincom() for estimation and inference for linear
combinations of regression functions from different groups.

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
