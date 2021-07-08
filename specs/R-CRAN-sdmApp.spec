%global __brp_check_rpaths %{nil}
%global packname  sdmApp
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          A User-Friendly Application for Species Distribution Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.6.7
BuildRequires:    R-CRAN-sp >= 1.2.0
BuildRequires:    R-CRAN-shiny >= 0.12.2
Requires:         R-CRAN-raster >= 2.6.7
Requires:         R-CRAN-sp >= 1.2.0
Requires:         R-CRAN-shiny >= 0.12.2

%description
A 'shiny' application that allows non-expert 'R' users to easily model
species distribution. It offers a reproducible work flow for species
distribution modeling into a single and user friendly environment.
'sdmApp' takes 'raster' data (in format supported by the 'raster package')
and species occurrence data (several format supported) as input argument.
It provides an interactive graphical user interface (GUI).

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
