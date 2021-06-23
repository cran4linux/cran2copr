%global __brp_check_rpaths %{nil}
%global packname  PubMedWordcloud
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          3%{?dist}%{?buildtag}
Summary:          'Pubmed' Word Clouds

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-RColorBrewer 

%description
Create a word cloud using the abstract of publications from 'Pubmed'.

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
%{rlibdir}/%{packname}/INDEX
