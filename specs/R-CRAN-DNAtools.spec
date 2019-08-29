%global packname  DNAtools
%global packver   0.1-22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.22
Release:          1%{?dist}
Summary:          Tools for Analysing Forensic Genetic DNA Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-multicool 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-multicool 

%description
Computationally efficient tools for comparing all pairs of profiles in a
DNA database. The expectation and covariance of the summary statistic is
implemented for fast computing. Routines for estimating proportions of
close related individuals are available. The use of wildcards (also called
F- designation) is implemented. Dedicated functions ease plotting the
results.

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
%{rlibdir}/%{packname}/libs
