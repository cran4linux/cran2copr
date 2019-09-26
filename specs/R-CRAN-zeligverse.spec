%global packname  zeligverse
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Easily Install and Load Stable Zelig Packages

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Amelia 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-WhatIf 
BuildRequires:    R-CRAN-Zelig 
BuildRequires:    R-CRAN-ZeligChoice 
BuildRequires:    R-CRAN-ZeligEI 
Requires:         R-CRAN-Amelia 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-MatchIt 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-WhatIf 
Requires:         R-CRAN-Zelig 
Requires:         R-CRAN-ZeligChoice 
Requires:         R-CRAN-ZeligEI 

%description
Provides an easy way to load stable Core Zelig and ancillary Zelig
packages.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
