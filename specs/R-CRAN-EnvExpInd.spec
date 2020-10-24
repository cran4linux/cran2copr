%global packname  EnvExpInd
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Environmental Exposure on the Individual Level

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-zoo 

%description
Tools for the assessment of the environmental exposure. The package
provides three methods (nearest monitoring site, inverse distance weighted
as described in Li Wu (2017) <doi:10.1016/j.envint.2016.11.013>,and
ordinary kriging) to calculate the environmental exposure (e.g. air
pollution) on the individual level.

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
