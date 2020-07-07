%global packname  DNAtools
%global packver   0.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}
Summary:          Tools for Analysing Forensic Genetic DNA Data

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-RcppParallel >= 4.3.20
BuildRequires:    R-CRAN-Rsolnp >= 1.16
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-multicool >= 0.1.10
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-RcppParallel >= 4.3.20
Requires:         R-CRAN-Rsolnp >= 1.16
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-multicool >= 0.1.10

%description
Computationally efficient tools for comparing all pairs of profiles in a
DNA database. The expectation and covariance of the summary statistic is
implemented for fast computing. Routines for estimating proportions of
close related individuals are available. The use of wildcards (also called
F- designation) is implemented. Dedicated functions ease plotting the
results.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
