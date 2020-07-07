%global packname  EloOptimized
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          Optimized Elo Rating Method for Obtaining Dominance Ranks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-BAMMtools 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-BAMMtools 
Requires:         R-tcltk 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rlang 

%description
Provides an implementation of the maximum likelihood methods for deriving
Elo scores as published in Foerster, Franz et al. (2016)
<DOI:10.1038/srep35404>.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
