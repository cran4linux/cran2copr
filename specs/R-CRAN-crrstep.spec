%global __brp_check_rpaths %{nil}
%global packname  crrstep
%global packver   2015-2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2015.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Stepwise Covariate Selection for the Fine & Gray Competing RisksRegression Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cmprsk 
Requires:         R-CRAN-cmprsk 

%description
Performs forward and backwards stepwise regression for the Proportional
subdistribution hazards model in competing risks (Fine & Gray 1999).
Procedure uses AIC, BIC and BICcr as selection criteria. BICcr has a
penalty of k = log(n*), where n* is the number of primary events.

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
