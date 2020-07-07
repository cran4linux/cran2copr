%global packname  echarts4r
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          2%{?dist}
Summary:          Create Interactive Graphs with 'Echarts JavaScript' Version 4

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-d3r 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-d3r 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rstudioapi 

%description
Easily create interactive charts by leveraging the 'Echarts Javascript'
library which includes 36 chart types, themes, 'Shiny' proxies and
animations.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/tutorials
%{rlibdir}/%{packname}/INDEX
