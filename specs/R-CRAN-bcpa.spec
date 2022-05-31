%global __brp_check_rpaths %{nil}
%global packname  bcpa
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Behavioral Change Point Analysis of Animal Movement

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-plyr 
Requires:         R-stats 

%description
The Behavioral Change Point Analysis (BCPA) is a method of identifying
hidden shifts in the underlying parameters of a time series, developed
specifically to be applied to animal movement data which is irregularly
sampled.  The method is based on: E. Gurarie, R. Andrews and K. Laidre A
novel method for identifying behavioural changes in animal movement data
(2009) Ecology Letters 12:5 395-408. A development version is on
<https://github.com/EliGurarie/bcpa>. NOTE: the BCPA method may be useful
for any univariate, irregularly sampled Gaussian time-series, but animal
movement analysts are encouraged to apply correlated velocity change point
analysis as implemented in the smoove package, as of this writing on
GitHub at <https://github.com/EliGurarie/smoove>. An example of a
univariate analysis is provided in the UnivariateBCPA vignette.

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
