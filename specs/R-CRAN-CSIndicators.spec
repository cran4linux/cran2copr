%global packname  CSIndicators
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Climate Services' Indicators Based on Sub-Seasonal to Decadal Predictions

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-multiApply >= 2.1.1
BuildRequires:    R-CRAN-s2dv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ClimProjDiags 
Requires:         R-CRAN-multiApply >= 2.1.1
Requires:         R-CRAN-s2dv 
Requires:         R-stats 
Requires:         R-CRAN-ClimProjDiags 

%description
Set of generalised tools for the flexible computation of climate related
indicators defined by the user. Each method represents a specific
mathematical approach which is combined with the possibility to select an
arbitrary time period to define the indicator. This enables a wide range
of possibilities to tailor the most suitable indicator for each particular
climate service application (agriculture, food security, energy, water
management…). This package is intended for sub-seasonal, seasonal and
decadal climate predictions, but its methods are also applicable to other
time-scales, provided the dimensional structure of the input is
maintained. Additionally, the outputs of the functions in this package are
compatible with 'CSTools'. This package was developed in the context of
H2020 MED-GOLD (776467) and S2S4E (776787) projects. Lledó et al. (2019)
<doi:10.1016/j.renene.2019.04.135>.

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
