%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fAssets
%global packver   4023.85
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4023.85
Release:          1%{?dist}%{?buildtag}
Summary:          Rmetrics - Analysing and Modelling Financial Assets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-fMultivar 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-ecodist 
BuildRequires:    R-CRAN-mvnormtest 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-fMultivar 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-ecodist 
Requires:         R-CRAN-mvnormtest 
Requires:         R-CRAN-energy 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
A collection of functions to manage, to investigate and to analyze data
sets of financial assets from different points of view.

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
