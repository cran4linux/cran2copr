%global packname  FuzzyStatTra
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Statistical Methods for Trapezoidal Fuzzy Numbers

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The aim of the package is to provide some basic functions for doing
statistics with trapezoidal fuzzy numbers. In particular, the package
contains several functions for simulating trapezoidal fuzzy numbers, as
well as for calculating some central tendency measures (mean and two types
of median), some scale measures (variance, ADD, MDD, Sn, Qn, Tn and some
M-estimators) and one diversity index and one inequality index. Moreover,
functions for calculating the 1-norm distance, the mid/spr distance and
the (phi,theta)-wabl/ldev/rdev distance between fuzzy numbers are
included, and a function to calculate the value phi-wabl given a sample of
trapezoidal fuzzy numbers.

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
