%global packname  gsubfn
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          3%{?dist}
Summary:          Utilities for Strings and Function Arguments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-proto 
Requires:         R-CRAN-proto 

%description
The gsubfn function is like gsub but can take a replacement function or
certain other objects instead of the replacement string. Matches and back
references are input to the replacement function and replaced by the
function output.  gsubfn can be used to split strings based on content
rather than delimiters and for quasi-perl-style string interpolation. The
package also has facilities for translating formulas to functions and
allowing such formulas in function calls instead of functions.  This can
be used with R functions such as apply, sapply, lapply, optim, integrate,
xyplot, Filter and any other function that expects another function as an
input argument or functions like cat or sql calls that may involve strings
where substitution is desirable. There is also a facility for returning
multiple objects from functions and a version of transform that allows the
RHS to refer to LHS used in the same transform.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ANNOUNCE
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/lipsum.txt
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/sample.txt
%doc %{rlibdir}/%{packname}/THANKS
%doc %{rlibdir}/%{packname}/unitTests
%doc %{rlibdir}/%{packname}/WISHLIST
%{rlibdir}/%{packname}/INDEX
