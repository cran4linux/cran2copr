%global packname  emax.glm
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          General Tools for Building GLM Expectation-Maximization Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-AER 
Requires:         R-MASS 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-AER 

%description
Implementation of Expectation Maximization (EM) regression of general
linear models. The package currently supports Poisson and Logistic
regression with variable weights, with underlying theory included in the
vignettes. New users are recommended to look at the em.glm() and
small.em() functions - the outputs of which are supported by AIC(), BIC(),
and logLik() calls. Several plot functions have been included for useful
diagnostics and model exploration. Methods are based on the theory of
Dempster et al (1977, ISBN:00359246), and follow the methods of Hastie et
al. (2009) <doi:10.1007/978-0-387-21606-5_7> and A. Zeileis et al (2017)
<doi:10.18637/jss.v027.i08>.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
