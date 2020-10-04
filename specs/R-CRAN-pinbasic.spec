%global packname  pinbasic
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Fast and Stable Estimation of the Probability of InformedTrading (PIN)

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-parallel 
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-stats 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-parallel 

%description
Utilities for fast and stable estimation of the probability of informed
trading (PIN) in the model introduced by Easley et al. (2002)
<DOI:10.1111/1540-6261.00493> are implemented. Since the basic model
developed by Easley et al. (1996) <DOI:10.1111/j.1540-6261.1996.tb04074.x>
is nested in the former due to equating the intensity of uninformed buys
and sells, functions can also be applied to this simpler model structure,
if needed. State-of-the-art factorization of the model likelihood function
as well as most recent algorithms for generating initial values for
optimization routines are implemented. In total, two likelihood
factorizations and three methodologies for starting values are included.
Furthermore, functions for simulating datasets of daily aggregated buys
and sells, calculating confidence intervals for the probability of
informed trading and posterior probabilities of trading days' conditions
are available.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
