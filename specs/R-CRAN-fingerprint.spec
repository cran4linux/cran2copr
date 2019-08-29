%global packname  fingerprint
%global packver   3.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.7
Release:          1%{?dist}
Summary:          Functions to Operate on Binary Fingerprint Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Functions to manipulate binary fingerprints of arbitrary length. A
fingerprint is represented by an object of S4 class 'fingerprint' which is
internally represented a vector of integers, such that each element
represents the position in the fingerprint that is set to 1. The bitwise
logical functions in R are overridden so that they can be used directly
with 'fingerprint' objects. A number of distance metrics are also
available (many contributed by Michael Fadock). Fingerprints can be
converted to Euclidean vectors (i.e., points on the unit hypersphere) and
can also be folded using OR.  Arbitrary fingerprint formats can be handled
via line handlers. Currently handlers are provided for CDK, MOE and BCI
fingerprint data.

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
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
