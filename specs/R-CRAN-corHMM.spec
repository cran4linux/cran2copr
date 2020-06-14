%global packname  corHMM
%global packver   1.22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.22
Release:          2%{?dist}
Summary:          Analysis of Binary Character Evolution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rmpfr 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-corpcor 
Requires:         R-nnet 
Requires:         R-CRAN-phangorn 
Requires:         R-parallel 
Requires:         R-CRAN-Rmpfr 

%description
Fits a hidden rates model that allows different transition rate classes on
different portions of a phylogeny by treating rate classes as hidden
states in a Markov process and various other functions for evaluating
models of binary character evolution.

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
