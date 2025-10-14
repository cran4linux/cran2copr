%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flashlight
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Shed Light on Black Box Machine Learning Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-MetricsWeighted >= 0.3.0
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-rpart.plot 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-MetricsWeighted >= 0.3.0
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-rpart.plot 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 

%description
Shed light on black box machine learning models by the help of model
performance, variable importance, global surrogate models, ICE profiles,
partial dependence (Friedman J. H. (2001) <doi:10.1214/aos/1013203451>),
accumulated local effects (Apley D. W. (2016)
<doi:10.48550/arXiv.1612.08468>), further effects plots, interaction
strength, and variable contribution breakdown (Gosiewska and Biecek (2019)
<doi:10.48550/arXiv.1903.11420>).  All tools are implemented to work with
case weights and allow for stratified analysis.  Furthermore, multiple
flashlights can be combined and analyzed together.

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
