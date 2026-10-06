%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ThesiStats
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tools for Quantitative Theses

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-semTools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-semTools 
Requires:         R-stats 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Provides helpers for the analyses that quantitative theses in the social
and behavioral sciences repeat: renaming and scoring items, recoding
Likert responses, cleaning sociodemographic variables written in Spanish
(age, academic term, degree and university), descriptive statistics,
univariate and multivariate normality checks, omega reliability from
ordinal confirmatory factor models, correlation matrices in table format,
and two-group or several-group comparisons with effect sizes.

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
