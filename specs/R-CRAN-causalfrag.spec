%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  causalfrag
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cross-Framework Sensitivity Analysis with an OLS Crosswalk

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
Runs, classifies, interprets and reports sensitivity analyses for
unmeasured confounding across the partial R-squared robustness value
approach (Cinelli and Hazlett, 2020, <doi:10.1111/rssb.12348>), E-values
(VanderWeele and Ding, 2017, <doi:10.7326/M16-2607>), and the impact
threshold for a confounding variable and robustness of inference to
replacement (Frank, 2000, <doi:10.1177/0049124100029002001>; Frank,
Maroulis, Duong and Kelcey, 2013, <doi:10.3102/0162373713493129>). An
ordinary least squares crosswalk reports the robustness values, impact
threshold and replacement percentage computed from the focal t statistic
and residual degrees of freedom, makes explicit that their agreement is
largely fixed by that shared input, and flags the boundary band in which
they disagree. Template-based plain-language reports are included, with
optional integration with the 'confoundvis' package for plots.

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
