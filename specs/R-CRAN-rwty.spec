%global packname  rwty
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          R We There Yet? Visualizing MCMC Convergence in Phylogenetics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-viridis 
Requires:         R-grid 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-GGally 
Requires:         R-parallel 

%description
Implements various tests, visualizations, and metrics for diagnosing
convergence of MCMC chains in phylogenetics.  It implements and automates
many of the functions of the AWTY package in the R environment.

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
