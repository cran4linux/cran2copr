%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RGAP
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Production Function Output Gap Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-KFAS 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-dlm 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-stats 
Requires:         R-CRAN-KFAS 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-dlm 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
The output gap indicates the percentage difference between the actual
output of an economy and its potential. Since potential output is a latent
process, the estimation of the output gap poses a challenge and numerous
filtering techniques have been proposed. 'RGAP' facilitates the estimation
of a Cobb-Douglas production function type output gap, as suggested by the
European Commission (Havik et al. 2014)
<https://ideas.repec.org/p/euf/ecopap/0535.html>. To that end, the
non-accelerating wage rate of unemployment (NAWRU) and the trend of total
factor productivity (TFP) can be estimated in two bivariate unobserved
component models by means of Kalman filtering and smoothing. 'RGAP'
features a flexible modeling framework for the appropriate state-space
models and offers frequentist as well as Bayesian estimation techniques.
Additional functionalities include direct access to the 'AMECO'
<https://economy-finance.ec.europa.eu/economic-research-and-databases/economic-databases/ameco-database_en>
database and automated model selection procedures. See the paper by
Streicher (2022) <http://hdl.handle.net/20.500.11850/552089> for details.

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
