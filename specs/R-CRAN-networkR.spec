%global packname  networkR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          Network Analysis and Visualization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fastmatch 
Requires:         R-Matrix 

%description
Collection of functions for fast manipulation, handling, and analysis of
large-scale networks based on family and social data. Functions are
utility functions used to manipulate data in three "formats": sparse
adjacency matrices, pedigree trio family data, and pedigree family data.
When possible, the functions should be able to handle millions of data
points quickly for use in combination with data from large public national
registers and databases. Kenneth Lange (2003, ISBN:978-8181281135).

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
%{rlibdir}/%{packname}/libs
