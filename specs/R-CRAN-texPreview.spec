%global packname  texPreview
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          Compile and Preview Snippets of 'LaTeX' in 'RStudio'

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-svgPanZoom 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-rematch2 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-svgPanZoom 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-rematch2 

%description
Compile and preview snippets of 'LaTeX'. Can be used directly from the R
console, from 'RStudio', in Shiny apps and R Markdown documents. Must have
'pdflatex' or 'xelatex' or 'lualatex' in 'PATH'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/tmpl.tex
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
