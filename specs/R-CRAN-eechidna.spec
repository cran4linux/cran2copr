%global packname  eechidna
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          3%{?dist}
Summary:          Exploring Election and Census Highly Informative Data Nationallyfor Australia

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.5.6
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-plotly >= 4.5.6
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-tidyr 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-rgdal 
Requires:         R-methods 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 

%description
Data from the seven Australian Federal Elections (House of
Representatives) between 2001 and 2019, and from the four Australian
Censuses over the same period. Includes tools for visualizing and
analysing the data, as well as imputing Census data for years in which a
Census does not occur. This package incorporates data that is copyright
Commonwealth of Australia (Australian Electoral Commission and Australian
Bureau of Statistics) 2019.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
