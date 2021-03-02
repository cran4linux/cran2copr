%global packname  RcmdrPlugin.UCA
%global packver   4.3-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          UCA Rcmdr Plug-in

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 1.6
BuildRequires:    R-CRAN-qicharts2 
BuildRequires:    R-CRAN-randtests 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-tseries 
Requires:         R-CRAN-Rcmdr >= 1.6
Requires:         R-CRAN-qicharts2 
Requires:         R-CRAN-randtests 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-tseries 

%description
Some extensions to Rcmdr (R Commander), randomness test, variance test for
one normal sample and predictions using active model, made by R-UCA
project and used in teaching statistics at University of Cadiz (UCA).

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
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
