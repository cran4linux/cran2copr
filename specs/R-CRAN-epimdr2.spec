%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epimdr2
%global packver   1.0-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Functions and Data for "Epidemics: Models and Data in R (2nd Edition)"

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-polspline 
BuildRequires:    R-CRAN-phaseR 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-polspline 
Requires:         R-CRAN-phaseR 
Requires:         R-CRAN-ggplot2 

%description
Functions, data sets and shiny apps for "Epidemics: Models and Data in R
(2nd edition)" by Ottar N. Bjornstad (2022, ISBN: 978-3-031-12055-8)
<https://link.springer.com/book/10.1007/978-3-319-97487-3>. The package
contains functions to study the Susceptible-Exposed-Infected-Removed SEIR
model, spatial and age-structured Susceptible-Infected-Removed SIR models;
time-series SIR and chain-binomial stochastic models; catalytic disease
models; coupled map lattice models of spatial transmission and network
models for social spread of infection. The package is also an advanced
quantitative companion to the 'Coursera' Epidemics Massive Online Open
Course <https://www.coursera.org/learn/epidemics>.

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
