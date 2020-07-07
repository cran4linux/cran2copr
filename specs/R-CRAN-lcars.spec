%global packname  lcars
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}
Summary:          LCARS Aesthetic for Shiny

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-trekcolors 
Requires:         R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-trekcolors 

%description
Provides Shiny widgets and theme that support a 'Library Computer
Access/Retrieval System' (LCARS) aesthetic for Shiny apps. The package
also includes functions for adding a minimal LCARS theme to static
'ggplot2' graphs. More details about LCARS can be found at
<https://en.wikipedia.org/wiki/LCARS>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny
%doc %{rlibdir}/%{packname}/stlogo-white.png
%doc %{rlibdir}/%{packname}/WORDLIST
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
