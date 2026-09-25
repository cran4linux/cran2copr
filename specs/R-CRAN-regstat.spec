%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  regstat
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Exact Test for a Change in Covariance (Dependence) Structure

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
Requires:         R-stats 

%description
An exact finite-sample test for whether two groups share a covariance
matrix, the omnibus form of the differential-network question. Under the
Gaussian null the likelihood-ratio statistic has a distribution given by
the real Jacobi ensemble that is free of the unknown common covariance, so
a single Monte-Carlo calibration at the identity serves every covariance
with no estimate of the nuisance covariance; this is the property that
survives the dimension barrier, where estimating the covariance is
hardest. The max-type high-dimensional test of Cai, Liu and Xia (2013)
<doi:10.1080/01621459.2012.758041> is provided for comparison. A pure-C
back-end does the numerics and also backs the 'Python' package 'regstat'.

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
