%global packname  lazyrmd
%global packver   0.2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0.1
Release:          1%{?dist}
Summary:          Render R Markdown Outputs Lazily

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-htmltools 

%description
An R Markdown html document format that provides the ability to lazily
load plot outputs as the user scrolls over them.  This is useful for large
R Markdown documents with many plots, as it allows for a fast initial page
load and defers loading of individual graphics to the time that the user
navigates near them.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/deps
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
