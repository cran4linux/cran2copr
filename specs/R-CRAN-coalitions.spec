%global packname  coalitions
%global packver   0.6.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.12
Release:          3%{?dist}
Summary:          Bayesian "Now-Cast" Estimation of Event Probabilities inMulti-Party Democracies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr > 0.5.0
BuildRequires:    R-CRAN-purrr > 0.2.2
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr > 0.5.0
Requires:         R-CRAN-purrr > 0.2.2
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 

%description
An implementation of a Bayesian framework for the opinion poll based
estimation of event probabilities in multi-party electoral systems (Bender
and Bauer (2018) <doi:10.21105/joss.00606>).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
