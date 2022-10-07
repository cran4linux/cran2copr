%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CSCNet
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting and Tuning Regularized Cause-Specific Cox Models with Elastic-Net Penalty

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0.92
BuildRequires:    R-CRAN-glmnet >= 4.1.4
BuildRequires:    R-CRAN-survival >= 3.3.1
BuildRequires:    R-CRAN-tibble >= 3.1.7
BuildRequires:    R-CRAN-riskRegression >= 2022.03.22
BuildRequires:    R-CRAN-prodlim >= 2019.11.13
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyverse >= 1.3.1
BuildRequires:    R-CRAN-future >= 1.26.1
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-furrr >= 0.3.0
BuildRequires:    R-CRAN-recipes >= 0.2.0
Requires:         R-CRAN-caret >= 6.0.92
Requires:         R-CRAN-glmnet >= 4.1.4
Requires:         R-CRAN-survival >= 3.3.1
Requires:         R-CRAN-tibble >= 3.1.7
Requires:         R-CRAN-riskRegression >= 2022.03.22
Requires:         R-CRAN-prodlim >= 2019.11.13
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyverse >= 1.3.1
Requires:         R-CRAN-future >= 1.26.1
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-furrr >= 0.3.0
Requires:         R-CRAN-recipes >= 0.2.0

%description
Flexible tools to fit, tune and obtain absolute risk predictions from
regularized cause-specific cox models with elastic-net penalty.

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
