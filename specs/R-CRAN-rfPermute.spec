%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rfPermute
%global packver   2.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Permutation p-Values for Random Forest Importance Metrics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest >= 4.6
BuildRequires:    R-CRAN-ggplot2 >= 3.3
BuildRequires:    R-CRAN-tibble >= 3.1
BuildRequires:    R-CRAN-magrittr >= 2.0
BuildRequires:    R-CRAN-swfscMisc >= 1.5
BuildRequires:    R-CRAN-abind >= 1.4
BuildRequires:    R-CRAN-tidyr >= 1.1
BuildRequires:    R-CRAN-dplyr >= 1.0
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-randomForest >= 4.6
Requires:         R-CRAN-ggplot2 >= 3.3
Requires:         R-CRAN-tibble >= 3.1
Requires:         R-CRAN-magrittr >= 2.0
Requires:         R-CRAN-swfscMisc >= 1.5
Requires:         R-CRAN-abind >= 1.4
Requires:         R-CRAN-tidyr >= 1.1
Requires:         R-CRAN-dplyr >= 1.0
Requires:         R-grDevices 
Requires:         R-CRAN-gridExtra 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 

%description
Estimate significance of importance metrics for a Random Forest model by
permuting the response variable. Produces null distribution of importance
metrics for each predictor variable and p-value of observed. Provides
summary and visualization functions for 'randomForest' results.

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
