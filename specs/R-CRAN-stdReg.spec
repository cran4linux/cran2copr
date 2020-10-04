%global packname  stdReg
%global packver   3.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Regression Standardization

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-drgee 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-survival 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-drgee 

%description
Contains functionality for regression standardization. Four general
classes of models are allowed; generalized linear models, conditional
generalized estimating equation models, Cox proportional hazards models
and shared frailty gamma-Weibull models. Sjolander, A. (2016)
<doi:10.1007/s10654-016-0157-3>.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
