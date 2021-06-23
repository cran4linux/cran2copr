%global __brp_check_rpaths %{nil}
%global packname  RcmdrPlugin.TeachStat
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Commander Plugin for Teaching Statistical Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 2.5.1
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-randtests 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-IndexNumR 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-distr 
BuildRequires:    R-CRAN-distrEx 
Requires:         R-CRAN-Rcmdr >= 2.5.1
Requires:         R-tcltk 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-randtests 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-IndexNumR 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-distr 
Requires:         R-CRAN-distrEx 

%description
R Commander plugin for teaching statistical methods. It adds a new menu
for making easier the teaching of the main concepts about the main
statistical methods.

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
