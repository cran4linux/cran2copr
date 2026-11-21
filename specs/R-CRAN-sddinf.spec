%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sddinf
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Direct Estimation and Inference for Spectral Differential Networks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
BuildRequires:    R-CRAN-clime 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-glassoFast 
BuildRequires:    R-CRAN-gsignal 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.11
Requires:         R-CRAN-clime 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-glassoFast 
Requires:         R-CRAN-gsignal 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixcalc 
Requires:         R-stats 

%description
Estimates and performs inference on the difference between two
high-dimensional inverse spectral densities, which describes how the
frequency-domain partial correlation network of a multivariate time series
changes across two conditions. The difference is estimated directly with
the lasso penalized D-trace loss of Yuan et al. (2017)
<doi:10.1093/biomet/asx049>, and de-biased confidence intervals and
p-values for individual edges are computed following Hellstern, Kim and
Shojaie (2026) <doi:10.48550/arXiv.2609.13609>. Also provides multivariate
spectral density estimates based on Welch's method and simulated example
data.

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
