%global packname  spduration
%global packver   0.17.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.17.1
Release:          3%{?dist}
Summary:          Split-Population Duration (Cure) Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-separationplot 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-corpcor 
Requires:         R-graphics 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-plyr 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-separationplot 
Requires:         R-CRAN-xtable 

%description
An implementation of split-population duration regression models. Unlike
regular duration models, split-population duration models are mixture
models that accommodate the presence of a sub-population that is not at
risk for failure, e.g. cancer patients who have been cured by treatment.
This package implements Weibull and Loglogistic forms for the duration
component, and focuses on data with time-varying covariates. These models
were originally formulated in Boag (1949)
<http://www.jstor.org/stable/2983694> and Berkson and Gage (1952)
<http://www.jstor.org/stable/2281318>, and extended in Schmidt and Witte
(1989) <doi:10.1016/0304-4076(89)90034-1>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
