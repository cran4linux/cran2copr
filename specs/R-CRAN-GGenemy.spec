%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GGenemy
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Audit 'ggplot2' Visualizations for Accessibility and Best Practices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-colorspace 
Requires:         R-grDevices 

%description
Audits 'ggplot2' visualizations for accessibility issues, misleading
practices, and readability problems. Checks for color accessibility
concerns including colorblind-unfriendly palettes, misleading scale
manipulations such as truncated axes and dual y-axes, text readability
issues like small fonts and overlapping labels, and general accessibility
barriers. Provides comprehensive audit reports with actionable suggestions
for improvement. Color vision deficiency simulation uses methods from the
'colorspace' package Zeileis et al. (2020) <doi:10.18637/jss.v096.i01>.
Contrast calculations follow WCAG 2.1 guidelines (W3C 2018
<https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum>).

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
