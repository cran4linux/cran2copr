%global packname  ymlthis
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Write 'YAML' for 'R Markdown', 'bookdown', 'blogdown', and More

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-usethis >= 1.5.0
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-whoami 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-usethis >= 1.5.0
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-whoami 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-yaml 

%description
Write 'YAML' front matter for R Markdown and related documents. yml_*()
functions write 'YAML' and use_*() functions let you write the resulting
'YAML' to your clipboard or to .yml files related to your project.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/addin
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
