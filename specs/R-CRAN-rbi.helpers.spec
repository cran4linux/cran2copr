%global packname  rbi.helpers
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          2%{?dist}
Summary:          'RBi' Helper Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rbi >= 0.10.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-rbi >= 0.10.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-reshape2 
Requires:         R-Matrix 

%description
Contains a collection of helper functions to use with 'RBi', the R
interface to 'LibBi', described in Murray et al. (2015)
<doi:10.18637/jss.v067.i10>. It contains functions to adapt the proposal
distribution and number of particles in particle Markov-Chain Monte Carlo,
as well as calculating the Deviance Information Criterion (DIC) and
converting between times in 'LibBi' results and R time/dates.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/example_run.nc
%{rlibdir}/%{packname}/INDEX
