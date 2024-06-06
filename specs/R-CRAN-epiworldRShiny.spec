%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epiworldRShiny
%global packver   0.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A 'shiny' Wrapper of the R Package 'epiworldR'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-epiworldR 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-utils 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-epiworldR 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-plotly 

%description
R 'shiny' web apps for epidemiological Agent-Based Models. It provides a
user-friendly interface to the Agent-Based Modeling (ABM) R package
'epiworldR' (Meyer et al., 2023) <DOI:10.21105/joss.05781>. Some of the
main features of the package include the Susceptible-Infected-Susceptible
(SIS), Susceptible-Infected-Recovered (SIR), and
Susceptible-Exposed-Infected-Recovered (SEIR) models. 'epiworldRShiny'
provides a web-based user interface for running various epidemiological
ABMs, simulating interventions, and visualizing results interactively.

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
