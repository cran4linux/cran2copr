%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FatTailsR
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Kiener Distributions and Fat Tails in Finance and Neuroscience

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-timeSeries 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-stats 

%description
Kiener distributions K1, K2, K3, K4 and K7 to characterize distributions
with left and right, symmetric or asymmetric fat tails in finance,
neuroscience and other disciplines. Two algorithms to estimate the
distribution parameters, quantiles, value-at-risk and expected shortfall.
IMPORTANT: Standardization has been changed in versions >= 2.0.0 to get sd
= 1 when kappa = Inf rather than 2*pi/sqrt(3) in versions <= 1.8.6. This
affects parameter g (other parameters stay unchanged). Do not update if
you need consistent comparisons with previous results for the g parameter.

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
