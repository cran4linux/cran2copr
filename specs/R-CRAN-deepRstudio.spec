%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deepRstudio
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Seamless Language Translation in 'RStudio' using 'DeepL' API and 'Rstudioapi'

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-crayon 

%description
Enhancing cross-language compatibility within the 'RStudio' environment
and supporting seamless language understanding, the 'deepRstudio' package
leverages the power of the 'DeepL' API (see
<https://www.deepl.com/docs-api>) to enable seamless, fast, accurate, and
affordable translation of code comments, documents, and text. This package
offers the ability to translate selected text into English (EN), as well
as from English into various languages, namely Japanese (JA), Chinese
(ZH), Spanish (ES), French (FR), Russian (RU), Portuguese (PT), and
Indonesian (ID). With much of the text being written in English, the
emphasis is on compatibility from English. It is also designed for
developers working on multilingual projects and data analysts
collaborating with international teams, simplifying the translation
process and making code more accessible and comprehensible to people with
diverse language backgrounds. This package uses the 'rstudioapi' package
and 'DeepL' API, and is simply implemented, executed from addins or via
shortcuts on 'RStudio'. With just a few steps, content can be translated
between supported languages, promoting better collaboration and expanding
the global reach of work. The functionality of this package works only on
'RStudio' using 'rstudioapi'.

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
