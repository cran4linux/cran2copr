%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  popstudy
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Applied Techniques to Demographic and Time Series Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-demography 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-rcompanion 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-corrr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-correlation 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rainbow 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-CRAN-demography 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-moments 
Requires:         R-grid 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-rcompanion 
Requires:         R-utils 
Requires:         R-CRAN-corrr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-correlation 
Requires:         R-parallel 
Requires:         R-CRAN-here 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rainbow 
Requires:         R-CRAN-Rdpack 

%description
The use of overparameterization is proposed with combinatorial analysis to
test a broader spectrum of possible ARIMA models. In the selection of
ARIMA models, the most traditional methods such as correlograms or others,
do not usually cover many alternatives to define the number of
coefficients to be estimated in the model, which represents an estimation
method that is not the best. The popstudy package contains several tools
for statistical analysis in demography and time series based in Shryock
research (Shryock et. al. (1980)
<https://books.google.co.cr/books?id=8Oo6AQAAMAAJ>).

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
