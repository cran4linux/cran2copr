%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stepR
%global packver   2.1-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Multiscale Change-Point Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-lowpassFilter >= 1.0.0
BuildRequires:    R-CRAN-digest >= 0.6.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-R.cache >= 0.10.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
Requires:         R-CRAN-lowpassFilter >= 1.0.0
Requires:         R-CRAN-digest >= 0.6.10
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-R.cache >= 0.10.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 

%description
Allows fitting of step-functions to univariate serial data where neither
the number of jumps nor their positions is known by implementing the
multiscale regression estimators SMUCE, simulataneous multiscale
changepoint estimator, (K. Frick, A. Munk and H. Sieling, 2014)
<doi:10.1111/rssb.12047> and HSMUCE, heterogeneous SMUCE, (F. Pein, H.
Sieling and A. Munk, 2017) <doi:10.1111/rssb.12202>. In addition,
confidence intervals for the change-point locations and bands for the
unknown signal can be obtained.

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
