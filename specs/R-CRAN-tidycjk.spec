%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidycjk
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Tools for Chinese, Japanese and Korean Text

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
A tidy toolkit for text that is written in Chinese, Japanese or Korean.
Most text tooling in R assumes that words are separated by whitespace,
which CJK writing does not use, so ordinary summaries of a text column
either treat a sentence as one undifferentiated blob or split it into
isolated characters. Word segmentation is therefore a pluggable engine
that the caller names explicitly rather than a bundled dictionary, because
where a word ends is a fact about a language and not about Unicode.
'tidycjk' classifies characters by Unicode block, reports which script and
which language a text is written in, measures how much of a text is CJK,
and turns those measurements into tibbles that slot straight into a
'tidyverse' workflow. It also measures display width in terminal columns,
pads and truncates to a width rather than to a character count, and
normalises fullwidth and halfwidth forms surgically -- including composing
halfwidth katakana voiced marks into single code points -- without the
collateral damage of a full 'NFKC' pass. Language detection deliberately
returns NA rather than guessing when a text is written in Han characters
only, because Japanese written without kana cannot be distinguished from
Chinese by script alone. Everything is derived from the Unicode
specification; the package makes no network requests and needs no compiled
code of its own.

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
