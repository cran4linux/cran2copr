%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  appac
%global packver   4.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Atmospheric Pressure Peak Area Correction for Gas Chromatography with Standard Detectors

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-kza 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-strucchange 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-kza 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-strucchange 

%description
Corrects gas-chromatography peak areas for the influence of ambient air
pressure on standard detectors open to the ambient atmosphere, such as the
flame ionization detector, whose pressure sensitivity was characterised by
Bocek, Novak and Janak (1969) <doi:10.1016/S0021-9673(00)99223-9>. Unlike
the pressure compensation of Ayers and Clardy (1985)
<https://patents.google.com/patent/US4512181A>, which is combined with a
calibration and valid only for a single calibration period of a few days,
per-cylinder peak areas are decomposed by principal components into a
pressure-correlated component and per-peak drift; a common
pressure-sensitivity coefficient (kappa) is estimated with a
heavy-tail-robust fit on a drift-reduced signal, and slow drift plus a
daily factor are removed. Returns the corrected areas together with a
chi-square goodness-of-fit diagnostic. Structural-break detection (package
'strucchange', Zeileis and others (2002) <doi:10.18637/jss.v007.i02>) is
provided for episode-level and variance breakpoint analysis.

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
