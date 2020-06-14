%global packname  bayespref
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Hierarchical Bayesian analysis of ecological count data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-lattice 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-coda 
Requires:         R-lattice 
Requires:         R-MASS 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-RColorBrewer 

%description
This program implements a hierarchical Bayesian analysis of count data,
such as preference experiments. It provides population-level and
individual-level preference parameter estimates obtained via MCMC. It also
allows for model comparison using Deviance Information Criterion.

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
%{rlibdir}/%{packname}/INDEX
