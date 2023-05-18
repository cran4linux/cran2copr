%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stabiliser
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Stabilising Variable Selection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-bigstep 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-expss 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-lmerTest 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-bigstep 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-expss 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-lmerTest 

%description
A stable approach to variable selection through stability selection and
the use of a permutation-based objective stability threshold. Lima et al
(2021) <doi:10.1038/s41598-020-79317-8>, Meinshausen and Buhlmann (2010)
<doi:10.1111/j.1467-9868.2010.00740.x>.

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
