%global packname  HETOP
%global packver   0.2-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          3%{?dist}
Summary:          MLE and Bayesian Estimation of Heteroskedastic Ordered Probit(HETOP) Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
Requires:         R-CRAN-R2jags 
Requires:         R-splines 
Requires:         R-stats 

%description
Provides functions for maximum likelihood and Bayesian estimation of the
Heteroskedastic Ordered Probit (HETOP) model, using methods described in
Lockwood, Castellano and Shear (2018) <doi:10.3102/1076998618795124> and
Reardon, Shear, Castellano and Ho (2017) <doi:10.3102/1076998616666279>.
It also provides a general function to compute the triple-goal estimators
of Shen and Louis (1998) <doi:10.1111/1467-9868.00135>.

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
