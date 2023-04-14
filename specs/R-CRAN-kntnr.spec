%global __brp_check_rpaths %{nil}
%global packname  kntnr
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          3%{?dist}%{?buildtag}
Summary:          R Client for 'kintone' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-purrr >= 0.2.3
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-purrr >= 0.2.3
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Retrieve data from 'kintone' (<https://www.kintone.com/>) via its API.
'kintone' is an enterprise application platform.

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
%{rlibdir}/%{packname}
