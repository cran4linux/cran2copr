%global packname  bayesreg
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}
Summary:          Bayesian Regression Models with Global-Local Shrinkage Priors

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats >= 3.0
BuildRequires:    R-CRAN-pgdraw >= 1.0
Requires:         R-stats >= 3.0
Requires:         R-CRAN-pgdraw >= 1.0

%description
Fits linear or logistic regression model using Bayesian global-local
shrinkage prior hierarchies as described in Polson and Scott (2010)
<doi:10.1093/acprof:oso/9780199694587.003.0017>. Handles ridge, lasso,
horseshoe and horseshoe+ regression with logistic, Gaussian, Laplace or
Student-t distributed targets using the algorithms summarized in Makalic
and Schmidt (2016) <arXiv:1611.06649>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
