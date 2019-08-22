%global packname  antitrust
%global packver   0.99.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.11
Release:          1%{?dist}
Summary:          Tools for Antitrust Practitioners

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rhandsontable 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rhandsontable 

%description
A collection of tools for antitrust practitioners, including the ability
to calibrate different consumer demand systems and simulate the effects of
mergers under different competitive regimes.

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
%doc %{rlibdir}/%{packname}/antitrust_shiny
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
