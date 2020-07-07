%global packname  MCMCglmm
%global packver   2.29
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.29
Release:          3%{?dist}
Summary:          MCMC Generalised Linear Mixed Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-tensorA 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-methods 
Requires:         R-Matrix 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-tensorA 
Requires:         R-CRAN-cubature 
Requires:         R-methods 

%description
MCMC Generalised Linear Mixed Models.

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
%{rlibdir}/%{packname}/libs
