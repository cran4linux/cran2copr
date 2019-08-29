%global packname  covsep
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Tests for Determining if the Covariance Structure of2-Dimensional Data is Separable

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm >= 1.0.4
Requires:         R-CRAN-mvtnorm >= 1.0.4

%description
Functions for testing if the covariance structure of 2-dimensional data
(e.g. samples of surfaces X_i = X_i(s,t)) is separable, i.e. if
covariance(X) = C_1 x C_2. A complete descriptions of the implemented
tests can be found in the paper Aston, John A. D.; Pigoli, Davide;
Tavakoli, Shahin. Tests for separability in nonparametric covariance
operators of random surfaces. Ann. Statist. 45 (2017), no. 4, 1431--1461.
<doi:10.1214/16-AOS1495> <https://projecteuclid.org/euclid.aos/1498636862>
<arXiv:1505.02023>.

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
