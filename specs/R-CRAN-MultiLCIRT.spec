%global packname  MultiLCIRT
%global packver   2.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.11
Release:          3%{?dist}
Summary:          Multidimensional Latent Class Item Response Theory Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-limSolve 
Requires:         R-MASS 
Requires:         R-CRAN-limSolve 

%description
Framework for the Item Response Theory analysis of dichotomous and ordinal
polytomous outcomes under the assumption of multidimensionality and
discreteness of the latent traits. The fitting algorithms allow for
missing responses and for different item parameterizations and are based
on the Expectation-Maximization paradigm. Individual covariates affecting
the class weights may be included in the new version (since 2.1).

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
