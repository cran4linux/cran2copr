%global __brp_check_rpaths %{nil}
%global packname  skm
%global packver   0.1.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5.4
Release:          3%{?dist}%{?buildtag}
Summary:          Selective k-Means

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-RcppParallel 

%description
Algorithms for solving selective k-means problem, which is defined as
finding k rows in an m x n matrix such that the sum of each column minimal
is minimized. In the scenario when m == n and each cell value in matrix is
a valid distance metric, this is equivalent to a k-means problem. The
selective k-means extends the k-means problem in the sense that it is
possible to have m != n, often the case m < n which implies the search is
limited within a small subset of rows. Also, the selective k-means extends
the k-means problem in the sense that the instance in row set can be
instance not seen in the column set, e.g., select 2 from 3 internet
service provider (row) for 5 houses (column) such that minimize the
overall cost (cell value) - overall cost is the sum of the column minimal
of the selected 2 service provider.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
