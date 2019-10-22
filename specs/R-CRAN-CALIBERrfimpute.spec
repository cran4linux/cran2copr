%global packname  CALIBERrfimpute
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Multiple Imputation Using MICE and Random Forest

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mice >= 2.20
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-CRAN-mice >= 2.20
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-randomForest 

%description
Functions to impute using Random Forest under Full Conditional
Specifications (Multivariate Imputation by Chained Equations). The CALIBER
programme is funded by the Wellcome Trust (086091/Z/08/Z) and the National
Institute for Health Research (NIHR) under its Programme Grants for
Applied Research programme (RP-PG-0407-10314). The author is supported by
a Wellcome Trust Clinical Research Training Fellowship (0938/30/Z/10/Z).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
