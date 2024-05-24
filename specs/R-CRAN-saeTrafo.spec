%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  saeTrafo
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Transformations for Unit-Level Small Area Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-emdi 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-parallelMap 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-HLMdiag 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-readODS 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-emdi 
Requires:         R-stats 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-parallelMap 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-HLMdiag 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-readODS 
Requires:         R-CRAN-rlang 

%description
The aim of this package is to offer new methodology for unit-level small
area models under transformations and limited population auxiliary
information. In addition to this new methodology, the widely used nested
error regression model without transformations (see "An Error-Components
Model for Prediction of County Crop Areas Using Survey and Satellite Data"
by Battese, Harter and Fuller (1988) <doi:10.1080/01621459.1988.10478561>)
and its well-known uncertainty estimate (see "The estimation of the mean
squared error of small-area estimators" by Prasad and Rao (1990)
<doi:10.1080/01621459.1995.10476570>) are provided. In this package, the
log transformation and the data-driven log-shift transformation are
provided. If a transformation is selected, an appropriate method is chosen
depending on the respective input of the population data: Individual
population data (see "Empirical best prediction under a nested error model
with log transformation" by Molina and Martín (2018)
<doi:10.1214/17-aos1608>) but also aggregated population data (see
"Estimating regional income indicators under transformations and access to
limited population auxiliary information" by Würz, Schmid and Tzavidis
<unpublished>) can be entered. Especially under limited data access, new
methodologies are provided in saeTrafo. Several options are available to
assess the used model and to judge, present and export its results. For a
detailed description of the package and the methods used see the
corresponding vignette.

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
