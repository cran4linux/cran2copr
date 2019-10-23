%global packname  sourceR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Fits a Non-Parametric Bayesian Source Attribution Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tensorA 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-hashmap 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-cluster 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-SPIn 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tensorA 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-hashmap 
Requires:         R-CRAN-R6 
Requires:         R-cluster 
Requires:         R-stats 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-SPIn 
Requires:         R-grDevices 
Requires:         R-CRAN-reshape2 

%description
Implements a non-parametric source attribution model to attribute cases of
disease to sources in Bayesian framework with source and type effects.
Type effects are clustered using a Dirichlet Process. Multiple times and
locations are supported.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
