%global packname  koRpus
%global packver   0.13-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.8
Release:          1%{?dist}%{?buildtag}
Summary:          Text Analysis with Emphasis on POS Tagging, Readability, and Lexical Diversity

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sylly >= 0.1.6
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-sylly >= 0.1.6
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 

%description
A set of tools to analyze texts. Includes, amongst others, functions for
automatic language detection, hyphenation, several indices of lexical
diversity (e.g., type token ratio, HD-D/vocd-D, MTLD) and readability
(e.g., Flesch, SMOG, LIX, Dale-Chall). Basic import functions for language
corpora are also provided, to enable frequency analyses (supports Celex
and Leipzig Corpora Collection file formats) and measures like tf-idf.
Note: For full functionality a local installation of TreeTagger is
recommended. It is also recommended to not load this package directly, but
by loading one of the available language support packages from the 'l10n'
repository <https://undocumeantit.github.io/repos/l10n/>. 'koRpus' also
includes a plugin for the R GUI and IDE RKWard, providing graphical
dialogs for its basic features. The respective R package 'rkward' cannot
be installed directly from a repository, as it is a part of RKWard. To
make full use of this feature, please install RKWard from
<https://rkward.kde.org> (plugins are detected automatically). Due to some
restrictions on CRAN, the full package sources are only available from the
project homepage. To ask for help, report bugs, request features, or
discuss the development of the package, please subscribe to the koRpus-dev
mailing list (<https://korpusml.reaktanz.de>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
