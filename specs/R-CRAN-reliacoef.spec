%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reliacoef
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Unidimensional and Multidimensional Reliability Coefficients

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-stats 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-matrixcalc 
Requires:         R-stats 

%description
Calculates and compares various reliability coefficients for
unidimensional and multidimensional scales. Supported unidimensional
estimators include coefficient alpha, congeneric reliability, the
Gilmer-Feldt coefficient, Feldt's classical congeneric reliability,
Hancock's H, Heise-Bohrnstedt's omega, Kaiser-Caffrey's alpha, and Ten
Berge and Zegers' mu series. Multidimensional estimators include
stratified alpha, maximal reliability, correlated factors reliability,
second-order factor reliability, and bifactor reliability. See Cho (2021)
<doi:10.1007/s11336-021-09801-1>, Cho (2024) <doi:10.1037/met0000475>, Cho
(2025) <doi:10.1037/met0000525>.

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
