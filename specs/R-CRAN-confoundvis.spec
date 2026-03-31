%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  confoundvis
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization Tools for Sensitivity Analysis of Unmeasured Confounding

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-rlang 
Requires:         R-graphics 
Requires:         R-stats 

%description
Provides visualization tools for sensitivity analysis to unmeasured
confounding in observational studies. Includes contour-based sensitivity
plots, robustness curves, and benchmark-oriented graphics that help
researchers assess how strong omitted confounding would need to be to
attenuate, invalidate, or reverse estimated effects. Supports
regression-based sensitivity analysis frameworks, including impact
threshold approaches (Frank, 2000, <doi:10.1177/0049124100029002001>),
partial R-squared methods (Cinelli and Hazlett, 2020,
<doi:10.1111/rssb.12348>), and E-value style metrics (VanderWeele and
Ding, 2017, <doi:10.7326/M16-2607>). Emphasizes clear, interpretable, and
publication-ready graphical summaries for transparent reporting of causal
sensitivity analyses across the social, behavioral, health, and
educational sciences.

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
