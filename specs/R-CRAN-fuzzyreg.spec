%global packname  fuzzyreg
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          2%{?dist}
Summary:          Fuzzy Linear Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-quadprog 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Estimators for fuzzy linear regression. The functions estimate parameters
of fuzzy linear regression models with crisp or fuzzy independent
variables (triangular fuzzy numbers are supported). Implements multiple
methods for parameter estimation and algebraic operations with triangular
fuzzy numbers. Includes functions for summarising, printing and plotting
the model fit. Calculates predictions from the model and total error of
fit. Diamond (1988) <doi:10.1016/0020-0255(88)90047-3>, Hung & Yang (2006)
<doi:10.1016/j.fss.2006.08.004>, Lee & Tanaka (1999)
<doi:10.15807/jorsj.42.98>, Nasrabadi, Nasrabadi & Nasrabady (2005)
<doi:10.1016/j.amc.2004.02.008>, Tanaka, Hayashi & Watada (1989)
<doi:10.1016/0377-2217(89)90431-1>, Zeng, Feng & Li (2017)
<doi:10.1016/j.asoc.2016.09.029>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
