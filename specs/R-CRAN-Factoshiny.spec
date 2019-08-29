%global packname  Factoshiny
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          Perform Factorial Analysis from 'FactoMineR' with a ShinyApplication

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-shiny 

%description
Perform factorial analysis with a menu and draw graphs interactively
thanks to 'FactoMineR' and a Shiny application.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/FactoCAapp2
%doc %{rlibdir}/%{packname}/FactoFAMDapp2
%doc %{rlibdir}/%{packname}/FactoHCPCapp2
%doc %{rlibdir}/%{packname}/FactoHCPCappdf2
%doc %{rlibdir}/%{packname}/FactoMCAapp2
%doc %{rlibdir}/%{packname}/FactoMFAapp
%doc %{rlibdir}/%{packname}/FactoMFAapp2
%doc %{rlibdir}/%{packname}/FactoPCAapp2
%doc %{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/INDEX
