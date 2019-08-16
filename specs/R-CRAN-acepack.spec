%global packname  acepack
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}
Summary:          ACE and AVAS for Selecting Multiple Regression Transformations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core

%description
Two nonparametric methods for multiple regression transform selection are
provided. The first, Alternative Conditional Expectations (ACE), is an
algorithm to find the fixed point of maximal correlation, i.e. it finds a
set of transformed response variables that maximizes R^2 using smoothing
functions [see Breiman, L., and J.H. Friedman. 1985. "Estimating Optimal
Transformations for Multiple Regression and Correlation". Journal of the
American Statistical Association. 80:580-598.
<doi:10.1080/01621459.1985.10478157>]. Also included is the Additivity
Variance Stabilization (AVAS) method which works better than ACE when
correlation is low [see Tibshirani, R.. 1986. "Estimating Transformations
for Regression via Additivity and Variance Stabilization". Journal of the
American Statistical Association. 83:394-405.
<doi:10.1080/01621459.1988.10478610>]. A good introduction to these two
methods is in chapter 16 of Frank Harrel's "Regression Modeling
Strategies" in the Springer Series in Statistics.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ace.doc
%doc %{rlibdir}/%{packname}/README
%doc %{rlibdir}/%{packname}/README.ace
%doc %{rlibdir}/%{packname}/README.avas
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
