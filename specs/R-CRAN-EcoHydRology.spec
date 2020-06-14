%global packname  EcoHydRology
%global packver   0.4.12.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.12.1
Release:          2%{?dist}
Summary:          A Community Modeling Foundation for Eco-Hydrology

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-operators 
BuildRequires:    R-CRAN-topmodel 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-operators 
Requires:         R-CRAN-topmodel 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-XML 

%description
Provides a flexible foundation for scientists, engineers, and policy
makers to base teaching exercises as well as for more applied use to model
complex eco-hydrological interactions.

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
