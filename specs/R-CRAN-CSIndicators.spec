%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CSIndicators
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Climate Services' Indicators Based on Sub-Seasonal to Decadal Predictions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-multiApply >= 2.1.1
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ClimProjDiags 
BuildRequires:    R-CRAN-CSTools 
BuildRequires:    R-CRAN-SPEI 
BuildRequires:    R-CRAN-lmom 
BuildRequires:    R-CRAN-lmomco 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-multiApply >= 2.1.1
Requires:         R-stats 
Requires:         R-CRAN-ClimProjDiags 
Requires:         R-CRAN-CSTools 
Requires:         R-CRAN-SPEI 
Requires:         R-CRAN-lmom 
Requires:         R-CRAN-lmomco 
Requires:         R-CRAN-zoo 

%description
Set of generalised tools for the flexible computation of climate related
indicators defined by the user. Each method represents a specific
mathematical approach which is combined with the possibility to select an
arbitrary time period to define the indicator. This enables a wide range
of possibilities to tailor the most suitable indicator for each particular
climate service application (agriculture, food security, energy, water
management, ...). This package is intended for sub-seasonal, seasonal and
decadal climate predictions, but its methods are also applicable to other
time-scales, provided the dimensional structure of the input is
maintained. Additionally, the outputs of the functions in this package are
compatible with 'CSTools'. This package is described in 'Pérez-Zanón et
al. (2023) <doi:10.1016/j.cliser.2023.100393>' and it was developed in the
context of 'H2020 MED-GOLD' (776467) and 'S2S4E' (776787) projects. See
'Lledó et al. (2019) <doi:10.1016/j.renene.2019.04.135>' and 'Chou et al.,
2023 <doi:10.1016/j.cliser.2023.100345>' for details.

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
