%global packname  MIICD
%global packver   2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4
Release:          1%{?dist}
Summary:          Multiple Imputation for Interval Censored Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mstate 
Requires:         R-survival 
Requires:         R-MASS 
Requires:         R-CRAN-mstate 

%description
Implements multiple imputation for proportional hazards regression with
interval censored data or proportional sub-distribution hazards regression
for interval censored competing risks data. The main functions allow to
estimate survival function, cumulative incidence function, Cox and Fine &
Gray regression coefficients and associated variance-covariance matrix.
'MIICD' functions call 'Surv', 'survfit' and 'coxph' from the 'survival'
package, 'crprep' from the 'mstate' package, and 'mvrnorm' from the 'MASS'
package.

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
%{rlibdir}/%{packname}/INDEX
