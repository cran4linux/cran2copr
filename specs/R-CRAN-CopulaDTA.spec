%global packname  CopulaDTA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Copula Based Bivariate Beta-Binomial Model for Diagnostic TestAccuracy Studies

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.2
Requires:         R-core >= 3.4.2
BuildArch:        noarch
BuildRequires:    R-stats >= 3.4.2
BuildRequires:    R-grDevices >= 3.4.2
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-rstan >= 2.16.2
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-methods 
Requires:         R-stats >= 3.4.2
Requires:         R-grDevices >= 3.4.2
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-rstan >= 2.16.2
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-methods 

%description
Modelling of sensitivity and specificity on their natural scale using
copula based bivariate beta-binomial distribution to yield marginal mean
sensitivity and specificity. The intrinsic negative correlation between
sensitivity and specificity is modelled using a copula function. A forest
plot can be obtained for categorical covariates or for the model with
intercept only. Nyaga VN, Arbyn M, Aerts M (2017)
<doi:10.18637/jss.v082.c01>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
