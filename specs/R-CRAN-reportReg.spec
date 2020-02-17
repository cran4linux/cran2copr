%global packname  reportReg
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          An Easy Way to Report Regression Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-nlme 
Requires:         R-nlme 

%description
Provides an easy way to report the results of regression analysis,
including: 1. Proportional hazards regression from function 'coxph' of
package 'survival'; 2. Conditional logistic regression from function
'clogit' of package 'survival'; 3. Ordered logistic regression from
function 'polr' of package 'MASS'; 4. Binary logistic regression from
function 'glm' of package 'stats'; 5. Linear regression from function 'lm'
of package 'stats'; 6. Risk regression model for survival analysis with
competing risks from function 'FGR' of package 'riskRegression'; 7.
Multilevel model from function 'lme' of package 'nlme'.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
