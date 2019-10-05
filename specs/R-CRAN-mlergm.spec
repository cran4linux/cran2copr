%global packname  mlergm
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Multilevel Exponential-Family Random Graph Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ergm >= 3.10.1
BuildRequires:    R-CRAN-sna >= 2.4
BuildRequires:    R-CRAN-network >= 1.15
BuildRequires:    R-parallel 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
Requires:         R-CRAN-ergm >= 3.10.1
Requires:         R-CRAN-sna >= 2.4
Requires:         R-CRAN-network >= 1.15
Requires:         R-parallel 
Requires:         R-Matrix 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 
Requires:         R-methods 
Requires:         R-graphics 

%description
Estimates exponential-family random graph models for multilevel network
data, assuming the multilevel structure is observed. The scope, at
present, covers multilevel models where the set of nodes is nested within
known blocks. The estimation method uses Monte-Carlo maximum likelihood
estimation (MCMLE) methods to estimate a variety of canonical or curved
exponential family models for binary random graphs. MCMLE methods for
curved exponential-family random graph models can be found in Hunter and
Handcock (2006) <DOI: 10.1198/106186006X133069>. The package supports
parallel computing, and provides methods for assessing goodness-of-fit of
models and visualization of networks.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
