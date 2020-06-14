%global packname  MultNonParam
%global packver   1.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          2%{?dist}
Summary:          Multivariate Nonparametric Methods

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-ICSNP 
Requires:         R-CRAN-ICSNP 

%description
A collection of multivariate nonparametric methods, selected in part to
support an MS level course in nonparametric statistical methods. Methods
include adjustments for multiple comparisons, implementation of
multivariate Mann-Whitney-Wilcoxon testing, inversion of these tests to
produce a confidence region, some permutation tests for linear models, and
some algorithms for calculating exact probabilities associated with one-
and two- stage testing involving Mann-Whitney-Wilcoxon statistics.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/lastinput
%doc %{rlibdir}/%{packname}/Makefile
%doc %{rlibdir}/%{packname}/NOTE
%doc %{rlibdir}/%{packname}/test.csv
%doc %{rlibdir}/%{packname}/testaov.f90
%doc %{rlibdir}/%{packname}/testconcord.f90
%doc %{rlibdir}/%{packname}/testinput
%doc %{rlibdir}/%{packname}/testperm.f90
%doc %{rlibdir}/%{packname}/testperms.f90
%doc %{rlibdir}/%{packname}/testprobest.f90
%doc %{rlibdir}/%{packname}/testtskmsurv.f90
%doc %{rlibdir}/%{packname}/tskmsurv.F90
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
