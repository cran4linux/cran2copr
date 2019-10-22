%global packname  robets
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Forecasting Time Series with Robust Exponential Smoothing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.2
BuildRequires:    R-CRAN-forecast 
Requires:         R-CRAN-Rcpp >= 0.12.2
Requires:         R-CRAN-forecast 

%description
We provide an outlier robust alternative of the function ets() in the
'forecast' package of Hyndman and Khandakar (2008)
<DOI:10.18637/jss.v027.i03>. For each method of a class of exponential
smoothing variants we made a robust alternative. The class includes
methods with a damped trend and/or seasonal components. The robust method
is developed by robustifying every aspect of the original exponential
smoothing variant. We provide robust forecasting equations, robust initial
values, robust smoothing parameter estimation and a robust information
criterion. The method is described in more detail in Crevits and Croux
(2016) <DOI:10.13140/RG.2.2.11791.18080>.

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
