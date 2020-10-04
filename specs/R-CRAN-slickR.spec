%global packname  slickR
%global packver   0.4.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.9
Release:          3%{?dist}%{?buildtag}
Summary:          Create Interactive Carousels with the JavaScript 'Slick' Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-htmlwidgets 
Requires:         R-CRAN-htmltools 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-lifecycle 
Requires:         R-stats 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-htmlwidgets 

%description
Create and customize interactive carousels using the 'Slick' JavaScript
library and the 'htmlwidgets' package. The carousels can contain plots
produced in R, images, 'iframes', videos and other 'htmlwidgets'.  These
carousels can be created directly from the R console, and viewed in the
'RStudio' internal viewer, in Shiny apps and R Markdown documents.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
