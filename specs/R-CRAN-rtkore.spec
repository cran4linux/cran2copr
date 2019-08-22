%global packname  rtkore
%global packver   1.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.5
Release:          1%{?dist}
Summary:          'STK++' Core Library Integration to 'R' using 'Rcpp'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-inline 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-inline 

%description
'STK++' <http://www.stkpp.org> is a collection of C++ classes for
statistics, clustering, linear algebra, arrays (with an 'Eigen'-like API),
regression, dimension reduction, etc. The integration of the library to
'R' is using 'Rcpp'. The 'rtkore' package includes the header files from
the 'STK++' core library. All files contain only template classes and/or
inline functions. 'STK++' is licensed under the GNU LGPL version 2 or
later. 'rtkore' (the 'stkpp' integration into 'R') is licensed under the
GNU GPL version 2 or later. See file LICENSE.note for details.

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
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/projects
%doc %{rlibdir}/%{packname}/templates
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
