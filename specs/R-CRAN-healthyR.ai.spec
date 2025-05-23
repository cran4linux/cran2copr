%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  healthyR.ai
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          The Machine Learning and AI Modeling Companion to 'healthyR'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-recipes >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-yardstick >= 0.0.8
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-h2o 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-CRAN-workflows 
BuildRequires:    R-CRAN-modeltime 
Requires:         R-CRAN-recipes >= 1.0.0
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-yardstick >= 0.0.8
Requires:         R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-h2o 
Requires:         R-stats 
Requires:         R-CRAN-dials 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-tune 
Requires:         R-CRAN-workflows 
Requires:         R-CRAN-modeltime 

%description
Hospital machine learning and ai data analysis workflow tools, modeling,
and automations. This library provides many useful tools to review common
administrative hospital data. Some of these include predicting length of
stay, and readmits. The aim is to provide a simple and consistent verb
framework that takes the guesswork out of everything.

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
