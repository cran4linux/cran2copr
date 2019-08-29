%global packname  linguisticsdown
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Easy Linguistics Document Writing with R Markdown

License:          MIT + file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-DT 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-DT 

%description
Provides 'Shiny gadgets' to search, type, and insert IPA symbols into
documents or scripts, requiring only knowledge about phonetics or
'X-SAMPA'. Also provides functions to facilitate the rendering of IPA
symbols in 'LaTeX' and PDF format, making IPA symbols properly rendered in
all output formats. A minimal R Markdown template for authoring
Linguistics related documents is also bundled with the package. Some
helper functions to facilitate authoring with R Markdown is also provided.

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
%license %{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/rmarkdown
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
