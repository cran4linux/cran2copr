%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  slxr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial-X (SLX) Models for Applied Researchers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-rlang 

%description
Tools for estimating, interpreting, and visualizing Spatial-X (SLX)
regression models. Provides a formula-based interface with first-class
support for variable-specific weights matrices, higher-order spatial lags,
temporally-lagged spatial variables (TSLS), and tidy effects decomposition
(direct, indirect, total). Designed to lower the barrier to SLX modeling
for applied researchers who already work with 'sf' and 'lm'-style
formulas. Methods follow Wimpy, Whitten, and Williams (2021)
<doi:10.1086/710089>.

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
