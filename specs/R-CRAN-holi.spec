%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  holi
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Higher Order Likelihood Inference Web Applications

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-likelihoodAsy 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pool 
BuildRequires:    R-CRAN-RPostgres 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-sn 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-likelihoodAsy 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pool 
Requires:         R-CRAN-RPostgres 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-sn 

%description
Higher order likelihood inference is a promising approach for analyzing
small sample size data. The 'holi' package provides web applications for
higher order likelihood inference. It currently supports linear, logistic,
and Poisson generalized linear models through the rstar_glm() function,
based on Pierce and Bellio (2017) <doi:10.1111/insr.12232> and
'likelihoodAsy'. The package offers two main features: LA_rstar(), which
launches an interactive 'shiny' application allowing users to fit models
with rstar_glm() through their web browser, and sim_rstar_glm_pgsql(),
which streamlines the process of launching a web-based 'shiny' simulation
application that saves results to a user-created 'PostgreSQL' database.

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
