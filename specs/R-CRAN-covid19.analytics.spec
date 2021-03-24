%global packname  covid19.analytics
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Load and Analyze Live Data from the CoViD-19 Pandemic

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-rentrez 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-collapsibleTree 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-rentrez 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-collapsibleTree 

%description
Load and analyze updated time series worldwide data of reported cases for
the Novel CoronaVirus Disease (CoViD-19) from different sources, including
the Johns Hopkins University Center for Systems Science and Engineering
(JHU CSSE) data repository <https://github.com/CSSEGISandData/COVID-19>,
"Our World in Data" <https://github.com/owid/> among several others. The
datasets reporting the CoViD19 cases are available in two main modalities,
as a time series sequences and aggregated data for the last day with
greater spatial resolution. Several analysis, visualization and modelling
functions are available in the package that will allow the user to compute
and visualize total number of cases, total number of changes and growth
rate globally or for an specific geographical location, while at the same
time generating models using these trends; generate interactive
visualizations and generate Susceptible-Infected-Recovered (SIR) model for
the disease spread.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
