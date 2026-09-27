%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  drisdiagnostics
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Diagnostic Systems for Plant Nutrient Analysis (DRIS, MDRIS, PASS)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-rlang 

%description
Provides implementations of the Diagnosis and Recommendation Integrated
System (DRIS), the Modified DRIS (MDRIS), and the Plant Analysis with
Standardized Scores (PASS) approaches for nutrient diagnosis in crops.
These methods allow quantitative evaluation of nutrient imbalances using
ratio-based indices and standardized scores, supporting improved
fertilizer use efficiency and crop management decisions. The DRIS method
is described in Walworth, J.L. and Sumner, M.E. (1987)
<doi:10.1007/978-1-4612-4682-4_4>. The MDRIS approach is detailed in
Beverly, R.B. (1987) <doi:10.1080/01904168709363672>. The PASS method
combining DRIS and sufficiency ranges is presented in Baldock, J.O. and
Schulte, E.E. (1996) <doi:10.2134/agronj1996.00021962008800030015x>.

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
