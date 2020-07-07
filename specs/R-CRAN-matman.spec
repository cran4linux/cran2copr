%global packname  matman
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Material Management

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ISOweek 
Requires:         R-CRAN-shiny 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ISOweek 

%description
A set of functions, classes and methods for performing ABC and ABC/XYZ
analyses, identifying overperforming, underperforming and constantly
performing items, and plotting, analyzing as well as predicting the
temporal development of items.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
