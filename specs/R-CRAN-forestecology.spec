%global __brp_check_rpaths %{nil}
%global packname  forestecology
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Methods and Data for Forest Ecology Model Fitting and Assessment

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-CRAN-snakecase 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-yardstick 
BuildRequires:    R-CRAN-blockCV 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sfheaders 
Requires:         R-CRAN-snakecase 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-yardstick 
Requires:         R-CRAN-blockCV 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-patchwork 

%description
Code for fitting and assessing models for the growth of trees. In
particular for the Bayesian neighborhood competition linear regression
model of Allen (2020): methods for model fitting and generating
fitted/predicted values, evaluating the effect of competitor species
identity using permutation tests, and evaluating model performance using
spatial cross-validation.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
