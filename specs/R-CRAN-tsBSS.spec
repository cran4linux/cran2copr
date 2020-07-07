%global packname  tsBSS
%global packver   0.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.5
Release:          3%{?dist}
Summary:          Blind Source Separation and Supervised Dimension Reduction forTime Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-JADE >= 2.0.2
BuildRequires:    R-CRAN-ICtest >= 0.3.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-boot 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-JADE >= 2.0.2
Requires:         R-CRAN-ICtest >= 0.3.2
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-forecast 
Requires:         R-boot 
Requires:         R-parallel 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
Different estimators are provided to solve the blind source separation
problem for multivariate time series with stochastic volatility
(Matilainen, Nordhausen and Oja (2015) <doi:10.1016/j.spl.2015.04.033>;
Matilainen, Miettinen, Nordhausen, Oja and Taskinen (2017)
<doi:10.17713/ajs.v46i3-4.671>) and supervised dimension reduction problem
for multivariate time series (Matilainen, Croux, Nordhausen and Oja (2017)
<doi:10.1016/j.ecosta.2017.04.002>). Different functions based on AMUSE
and SOBI are also provided for estimating the dimension of the white noise
subspace.

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
%doc %{rlibdir}/%{packname}/ChangeLog
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
