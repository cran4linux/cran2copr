%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MassWateR
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quality Control and Analysis of Massachusetts Water Quality Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggspatial 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-maptiles 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyterra 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-writexl 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggspatial 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-maptiles 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyterra 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-units 
Requires:         R-CRAN-writexl 

%description
Methods for quality control and exploratory analysis of surface water
quality data collected in Massachusetts, USA.  Functions are developed to
facilitate data formatting for the Water Quality Exchange Network
<https://www.epa.gov/waterdata/water-quality-data-upload-wqx> and
reporting of data quality objectives to state agencies. Quality control
methods are from Massachusetts Department of Environmental Protection
(2020)
<https://www.mass.gov/orgs/massachusetts-department-of-environmental-protection>.

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
