%global packname  splm
%global packver   1.4-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.11
Release:          3%{?dist}
Summary:          Econometric Models for Spatial Panel Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-bdsmatrix 
BuildRequires:    R-CRAN-ibdreg 
BuildRequires:    R-nlme 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-methods 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-maxLik 
Requires:         R-MASS 
Requires:         R-CRAN-bdsmatrix 
Requires:         R-CRAN-ibdreg 
Requires:         R-nlme 
Requires:         R-Matrix 
Requires:         R-CRAN-spam 
Requires:         R-methods 

%description
ML and GM estimation and diagnostic testing of econometric models for
spatial panel data.

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
