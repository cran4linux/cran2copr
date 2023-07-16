%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gtsummary
%global packver   1.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Presentation-Ready Data Summary and Analytic Result Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-cli >= 3.1.1
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-knitr >= 1.37
BuildRequires:    R-CRAN-broom.helpers >= 1.13.0
BuildRequires:    R-CRAN-tidyr >= 1.1.4
BuildRequires:    R-CRAN-dplyr >= 1.1.1
BuildRequires:    R-CRAN-rlang >= 1.0.3
BuildRequires:    R-CRAN-broom >= 1.0.1
BuildRequires:    R-CRAN-lifecycle >= 1.0.1
BuildRequires:    R-CRAN-purrr >= 1.0.1
BuildRequires:    R-CRAN-forcats >= 1.0.0
BuildRequires:    R-CRAN-gt >= 0.9.0
BuildRequires:    R-CRAN-vctrs >= 0.5.2
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-cli >= 3.1.1
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-knitr >= 1.37
Requires:         R-CRAN-broom.helpers >= 1.13.0
Requires:         R-CRAN-tidyr >= 1.1.4
Requires:         R-CRAN-dplyr >= 1.1.1
Requires:         R-CRAN-rlang >= 1.0.3
Requires:         R-CRAN-broom >= 1.0.1
Requires:         R-CRAN-lifecycle >= 1.0.1
Requires:         R-CRAN-purrr >= 1.0.1
Requires:         R-CRAN-forcats >= 1.0.0
Requires:         R-CRAN-gt >= 0.9.0
Requires:         R-CRAN-vctrs >= 0.5.2

%description
Creates presentation-ready tables summarizing data sets, regression
models, and more. The code to create the tables is concise and highly
customizable. Data frames can be summarized with any function, e.g.
mean(), median(), even user-written functions. Regression models are
summarized and include the reference rows for categorical variables.
Common regression models, such as logistic regression and Cox proportional
hazards regression, are automatically identified and the tables are
pre-filled with appropriate column headers.

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
