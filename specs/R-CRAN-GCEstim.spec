%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GCEstim
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Coefficients Estimation Using the Generalized Cross Entropy

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-downlit 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-lbfgs 
BuildRequires:    R-CRAN-lbfgsb3c 
BuildRequires:    R-CRAN-meboot 
BuildRequires:    R-CRAN-optimParallel 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-clusterGeneration 
BuildRequires:    R-CRAN-simstudy 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-pathviewr 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-bayestestR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggdist 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-hdrcde 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinydashboardPlus 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-downlit 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-lbfgs 
Requires:         R-CRAN-lbfgsb3c 
Requires:         R-CRAN-meboot 
Requires:         R-CRAN-optimParallel 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-rstudioapi 
Requires:         R-stats 
Requires:         R-CRAN-clusterGeneration 
Requires:         R-CRAN-simstudy 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-pathviewr 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-bayestestR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggdist 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-hdrcde 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinydashboardPlus 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-magrittr 

%description
Estimation and inference using the Generalized Maximum Entropy (GME) and
Generalized Cross Entropy (GCE) framework, a flexible method for solving
ill-posed inverse problems and parameter estimation under uncertainty
(Golan, Judge, and Miller (1996, ISBN:978-0471145925) "Maximum Entropy
Econometrics: Robust Estimation with Limited Data"). The package includes
routines for generalized cross entropy estimation of linear models
including the implementation of a GME-GCE two steps approach. Diagnostic
tools, and options to incorporate prior information through support and
prior distributions are available (Macedo, Cabral, Afreixo, Macedo and
Angelelli (2025) <doi:10.1007/978-3-031-97589-9_21>). In particular,
support spaces can be defined by the user or be internally computed based
on the ridge trace or on the distribution of standardized regression
coefficients. Different optimization methods for the objective function
can be used. An adaptation of the normalized entropy aggregation (Macedo
and Costa (2019) <doi:10.1007/978-3-030-26036-1_2> "Normalized entropy
aggregation for inhomogeneous large-scale data") and a two-stage maximum
entropy approach for time series regression (Macedo (2022)
<doi:10.1080/03610918.2022.2057540>) are also available. Suitable for
applications in econometrics, health, signal processing, and other fields
requiring robust estimation under data constraints.

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
