%global __brp_check_rpaths %{nil}
%global packname  SlidingWindows
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Time Series Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-DCCA 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-nonlinearTseries 
BuildRequires:    R-CRAN-TSEntropies 
Requires:         R-stats 
Requires:         R-CRAN-DCCA 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-nonlinearTseries 
Requires:         R-CRAN-TSEntropies 

%description
A collection of functions to perform Detrended Fluctuation Analysis (DFA
exponent), GUEDES et al. (2019) <doi:10.1016/j.physa.2019.04.132> ,
Detrended cross-correlation coefficient (RHODCCA), GUEDES & ZEBENDE (2019)
<doi:10.1016/j.physa.2019.121286>, DMCA cross-correlation coefficient and
Detrended multiple cross-correlation coefficient (DMC), GUEDES &
SILVA-FILHO & ZEBENDE (2018) <doi:10.1016/j.physa.2021.125990>, both with
sliding windows approach.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
