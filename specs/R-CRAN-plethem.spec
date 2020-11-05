%global packname  plethem
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Population Life Course Exposure to Health Effects Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-formatR 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-V8 
BuildRequires:    R-CRAN-httk 
BuildRequires:    R-CRAN-NonCompart 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-DiagrammeRsvg 
BuildRequires:    R-CRAN-rsvg 
BuildRequires:    R-CRAN-devEMF 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-formatR 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-sqldf 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-V8 
Requires:         R-CRAN-httk 
Requires:         R-CRAN-NonCompart 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-DiagrammeRsvg 
Requires:         R-CRAN-rsvg 
Requires:         R-CRAN-devEMF 

%description
Functions, data and user interfaces for performing physiologically based
pharmacokinetic ('PBPK') modeling, in-vitro-to-in-vivo Extrapolation
('IVIVE') and exposure estimation. Also contains user interfaces to run
models from the 'httk' package. Taken together these provide an easy to
use and powerful modeling tool that can be used for all steps along the
source-to-outcome continuum.All the analysis tools in the package are run
as interactive applications. Check package help for more information.
Refer to the manuscript 'Population Life-course exposure to health effects
model (PLETHEM): An R package for PBPK modeling' <doi:
10.1016/j.comtox.2019.100115> for more information on the models and
algorithms used in the package. More information on PBPK modeling itself
can be found in the book 'Physiologically Based Pharmacokinetic Modeling:
Science and Applications' by Reddy et al <doi:10.1002/0471478768>.

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
