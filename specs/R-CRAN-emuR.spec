%global packname  emuR
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          2%{?dist}
Summary:          Main Package of the EMU Speech Database Management System

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RSQLite >= 2.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.6.1
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-httpuv >= 1.3.2
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-tidyr >= 0.8.2
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-mime >= 0.6
BuildRequires:    R-CRAN-DBI >= 0.3.1
BuildRequires:    R-CRAN-git2r >= 0.27.1
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-rstudioapi >= 0.10
BuildRequires:    R-CRAN-wrassp >= 0.1.4
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-RSQLite >= 2.0.0
Requires:         R-CRAN-jsonlite >= 1.6.1
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-httpuv >= 1.3.2
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-tidyr >= 0.8.2
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-mime >= 0.6
Requires:         R-CRAN-DBI >= 0.3.1
Requires:         R-CRAN-git2r >= 0.27.1
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-rstudioapi >= 0.10
Requires:         R-CRAN-wrassp >= 0.1.4
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-shiny 

%description
Provides the next iteration of the EMU Speech Database Management System
(EMU-SDMS) with database management, data extraction, data preparation and
data visualization facilities.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
