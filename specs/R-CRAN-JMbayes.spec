%global packname  JMbayes
%global packver   0.8-85
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.85
Release:          1%{?dist}
Summary:          Joint Modeling of Longitudinal and Time-to-Event Data under aBayesian Approach

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-nlme 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-jagsUI 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-nlme 
Requires:         R-survival 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-rstan 
Requires:         R-MASS 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-jagsUI 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-shiny 
Requires:         R-splines 
Requires:         R-CRAN-Hmisc 

%description
Shared parameter models for the joint modeling of longitudinal and
time-to-event data using MCMC; Dimitris Rizopoulos (2016)
<doi:10.18637/jss.v072.i07>.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/shiny_app_JM
%doc %{rlibdir}/%{packname}/shiny_app_lme
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
