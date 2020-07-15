%global packname  journalabbr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Journal Abbreviations for BibTeX Documents

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-bib2df 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-bib2df 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-httr 

%description
Since the reference management software (such as 'Zotero', 'Mendeley')
exports Bib file journal abbreviation is not detailed enough, the
'journalabbr' package only abbreviates the journal field of Bib file, and
then outputs a new Bib file for generating reference format with journal
abbreviation on other software (such as 'texstudio'). The abbreviation
table is from 'JabRef'.

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
