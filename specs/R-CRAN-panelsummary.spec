%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  panelsummary
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Publication-Ready Regression Tables with Panels

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods >= 4.1.3
BuildRequires:    R-CRAN-stringr >= 1.4.1
BuildRequires:    R-CRAN-kableExtra >= 1.3.4
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-rlang >= 1.0.6
BuildRequires:    R-CRAN-modelsummary >= 1.0.2
BuildRequires:    R-CRAN-fixest >= 0.10.4
Requires:         R-methods >= 4.1.3
Requires:         R-CRAN-stringr >= 1.4.1
Requires:         R-CRAN-kableExtra >= 1.3.4
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-modelsummary >= 1.0.2
Requires:         R-CRAN-fixest >= 0.10.4

%description
Create an automated regression table that is well-suited for models that
are estimated with multiple dependent variables. 'panelsummary' extends
'modelsummary' (Arel-Bundock, V. (2022) <doi:10.18637/jss.v103.i01>) by
allowing regression tables to be split into multiple sections with a
simple function call. Utilize familiar arguments such as fmt, estimate,
statistic, vcov, conf_level, stars, coef_map, coef_omit, coef_rename,
gof_map, and gof_omit from 'modelsummary' to clean the table, and
additionally, add a row for the mean of the dependent variable without
external manipulation.

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
