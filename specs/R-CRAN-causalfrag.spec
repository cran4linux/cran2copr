%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  causalfrag
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cross-Framework Causal Fragility Index

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.4.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-glue >= 1.6.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-cli >= 3.4.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-glue >= 1.6.0
Requires:         R-CRAN-rlang >= 1.0.0

%description
Provides a unified workflow for running, classifying, visualizing, and
interpreting sensitivity analyses for unmeasured confounding across
multiple causal frameworks. Introduces the Causal Fragility Index (CFI), a
single 0-100 composite score that integrates evidence from the partial
R-squared robustness value approach (Cinelli and Hazlett, 2020,
<doi:10.1111/rssb.12348>), E-value metrics (VanderWeele and Ding, 2017,
<doi:10.7326/M16-2607>), and the Impact Threshold for a Confounding
Variable (Frank, 2000, <doi:10.1177/0049124100029002001>) into one
interpretable measure of robustness. The package also provides
template-based plain-language narrative interpretation and
publication-ready reporting, with optional integration with the
'confoundvis' package for sensitivity plots.

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
