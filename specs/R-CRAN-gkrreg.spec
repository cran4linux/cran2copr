%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gkrreg
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Kernel Robust Regression (GKRReg)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-sm 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-sm 

%description
Implements the Gaussian Kernel Robust Regression (GKRReg / GKRR) method
proposed by De Carvalho, Lima Neto and Ferreira (2017)
<doi:10.1016/j.neucom.2016.12.035>. The method re-weights observations
iteratively using the Gaussian kernel so that poorly-fitted observations
(outliers, leverage points) receive small weights, yielding resistance to
Y-space outliers, X-space outliers and leverage points. Convergence is
guaranteed by Propositions 4.1 and 4.2 of the original paper. Three
estimators for the kernel width hyper-parameter are provided (S1: Caputo,
S2: pairwise median, S3: residual variance). Inference is provided via an
analytic sandwich variance estimator (default) or via bootstrap
(percentile, normal and BCa intervals with p-values) through gkrr_boot().
Six real datasets from the robust regression literature are included to
facilitate reproducible comparisons.

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
