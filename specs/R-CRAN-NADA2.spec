%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NADA2
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Analysis for Censored Environmental Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-EnvStats >= 2.4
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-Kendall 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-NADA 
BuildRequires:    R-CRAN-perm 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-cenGAM 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-EnvStats >= 2.4
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-Kendall 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-NADA 
Requires:         R-CRAN-perm 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-cenGAM 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-coin 
Requires:         R-CRAN-survival 

%description
Contains methods described by Dennis Helsel in his book "Statistics for
Censored Environmental Data using Minitab and R" (2011) and courses and
videos at <https://practicalstats.com>. This package adds new functions to
the `NADA` Package.

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
