%global packname  bhm
%global packver   1.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.15
Release:          1%{?dist}
Summary:          Biomarker Threshold Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-MASS 
BuildRequires:    R-survival 
BuildRequires:    R-methods 
Requires:         R-CRAN-coda 
Requires:         R-MASS 
Requires:         R-survival 
Requires:         R-methods 

%description
Contains tools to fit both predictive and prognostic biomarker effects
using biomarker threshold models. Evaluate the treatment effect, biomarker
effect and treatment-biomarker interaction using probability index
measurement. Test for treatment-biomarker interaction using residual
bootstrap method.

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
