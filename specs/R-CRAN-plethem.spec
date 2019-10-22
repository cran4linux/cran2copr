%global packname  plethem
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          Population Life Course Exposure to Health Effects Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-data.table 
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
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-data.table 
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

%description
Functions, data and user interfaces for performing Physiologically Based
Pharmacokinetic('PBPK') Modeling, In-vitro to In-vivo Extrapolation
('IVIVE') and exposure estimation. Also contains user interfaces to run
models from the 'httk' package. Taken together these provide an easy to
use and powerful modeling tool that can be used for all steps along the
source-to-outcome continuum.All the analysis tools in the package can only
be run as shiny apps. Check vignettes and package help for more
information. More information on PBPK modeling can be found in the book
'Physiologically Based Pharmacokinetic Modeling: Science and Applications'
by Reddy et al <doi:10.1002/0471478768>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/database
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/HT-IVIVE
%doc %{rlibdir}/%{packname}/httk_pbtk
%doc %{rlibdir}/%{packname}/rapidPBPK
%doc %{rlibdir}/%{packname}/rapidPBPK_pop
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
