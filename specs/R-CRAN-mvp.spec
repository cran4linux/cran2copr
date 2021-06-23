%global __brp_check_rpaths %{nil}
%global packname  mvp
%global packver   1.0-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          3%{?dist}%{?buildtag}
Summary:          Fast Symbolic Multivariate Polynomials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-mpoly >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-magic 
Requires:         R-CRAN-mpoly >= 1.1.0
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-magic 

%description
Fast manipulation of symbolic multivariate polynomials using the 'Map'
class of the Standard Template Library.  The package uses print and
coercion methods from the 'mpoly' package (Kahle 2013, "Multivariate
polynomials in R".  The R Journal, 5(1):162), but offers speed
improvements.  It is comparable in speed to the 'spray' package for sparse
arrays, but retains the symbolic benefits of 'mpoly'.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/gastineau.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
