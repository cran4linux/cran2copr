%global packname  sparkxgb
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Interface for 'XGBoost' on 'Apache Spark'

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-sparklyr >= 1.0
BuildRequires:    R-CRAN-forge >= 0.2.0
Requires:         R-CRAN-sparklyr >= 1.0
Requires:         R-CRAN-forge >= 0.2.0

%description
A 'sparklyr' <https://spark.rstudio.com/> extension that provides an
interface for 'XGBoost' <https://github.com/dmlc/xgboost> on 'Apache
Spark'. 'XGBoost' is an optimized distributed gradient boosting library.

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
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/sparkml
%{rlibdir}/%{packname}/INDEX
