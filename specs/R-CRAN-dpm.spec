%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dpm
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Panel Models Fit with Maximum Likelihood

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-jtools >= 2.0.1
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-panelr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-stats4 
Requires:         R-CRAN-jtools >= 2.0.1
Requires:         R-CRAN-lavaan 
Requires:         R-methods 
Requires:         R-CRAN-panelr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-Formula 
Requires:         R-stats4 

%description
Implements the dynamic panel models described by Allison, Williams, and
Moral-Benito (2017 <doi:10.1177/2378023117710578>) in R. This class of
models uses structural equation modeling to specify dynamic (lagged
dependent variable) models with fixed effects for panel data.
Additionally, models may have predictors that are only weakly exogenous,
i.e., are affected by prior values of the dependent variable. Options also
allow for random effects, dropping the lagged dependent variable, and a
number of other specification choices.

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
