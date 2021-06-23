%global __brp_check_rpaths %{nil}
%global packname  seedr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hydro and Thermal Time Seed Germination Models in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.13
BuildRequires:    R-CRAN-binom >= 1.1
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table >= 1.13
Requires:         R-CRAN-binom >= 1.1
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Analysis of seed germination data using the physiological time modelling
approach. Includes functions to fit hydrotime and thermal-time models with
the traditional approaches of Bradford (1990) <doi:10.1104/pp.94.2.840>
and Garcia-Huidobro (1982) <doi:10.1093/jxb/33.2.288>. Allows to fit
models to grouped datasets, i.e. datasets containing multiple species,
seedlots or experiments.

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
