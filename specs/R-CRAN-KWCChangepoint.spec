%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KWCChangepoint
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Changepoint Detection for Functional and Multivariate Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-ddalpha 
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-ddalpha 
Requires:         R-CRAN-fda.usc 
Requires:         R-CRAN-tibble 

%description
Detect and test for changes in covariance structures of functional data,
as well as changepoint detection for multivariate data more generally.
Method for detecting non-stationarity in resting state functional Magnetic
Resonance Imaging (fMRI) scans as seen in Ramsay, K., & Chenouri, S.
(2025) <doi:10.1080/10485252.2025.2503891> is implemented in
fmri_changepoints(). Also includes depth- and rank-based implementation of
the wild binary segmentation algorithm for detecting multiple changepoints
in multivariate data.

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
