%global packname  BAYESDEF
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Bayesian Analysis of DSD

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         tcl
Requires:         tk
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-gWidgets 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-REdaS 
Requires:         R-tcltk 
Requires:         R-CRAN-gWidgets 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-REdaS 

%description
Definitive Screening Designs are a class of experimental designs that
under factor sparsity have the potential to estimate linear, quadratic and
interaction effects with little experimental effort. BAYESDEF is a package
that performs a five step strategy to analyze this kind of experiments
that makes use of tools coming from the Bayesian approach. It also
includes the least absolute shrinkage and selection operator (lasso) as a
check (Aguirre VM. (2016) <DOI:10.1002/asmb.2160>).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
