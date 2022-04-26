%global __brp_check_rpaths %{nil}
%global packname  TextForecast
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Analysis and Forecasting Using Textual Data from a Time-Varying Dictionary

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-udpipe 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-forecast 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-udpipe 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-pdftools 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-Matrix 

%description
Provides functionalities based on the paper "Time Varying Dictionary and
the Predictive Power of FED Minutes" (Lima, 2018)
<doi:10.2139/ssrn.3312483>. It selects the most predictive terms, that we
call time-varying dictionary using supervised machine learning techniques
as lasso and elastic net.

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
