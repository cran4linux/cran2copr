%global packname  RcmdrPlugin.temis
%global packver   0.7.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.10
Release:          3%{?dist}%{?buildtag}
Summary:          Graphical Integrated Text Mining Solution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R2HTML >= 2.3.0
BuildRequires:    R-CRAN-Rcmdr >= 2.1.1
BuildRequires:    R-CRAN-tm >= 0.6
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-NLP 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-lattice 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ca 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-R2HTML >= 2.3.0
Requires:         R-CRAN-Rcmdr >= 2.1.1
Requires:         R-CRAN-tm >= 0.6
Requires:         R-methods 
Requires:         R-CRAN-NLP 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-zoo 
Requires:         R-lattice 
Requires:         R-tcltk 
Requires:         R-CRAN-tcltk2 
Requires:         R-utils 
Requires:         R-CRAN-ca 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-stringi 

%description
An 'R Commander' plug-in providing an integrated solution to perform a
series of text mining tasks such as importing and cleaning a corpus, and
analyses like terms and documents counts, vocabulary tables, terms
co-occurrences and documents similarity measures, time series analysis,
correspondence analysis and hierarchical clustering. Corpora can be
imported from spreadsheet-like files, directories of raw text files,
'Twitter' queries, as well as from 'Dow Jones Factiva', 'LexisNexis',
'Europresse' and 'Alceste' files.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/INDEX
