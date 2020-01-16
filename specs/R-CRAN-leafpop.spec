%global packname  leafpop
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}
Summary:          Include Tables, Images and Graphs in Leaflet Pop-Ups

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-brew 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-svglite 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-brew 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-svglite 
Requires:         R-CRAN-uuid 

%description
Creates 'HTML' strings to embed tables, images or graphs in pop-ups of
interactive maps created with packages like 'leaflet' or 'mapview'.
Handles local images located on the file system or via remote URL. Handles
graphs created with 'lattice' or 'ggplot2' as well as interactive plots
created with 'htmlwidgets'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
