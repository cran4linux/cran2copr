%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hbsaems
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Bayes Small Area Estimation Model using 'Stan'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-brms 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-bridgesampling 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-minerva 
BuildRequires:    R-CRAN-priorsense 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-XICOR 
Requires:         R-CRAN-brms 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-bridgesampling 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-minerva 
Requires:         R-CRAN-priorsense 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinydashboard 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-CRAN-XICOR 

%description
Implementing Hierarchical Bayesian Small Area Estimation models using the
'brms' package as the computational backend. The modeling framework
follows the methodological foundations described in area-level models.
This package is designed to facilitate a principled Bayesian workflow,
enabling users to conduct prior predictive checks, model fitting,
posterior predictive checks, model comparison, and sensitivity analysis in
a coherent and reproducible manner. It supports flexible model
specifications via 'brms' and promotes transparency in model development,
aligned with the recommendations of modern Bayesian data analysis
practices, implementing methods described in Rao and Molina (2015)
<doi:10.1002/9781118735855>.

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
