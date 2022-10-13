%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cvms
%global packver   1.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Cross-Validation for Model Selection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.3
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-MuMIn >= 1.43.17
BuildRequires:    R-CRAN-pROC >= 1.16.0
BuildRequires:    R-CRAN-data.table >= 1.12
BuildRequires:    R-CRAN-lme4 >= 1.1.23
BuildRequires:    R-CRAN-tidyr >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-rearrr >= 0.3.0
BuildRequires:    R-CRAN-parameters >= 0.15.0
BuildRequires:    R-CRAN-recipes >= 0.1.13
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble >= 3.0.3
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-MuMIn >= 1.43.17
Requires:         R-CRAN-pROC >= 1.16.0
Requires:         R-CRAN-data.table >= 1.12
Requires:         R-CRAN-lme4 >= 1.1.23
Requires:         R-CRAN-tidyr >= 1.1.2
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-rearrr >= 0.3.0
Requires:         R-CRAN-parameters >= 0.15.0
Requires:         R-CRAN-recipes >= 0.1.13
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Cross-validate one or multiple regression and classification models and
get relevant evaluation metrics in a tidy format. Validate the best model
on a test set and compare it to a baseline evaluation. Alternatively,
evaluate predictions from an external model. Currently supports regression
and classification (binary and multiclass). Described in chp. 5 of
Jeyaraman, B. P., Olsen, L. R., & Wambugu M. (2019, ISBN: 9781838550134).

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
