%global packname  wiserow
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Multi-Threaded, Coercion-Free Implementations of Common Row-WiseOperations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-RcppParallel >= 4.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-RcppParallel >= 4.4.0
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-methods 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-tidyselect 

%description
Fast row-oriented operations implemented in C++, all of which are
multi-threaded by leveraging 'RcppParallel' and 'RcppThread'. Virtually no
deep copies of input data are made, even of character data thanks to the
'string_ref' class from the C++ 'Boost' library. In contrast to other
functions, the ones in this package support data frames with differently
typed columns as input without coercing to a matrix, performing, if
necessary, on-the-fly type promotion according to R rules (like
transforming logicals to integers to allow summation).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/_pkgdown.yml
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
