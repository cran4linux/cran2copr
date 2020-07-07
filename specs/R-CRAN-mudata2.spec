%global packname  mudata2
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}
Summary:          Interchange Tools for Multi-Parameter Spatiotemporal Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.2
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-fs 
Requires:         R-CRAN-jsonlite >= 1.2
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-fs 

%description
Formatting and structuring multi-parameter spatiotemporal data is often a
time-consuming task. This package offers functions and data structures
designed to easily organize and visualize these data for applications in
geology, paleolimnology, dendrochronology, and paleoclimate. See
Dunnington and Spooner (2018) <doi:10.1139/facets-2017-0026>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
