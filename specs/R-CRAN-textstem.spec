%global packname  textstem
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Stemming and Lemmatizing Text

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quanteda >= 0.99.12
BuildRequires:    R-CRAN-lexicon >= 0.4.1
BuildRequires:    R-CRAN-koRpus.lang.en 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-hunspell 
BuildRequires:    R-CRAN-koRpus 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-textclean 
BuildRequires:    R-CRAN-textshape 
BuildRequires:    R-utils 
Requires:         R-CRAN-quanteda >= 0.99.12
Requires:         R-CRAN-lexicon >= 0.4.1
Requires:         R-CRAN-koRpus.lang.en 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-hunspell 
Requires:         R-CRAN-koRpus 
Requires:         R-CRAN-SnowballC 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-textclean 
Requires:         R-CRAN-textshape 
Requires:         R-utils 

%description
Tools that stem and lemmatize text.  Stemming is a process that removes
endings such as affixes.  Lemmatization is the process of grouping
inflected forms together as a single base form.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
