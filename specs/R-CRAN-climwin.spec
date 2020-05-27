%global packname  climwin
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}
Summary:          Climate Window Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-nlme 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-Matrix 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-RcppRoll 
Requires:         R-nlme 

%description
Contains functions to detect and visualise periods of climate sensitivity
(climate windows) for a given biological response. Please see van de Pol
et al. (2016) <doi:10.1111/2041-210X.12590> and Bailey and van de Pol
(2016) <doi:10.1371/journal.pone.0167980> for details.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
