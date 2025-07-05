%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sampcompR
%global packver   0.3.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Comparing and Visualizing Differences Between Surveys

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-svrep 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-svrep 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 

%description
Easily analyze and visualize differences between samples (e.g., benchmark
comparisons, nonresponse comparisons in surveys) on three levels. The
comparisons can be univariate, bivariate or multivariate. On univariate
level the variables of interest of a survey and a comparison survey (i.e.
benchmark) are compared, by calculating one of several difference measures
(e.g., relative difference in mean), and an average difference between the
surveys. On bivariate level a function can calculate significant
differences in correlations for the surveys. And on multivariate levels a
function can calculate significant differences in model coefficients
between the surveys of comparison. All of those differences can be easily
plotted and outputted as a table. For more detailed information on the
methods and example use see Rohr, B., Silber, H., & Felderer, B. (2024).
Comparing the Accuracy of Univariate, Bivariate, and Multivariate
Estimates across Probability and Nonprobability Surveys with Population
Benchmarks. Sociological Methodology <doi:10.1177/00811750241280963>.

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
