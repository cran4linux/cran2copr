%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nhscancerwaits
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          NHS Cancer Waiting-Time Analysis, Benchmarking and Multilevel Modelling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-broom.mixed 
BuildRequires:    R-CRAN-performance 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-writexl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-broom.mixed 
Requires:         R-CRAN-performance 
Requires:         R-CRAN-cluster 
Requires:         R-stats 
Requires:         R-CRAN-writexl 

%description
Provides tools for importing, harmonising, cleaning, analysing,
benchmarking and visualising National Health Service (NHS) England Cancer
Waiting Times data. The package supports national performance monitoring,
provider-level benchmarking and cancer pathway comparisons through key
performance indicator summaries, provider filtering, clustering analyses,
mixed-effects regression models, variance decomposition, intraclass
correlation coefficient estimation, adjusted provider performance
estimation and sensitivity analyses. Functions are included for
exploratory analysis, publication-ready visualisations and spreadsheet
exports, supporting reproducible health services research, cancer services
evaluation, quality improvement and assessment of waiting-time performance
across healthcare organisations. Mixed-effects modelling functionality is
based on Bates et al. (2015) <doi:10.18637/jss.v067.i01>. Multilevel
modelling concepts and variance decomposition follow Gelman and Hill
(2007, ISBN:9780521686891). Cancer Waiting Times definitions and reporting
standards follow NHS England
<https://www.england.nhs.uk/statistics/statistical-work-areas/cancer-waiting-times/>.

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
