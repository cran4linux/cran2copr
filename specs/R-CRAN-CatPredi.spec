%global packname  CatPredi
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Optimal Categorisation of Continuous Variables in PredictionModels

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-CPE 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-mgcv 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-survival 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-CPE 
Requires:         R-CRAN-rgenoud 
Requires:         R-mgcv 
Requires:         R-stats 
Requires:         R-graphics 

%description
Allows the user to categorise a continuous predictor variable in a
logistic or a Cox proportional hazards regression setting, by maximising
the discriminative ability of the model. I Barrio, I Arostegui, MX
Rodriguez-Alvarez, JM Quintana (2015) <doi:10.1177/0962280215601873>. I
Barrio, MX Rodriguez-Alvarez, L Meira-Machado, C Esteban, I Arostegui
(2017) <https://www.idescat.cat/sort/sort411/41.1.3.barrio-etal.pdf>.

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
