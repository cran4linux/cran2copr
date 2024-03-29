%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clintools
%global packver   0.9.10.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.10.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Clinical Research

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival >= 3.4.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-nlme >= 3.1.160
BuildRequires:    R-CRAN-stringi >= 1.7.8
BuildRequires:    R-CRAN-xml2 >= 1.3.2
BuildRequires:    R-CRAN-scales >= 1.2.1
BuildRequires:    R-CRAN-pROC >= 1.18.0
BuildRequires:    R-CRAN-lme4 >= 1.1.27.1
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-irr >= 0.84.1
BuildRequires:    R-CRAN-signal >= 0.7.6
BuildRequires:    R-CRAN-pander >= 0.6.5
BuildRequires:    R-CRAN-parameters >= 0.19.0
Requires:         R-CRAN-survival >= 3.4.0
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-nlme >= 3.1.160
Requires:         R-CRAN-stringi >= 1.7.8
Requires:         R-CRAN-xml2 >= 1.3.2
Requires:         R-CRAN-scales >= 1.2.1
Requires:         R-CRAN-pROC >= 1.18.0
Requires:         R-CRAN-lme4 >= 1.1.27.1
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-irr >= 0.84.1
Requires:         R-CRAN-signal >= 0.7.6
Requires:         R-CRAN-pander >= 0.6.5
Requires:         R-CRAN-parameters >= 0.19.0

%description
Every research team have their own script for data management, statistics
and most importantly hemodynamic indices. The purpose is to standardize
scripts utilized in clinical research. The hemodynamic indices can be used
in a long-format dataframe, and add both periods of interest
(trigger-periods), and delete artifacts with deleter-files. Transfer
function analysis (Claassen et al. (2016) <doi:10.1177/0271678X15626425>)
and Mx (Czosnyka et al. (1996) <doi:10.1161/01.str.27.10.1829>) can be
calculated using this package.

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
