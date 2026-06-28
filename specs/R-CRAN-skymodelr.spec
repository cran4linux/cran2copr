%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  skymodelr
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Generates and Samples Realistic Terrestrial Atmospheres

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-rayimage >= 0.24.1
BuildRequires:    R-CRAN-rayvertex >= 0.14.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-swephR 
BuildRequires:    R-CRAN-RcppThread 
BuildRequires:    R-CRAN-libimath 
BuildRequires:    R-CRAN-libopenexr 
Requires:         R-CRAN-rayimage >= 0.24.1
Requires:         R-CRAN-rayvertex >= 0.14.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-swephR 

%description
Generates physically based sky environment maps and radiance samples using
the spectral Hosek-Wilkie and Prague atmosphere models. Functions write
high-dynamic-range 'OpenEXR' domes in latitude-longitude projections,
compute per-direction RGB or 55-channel values, and optionally composite
time-accurate star fields and moon phases. Features include automatic sun
and moon positioning from date, time and location, support for sea-level
and high-altitude observers, wide-spectrum coefficients, and multithreaded
C++ acceleration for fast, high-resolution output. For model details, see
Hosek and Wilkie (2012) <doi:10.1145/2185520.2185591>, Hosek and Wilkie
(2013) <doi:10.1109/MCG.2013.18>, Wilkie et al. (2021)
<doi:10.1145/3450626.3459758>, and Vevoda et al. (2022)
<doi:10.1111/cgf.14677>.

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
