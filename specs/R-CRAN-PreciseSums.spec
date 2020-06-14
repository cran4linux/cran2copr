%global packname  PreciseSums
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          2%{?dist}
Summary:          Accurate Floating Point Sums and Products

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2

%description
Most of the time floating point arithmetic does approximately the right
thing.  When adding sums or having products of numbers that greatly differ
in magnitude, the floating point arithmetic may be incorrect.  This
package implements the Kahan (1965) sum <doi:10.1145/363707.363723>,
Neumaier (1974) sum <doi:10.1002/zamm.19740540106>, pairwise-sum (adapted
from 'NumPy', See Castaldo (2008) <doi:10.1137/070679946> for a discussion
of accuracy), and arbitrary precision sum (adapted from the fsum in
'Python' ; Shewchuk (1997)
<http://www.cs.berkeley.edu/~jrs/papers/robustr.pdf>).  In addition,
products are changed to long double precision for accuracy, or changed
into a log-sum for accuracy.

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
%{rlibdir}/%{packname}/include
