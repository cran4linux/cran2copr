%global __brp_check_rpaths %{nil}
%global packname  tm.plugin.lexisnexis
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Import Articles from 'LexisNexis' Using the 'tm' Text MiningFramework

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tm >= 0.6
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-NLP 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-ISOcodes 
Requires:         R-CRAN-tm >= 0.6
Requires:         R-utils 
Requires:         R-CRAN-NLP 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-ISOcodes 

%description
Provides a 'tm' Source to create corpora from articles exported from the
'LexisNexis' content provider as HTML files. It is able to read both text
content and meta-data information (including source, date, title, author
and pages). Note that the file format is highly unstable: there is no
warranty that this package will work for your corpus, and you may have to
adjust the code to adapt it to your particular format.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
