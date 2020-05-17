%global packname  polAr
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Argentina Political Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.2
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.3
BuildRequires:    R-CRAN-geofacet 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-formattable 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-attempt 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-curl >= 4.2
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.3
Requires:         R-CRAN-geofacet 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-formattable 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-attempt 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grDevices 

%description
Toolbox for the Analysis of Political and Electoral Data from Argentina.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
