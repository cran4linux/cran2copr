%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pdcor
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast and Light-Weight Partial Distance Correlation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dcov 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-Rfast2 
BuildRequires:    R-stats 
Requires:         R-CRAN-dcov 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-Rfast2 
Requires:         R-stats 

%description
Fast and memory-less computation of the partial distance correlation for
vectors and matrices. Permutation-based and asymptotic hypothesis testing
for zero partial distance correlation are also performed. References
include: Szekely G. J. and Rizzo M. L. (2014). "Partial distance
correlation with methods for dissimilarities". The Annals Statistics,
42(6): 2382--2412. <doi:10.1214/14-AOS1255>. Shen C., Panda S. and
Vogelstein J. T. (2022). "The Chi-Square Test of Distance Correlation".
Journal of Computational and Graphical Statistics, 31(1): 254--262.
<doi:10.1080/10618600.2021.1938585>. Szekely G. J. and Rizzo M. L. (2023).
"The Energy of Data and Distance Correlation". Chapman and Hall/CRC.
<ISBN:9781482242744>.

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
