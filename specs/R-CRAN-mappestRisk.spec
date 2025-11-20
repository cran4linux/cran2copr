%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mappestRisk
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Create Maps Forecasting Risk of Pest Occurrence

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geodata 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-khroma 
BuildRequires:    R-CRAN-nls.multstart 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rTPC 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geodata 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-khroma 
Requires:         R-CRAN-nls.multstart 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rTPC 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tidyr 

%description
There are three different modules: (1) model fitting and selection using a
set of the most commonly used equations describing developmental responses
to temperature helped by already existing R packages ('rTPC') and
nonlinear regression model functions from 'nls.multstart' (Padfield et al.
2021, <doi:10.1111/2041-210X.13585>), with visualization of model
predictions to guide ecological criteria for model selection; (2)
calculation of suitability thermal limits, which consist on a temperature
interval delimiting the optimal performance zone or suitability; and (3)
climatic data extraction and visualization inspired on previous research
(Taylor et al. 2019, <doi:10.1111/1365-2664.13455>), with either
exportable rasters, static map images or html, interactive maps.

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
