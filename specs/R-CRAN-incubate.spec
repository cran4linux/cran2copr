%global __brp_check_rpaths %{nil}
%global packname  incubate
%global packver   1.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Time-to-Event Analysis with Variable Incubation Phases

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3
BuildRequires:    R-CRAN-future.apply >= 1.6
BuildRequires:    R-CRAN-glue >= 1.4
BuildRequires:    R-CRAN-future >= 1.21
BuildRequires:    R-CRAN-scales >= 0.5
BuildRequires:    R-CRAN-rlang >= 0.4
BuildRequires:    R-CRAN-purrr >= 0.3
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 >= 3.3
Requires:         R-CRAN-future.apply >= 1.6
Requires:         R-CRAN-glue >= 1.4
Requires:         R-CRAN-future >= 1.21
Requires:         R-CRAN-scales >= 0.5
Requires:         R-CRAN-rlang >= 0.4
Requires:         R-CRAN-purrr >= 0.3
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-tibble 

%description
Fit parametric models for time-to-event data that show an initial
'incubation period', i.e., a variable phase where the hazard is zero. The
delayed Weibull distribution serves as the foundational data model. The
specific method of MSE (maximum spacing estimation) is used for parameter
estimation. Bootstrap confidence intervals for parameters and significance
tests in a two group setting are provided.

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
