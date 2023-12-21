%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  r2mlm
%global packver   0.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          R-Squared Measures for Multilevel Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.6.3
BuildRequires:    R-CRAN-nlme >= 3.1.14
BuildRequires:    R-CRAN-rockchalk >= 1.8.157
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-lme4 >= 1.1.23
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-rlang >= 0.4.6
Requires:         R-methods >= 3.6.3
Requires:         R-CRAN-nlme >= 3.1.14
Requires:         R-CRAN-rockchalk >= 1.8.157
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-lme4 >= 1.1.23
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-rlang >= 0.4.6

%description
Generates both total- and level-specific R-squared measures from Rights
and Sterba’s (2019) <doi:10.1037/met0000184> framework of R-squared
measures for multilevel models with random intercepts and/or slopes, which
is based on a complete decomposition of variance. Additionally generates
graphical representations of these R-squared measures to allow visualizing
and interpreting all measures in the framework together as an integrated
set. This framework subsumes 10 previously-developed R-squared measures
for multilevel models as special cases of 5 measures from the framework,
and it also includes several newly-developed measures. Measures in the
framework can be used to compute R-squared differences when comparing
multilevel models (following procedures in Rights & Sterba (2020)
<doi:10.1080/00273171.2019.1660605>). Bootstrapped confidence intervals
can also be calculated. To use the confidence interval functionality,
download bootmlm from <https://github.com/marklhc/bootmlm>.

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
