%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcmdrPlugin.temis
%global packver   0.7.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.12
Release:          1%{?dist}%{?buildtag}
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
BuildRequires:    R-CRAN-lattice 
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
Requires:         R-CRAN-lattice 
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
imported from spreadsheet-like files, directories of raw text files, as
well as from 'Dow Jones Factiva', 'LexisNexis', 'Europresse' and 'Alceste'
files.

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
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
