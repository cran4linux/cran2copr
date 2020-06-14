%global packname  MESS
%global packver   0.5.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.6
Release:          2%{?dist}
Summary:          Miscellaneous Esoteric Statistical Scripts

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-geeM 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggformula 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-geeM 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggformula 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-kinship2 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 

%description
A mixed collection of useful and semi-useful diverse statistical
functions, some of which may even be referenced in The R Primer book.

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
%{rlibdir}/%{packname}/libs
