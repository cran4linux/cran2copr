%global packname  journalabbr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Journal Abbreviations for BibTeX Documents

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-shiny 

%description
Since the reference management software (such as 'Zotero', 'Mendeley')
exports Bib file journal abbreviation is not detailed enough, the
'journalabbr' package only abbreviates the journal field of Bib file, and
then outputs a new Bib file for generating reference format with journal
abbreviation on other software (such as 'texstudio'). The abbreviation
table is from 'JabRef'. At the same time, 'Shiny' application is provided
to generate 'thebibliography', a reference format that can be directly
used for latex paper writing based on 'Rmd' files.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
