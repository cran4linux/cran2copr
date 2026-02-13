%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ViroReportR
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Respiratory Viral Infection Forecast Reporting

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-EpiEstim 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-incidence 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-projections 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-cowplot 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-EpiEstim 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-incidence 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-projections 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-cowplot 

%description
Tools for reporting and forecasting viral respiratory infections, using
case surveillance data. Report generation tools for short-term forecasts,
and validation metrics for an arbitrary number of customizable respiratory
viruses. Estimation of the effective reproduction number is based on the
'EpiEstim' framework described in work by 'Cori' and colleagues. (2013)
<doi:10.1093/aje/kwt133>.

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
