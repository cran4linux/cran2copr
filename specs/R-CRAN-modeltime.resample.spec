%global packname  modeltime.resample
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Resampling Tools for Time Series Forecasting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-timetk >= 2.5.0
BuildRequires:    R-CRAN-modeltime >= 0.3.0
BuildRequires:    R-CRAN-parsnip >= 0.1.4
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-workflows 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-yardstick 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-tictoc 
Requires:         R-CRAN-timetk >= 2.5.0
Requires:         R-CRAN-modeltime >= 0.3.0
Requires:         R-CRAN-parsnip >= 0.1.4
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-tune 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-workflows 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-dials 
Requires:         R-CRAN-yardstick 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-tictoc 

%description
A 'modeltime' extension that implements forecast resampling tools that
assess time-based model performance and stability for a single time
series, panel data, and cross-sectional time series analysis.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
