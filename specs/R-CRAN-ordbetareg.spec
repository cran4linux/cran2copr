%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ordbetareg
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Ordered Beta Regression Models with 'brms'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-brms >= 2.18.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-rstantools 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-brms >= 2.18.0
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-rstantools 

%description
Implements ordered beta regression models, which are for modeling
continuous variables with upper and lower bounds, such as survey sliders,
dose-response relationships and indexes. For more information, see Kubinec
(2023) <doi:10.31235/osf.io/2sx6y>. The package is a front-end to the R
package 'brms', which facilitates a range of regression specifications,
including hierarchical, dynamic and multivariate modeling.

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
