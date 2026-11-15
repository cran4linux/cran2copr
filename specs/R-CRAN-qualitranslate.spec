%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qualitranslate
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Translation Workflow for Qualitative Interview Transcripts

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-later 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-promises 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-zip 

%description
A local browser workspace for translating qualitative interview
transcripts in research. Transcript sections are translated in batches by
forward translation, then by a blind back-translation whose request holds
only the forward translation (never the original, the study context, the
glossary or translator notes), and then by a reconciliation step that
compares all three texts, flags discrepancies by category and severity and
proposes a draft. Every draft needs a named human review decision before
it counts as reviewed. Each stage can be run by copying prompt packets
into any chat tool, including institutional chat services, or through the
'Mistral' or 'Anthropic' ('Claude') application programming interfaces.
Exports include reviewed translations, a parallel review table, the exact
prompts and replies, a hash-chained audit record and a draft methods
paragraph. Projects are interchangeable with the 'Python' version of the
tool.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
