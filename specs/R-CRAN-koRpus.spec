%global packname  koRpus
%global packver   0.11-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.5
Release:          3%{?dist}
Summary:          An R Package for Text Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sylly >= 0.1.4
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
Requires:         R-CRAN-sylly >= 0.1.4
Requires:         R-CRAN-data.table 
Requires:         R-methods 

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
repository <https://undocumeantit.github.io/repos/l10n>. 'koRpus' also
includes a plugin for the R GUI and IDE RKWard, providing graphical
dialogs for its basic features. The respective R package 'rkward' cannot
be installed directly from a repository, as it is a part of RKWard. To
make full use of this feature, please install RKWard from
<https://rkward.kde.org> (plugins are detected automatically). Due to some
restrictions on CRAN, the full package sources are only available from the
project homepage. To ask for help, report bugs, request features, or
discuss the development of the package, please subscribe to the koRpus-dev
mailing list (<http://korpusml.reaktanz.de>).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/README.languages
%doc %{rlibdir}/%{packname}/rkward
%doc %{rlibdir}/%{packname}/shiny
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
