%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  modernBoot
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Modern Resampling Methods: Bootstraps, Wild, Block, Permutation, and Selection Guidance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
Requires:         R-stats 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 

%description
Implements modern resampling and permutation methods for robust
statistical inference without restrictive parametric assumptions. Provides
bias-corrected and accelerated (BCa) bootstrap (Efron and Tibshirani
(1993) <doi:10.1201/9780429246593>), wild bootstrap for heteroscedastic
regression (Liu (1988) <doi:10.1214/aos/1176351062>, Davidson and
Flachaire (2008) <doi:10.1016/j.jeconom.2008.08.003>), block bootstrap for
time series (Politis and Romano (1994)
<doi:10.1080/01621459.1994.10476870>), and permutation-based multiple
testing correction (Westfall and Young (1993) <ISBN:0-471-55761-7>).
Methods handle non-normal data, heteroscedasticity, time series
correlation, and multiple comparisons.

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
