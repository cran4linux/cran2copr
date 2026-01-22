%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RSP
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          'shiny' Applications for Statistical and Psychometric Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MVN >= 6.0
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-ShinyItemAnalysis 
BuildRequires:    R-CRAN-catR 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-hornpa 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-polycor 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-semPlot 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ltm 
BuildRequires:    R-CRAN-shinycustomloader 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-MVN >= 6.0
Requires:         R-CRAN-DT 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-ShinyItemAnalysis 
Requires:         R-CRAN-catR 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-hornpa 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-polycor 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-semPlot 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ltm 
Requires:         R-CRAN-shinycustomloader 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-shiny 
Requires:         R-utils 
Requires:         R-CRAN-rstudioapi 

%description
Toolbox with 'shiny' applications for widely used psychometric methods.
Those methods include following analysis: Item analysis, item response
theory calibration, principal component analysis, confirmatory factor
analysis - structural equation modeling, generating simulated data.
References: Chalmers (2012, <doi:10.18637/jss.v048.i06>); Revelle (2022,
<https://CRAN.R-project.org/package=psych Version = 2.2.9.>); Rosseel
(2012, <doi:10.18637/jss.v048.i02>); Magis & Raiche (2012,
<doi:10.18637/jss.v048.i08>); Magis & Barrada (2017,
<doi:10.18637/jss.v076.c01>).

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
