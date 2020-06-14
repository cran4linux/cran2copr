%global packname  plotly
%global packver   4.9.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.9.2.1
Release:          2%{?dist}
Summary:          Create Interactive Web Graphics via 'plotly.js'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-htmlwidgets >= 1.3
BuildRequires:    R-CRAN-htmltools >= 0.3.6
BuildRequires:    R-CRAN-lazyeval >= 0.2.0
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-crosstalk 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-promises 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-htmlwidgets >= 1.3
Requires:         R-CRAN-htmltools >= 0.3.6
Requires:         R-CRAN-lazyeval >= 0.2.0
Requires:         R-tools 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-hexbin 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-crosstalk 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-promises 

%description
Create interactive web graphics from 'ggplot2' graphs and/or a custom
interface to the (MIT-licensed) JavaScript library 'plotly.js' inspired by
the grammar of graphics.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/docker
%doc %{rlibdir}/%{packname}/docs.R
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/plotlyjs.R
%doc %{rlibdir}/%{packname}/stars.R
%{rlibdir}/%{packname}/INDEX
