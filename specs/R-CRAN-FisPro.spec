%global packname  FisPro
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Fuzzy Inference System Design and Optimization

License:          CeCILL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-methods 
Requires:         R-CRAN-Rdpack 

%description
Fuzzy inference systems are based on fuzzy rules, which have a good
capability for managing progressive phenomenons. This package is a basic
implementation of the main functions to use a Fuzzy Inference System (FIS)
provided by the open source software 'FisPro' <https://www.fispro.org>.
'FisPro' allows to create fuzzy inference systems and to use them for
reasoning purposes, especially for simulating a physical or biological
system.

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
