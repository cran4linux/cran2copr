%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Dyn4cast
%global packver   11.11.26
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          11.11.26
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Modeling and Machine Learning Environment

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-formattable 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-ModelMetrics 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-modelsummary 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-marginaleffects 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-stats 
Requires:         R-splines 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-formattable 
Requires:         R-utils 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-ModelMetrics 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-modelsummary 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-marginaleffects 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-tidyselect 

%description
Estimates, predict and forecast dynamic models as well as Machine Learning
metrics which assists in model selection for further analysis. The package
also have capabilities to provide tools and metrics that are useful in
machine learning and modeling. For example, there is quick summary,
percent sign, Mallow's Cp tools and others. The ecosystem of this package
is analysis of economic data for national development. The package is so
far stable and has high reliability and efficiency as well as time-saving.
The package is a variety but the following references are important guide
to the major themes in the package (Hyndman & Athanasopoulos (2014 ISBN
978-0-9875071-0-5), Alkire & Santos (2014,
doi.org/10.1016/j.worlddev.2014.01.026)).

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
