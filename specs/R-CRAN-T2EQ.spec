%global __brp_check_rpaths %{nil}
%global packname  T2EQ
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Functions for Applying the T^2-Test for Equivalence

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Contains functions for applying the T^2-test for equivalence. The T^2-test
for equivalence is a multivariate two-sample equivalence test. Distance
measure of the test is the Mahalanobis distance. For multivariate normally
distributed data the T^2-test for equivalence is exact and UMPI. The
function T2EQ() implements the T^2-test for equivalence according to
Wellek (2010) <DOI:10.1201/ebk1439808184>. The function
T2EQ.dissolution.profiles.hoffelder() implements a variant of the T^2-test
for equivalence according to Hoffelder (2016)
<http://www.ecv.de/suse_item.php?suseId=Z|pi|8430> for the equivalence
comparison of highly variable dissolution profiles.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
