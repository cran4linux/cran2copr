%global packname  MasterBayes
%global packver   2.55
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.55
Release:          1%{?dist}
Summary:          ML and MCMC Methods for Pedigree Reconstruction and Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-genetics 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-genetics 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-kinship2 
Requires:         R-methods 
Requires:         R-stats 

%description
The primary aim of MasterBayes is to use MCMC techniques to integrate over
uncertainty in pedigree configurations estimated from molecular markers
and phenotypic data.  Emphasis is put on the marginal distribution of
parameters that relate the phenotypic data to the pedigree. All simulation
is done in compiled C++ for efficiency.

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
