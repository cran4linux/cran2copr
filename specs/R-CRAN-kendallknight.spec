%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kendallknight
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Implementation of Kendall's Correlation Coefficient Computation

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cpp4r 
Requires:         R-stats 

%description
The computational complexity of the implemented algorithm for Kendall's
correlation is O(n log(n)), which is faster than the base R implementation
with a computational complexity of O(n^2). For small vectors (i.e., less
than 100 observations), the time difference is negligible. However, for
larger vectors, the speed difference can be substantial and the numerical
difference is minimal. The references are Knight (1966)
<doi:10.2307/2282833>, Abrevaya (1999)
<doi:10.1016/S0165-1765(98)00255-9>, Christensen (2005)
<doi:10.1007/BF02736122> and Emara (2024) <https://learningcpp.org/>. This
implementation is described in Vargas Sepulveda (2025)
<doi:10.1371/journal.pone.0326090>.

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
