%global packname  risksetROC
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Riskset ROC curve estimation from censored survival data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.6.1
Requires:         R-core >= 1.6.1
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-MASS 
Requires:         R-survival 
Requires:         R-MASS 

%description
Compute time-dependent Incident/dynamic accuracy measures (ROC curve, AUC,
integrated AUC )from censored survival data under proportional or
non-proportional hazard assumption of Heagerty & Zheng (Biometrics, Vol 61
No 1, 2005, PP 92-105).

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
