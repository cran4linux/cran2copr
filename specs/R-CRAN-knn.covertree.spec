%global packname  knn.covertree
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          An Accurate kNN Implementation with Multiple Distance Measures

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.5.0
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-RcppEigen >= 0.3.3.5.0
Requires:         R-Matrix 
Requires:         R-methods 

%description
Similarly to the 'FNN' package, this package allows calculation of the k
nearest neighbors (kNN) of a data matrix. The implementation is based on
cover trees introduced by Alina Beygelzimer, Sham Kakade, and John
Langford (2006) <doi:10.1145/1143844.1143857>.

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
