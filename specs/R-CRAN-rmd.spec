%global packname  rmd
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Easily Install and Load the R Markdown Family

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shinyjs >= 0.6
BuildRequires:    R-CRAN-rappdirs >= 0.3.1
BuildRequires:    R-CRAN-rvest >= 0.3.1
BuildRequires:    R-CRAN-shiny >= 0.13.2
BuildRequires:    R-CRAN-xml2 >= 0.1.2
BuildRequires:    R-CRAN-DT >= 0.1
BuildRequires:    R-CRAN-miniUI >= 0.1
BuildRequires:    R-CRAN-blogdown 
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-bookdownplus 
BuildRequires:    R-CRAN-citr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mindr 
BuildRequires:    R-CRAN-pagedown 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-rticles 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tinytex 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xaringan 
Requires:         R-CRAN-shinyjs >= 0.6
Requires:         R-CRAN-rappdirs >= 0.3.1
Requires:         R-CRAN-rvest >= 0.3.1
Requires:         R-CRAN-shiny >= 0.13.2
Requires:         R-CRAN-xml2 >= 0.1.2
Requires:         R-CRAN-DT >= 0.1
Requires:         R-CRAN-miniUI >= 0.1
Requires:         R-CRAN-blogdown 
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-bookdownplus 
Requires:         R-CRAN-citr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-dplyr 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mindr 
Requires:         R-CRAN-pagedown 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-rticles 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tinytex 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-xaringan 

%description
The 'rmd' package manages multiple R markdown packages. These R markdown
packages include currently 'rmarkdown', 'knitr', 'bookdown',
'bookdownplus', 'blogdown', 'rticles', 'tinytex', 'xaringan', 'citr', and
'mindr'. They can be installed and loaded in a single step with the 'rmd'
package. The conflicts between these packages are evaluated as well.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/gadgets
%doc %{rlibdir}/%{packname}/media
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
