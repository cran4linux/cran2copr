%global packname  arrApply
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Apply a Function to a Margin of an Array

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.0

%description
High performance variant of apply() for a fixed set of functions.
Considerable speedup is a trade-off for universality, user defined
functions cannot be used with this package. However, 21 most currently
employed functions are available for usage. They can be divided in three
types: reducing functions (like mean(), sum() etc., giving a scalar when
applied to a vector), mapping function (like normalise(), cumsum() etc.,
giving a vector of the same length as the input vector) and finally,
vector reducing function (like diff() which produces result vector of a
length different from the length of input vector). Optional or mandatory
additional arguments required by some functions (e.g. norm type for norm()
or normalise() functions) can be passed as named arguments in '...'.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
