%global __brp_check_rpaths %{nil}
%global packname  seer
%global packver   1.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Feature-Based Forecast Model Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.3
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-forecTheta 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tsfeatures 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-forecast >= 8.3
Requires:         R-stats 
Requires:         R-CRAN-urca 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-forecTheta 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 
Requires:         R-utils 
Requires:         R-CRAN-tsfeatures 
Requires:         R-CRAN-MASS 

%description
A novel meta-learning framework for forecast model selection using time
series features. Many applications require a large number of time series
to be forecast. Providing better forecasts for these time series is
important in decision and policy making. We propose a classification
framework which selects forecast models based on features calculated from
the time series. We call this framework FFORMS (Feature-based FORecast
Model Selection). FFORMS builds a mapping that relates the features of
time series to the best forecast model using a random forest. 'seer'
package is the implementation of the FFORMS algorithm. For more details
see our paper at
<https://www.monash.edu/business/econometrics-and-business-statistics/research/publications/ebs/wp06-2018.pdf>.

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
