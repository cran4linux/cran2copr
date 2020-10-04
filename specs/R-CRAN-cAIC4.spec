%global packname  cAIC4
%global packver   0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9
Release:          3%{?dist}%{?buildtag}
Summary:          Conditional Akaike Information Criterion for 'lme4' and 'nlme'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.1.6
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats4 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-RLRsim 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-lme4 >= 1.1.6
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-stats4 
Requires:         R-nlme 
Requires:         R-CRAN-RLRsim 
Requires:         R-mgcv 
Requires:         R-CRAN-mvtnorm 

%description
Provides functions for the estimation of the conditional Akaike
information in generalized mixed-effect models fitted with (g)lmer() from
'lme4', lme() from 'nlme' and gamm() from 'mgcv'.

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
