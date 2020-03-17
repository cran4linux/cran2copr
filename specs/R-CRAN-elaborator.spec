%global packname  elaborator
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          A 'shiny' Application for Exploring Laboratory Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-seriation 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-V8 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-bsplus 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-gclus 
Requires:         R-CRAN-seriation 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-V8 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-bsplus 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-gclus 

%description
A novel concept for generating knowledge and gaining insights into
laboratory data. You will be able to efficiently and easily explore your
laboratory data from different perspectives.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
