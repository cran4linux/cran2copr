%global packname  fishmethods
%global packver   1.11-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11.1
Release:          2%{?dist}
Summary:          Fishery Science Methods and Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7.0
Requires:         R-core >= 2.7.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-MASS 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-bootstrap 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-MASS 
Requires:         R-boot 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-bootstrap 
Requires:         R-CRAN-numDeriv 

%description
Functions for applying a wide range of fisheries stock assessment methods.

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
