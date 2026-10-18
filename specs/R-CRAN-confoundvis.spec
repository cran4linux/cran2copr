%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  confoundvis
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Common Interface for Visualizing and Reporting Sensitivity Analyses for Unmeasured Confounding

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-rlang 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
A common interface to established sensitivity analyses for unmeasured
confounding in observational studies. Results of impact threshold and
robustness of inference to replacement analysis (Frank, 2000,
<doi:10.1177/0049124100029002001>; Frank et al., 2013,
<doi:10.3102/0162373713493129>), partial R-squared omitted-variable bias
analysis (Cinelli and Hazlett, 2020, <doi:10.1111/rssb.12348>), E-values
(VanderWeele and Ding, 2017, <doi:10.7326/M16-2607>), and Rosenbaum bounds
for matched pairs (Rosenbaum, 2002, <doi:10.1007/978-1-4757-3692-2>) are
stored in one object that keeps each framework's own parameter. Robustness
curves, summary tables, and plain-language reports are available for every
framework; two-parameter surfaces, the exact correlation contour, and
observed-covariate benchmarks are provided where the corresponding
framework defines them. Results can be computed from fitted models or
matched-pair differences, or converted from the 'sensemakr', 'konfound',
and 'EValue' packages, and agree with those packages.

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
