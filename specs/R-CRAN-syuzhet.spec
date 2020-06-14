%global packname  syuzhet
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          2%{?dist}
Summary:          Extracts Sentiment and Sentiment-Derived Plot Arcs from Text

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-textshape >= 1.3.0
BuildRequires:    R-CRAN-NLP 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-dtt 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-textshape >= 1.3.0
Requires:         R-CRAN-NLP 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-dtt 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 

%description
Extracts sentiment and sentiment-derived plot arcs from text using a
variety of sentiment dictionaries conveniently packaged for consumption by
R users.  Implemented dictionaries include "syuzhet" (default) developed
in the Nebraska Literary Lab "afinn" developed by Finn {AA}rup Nielsen,
"bing" developed by Minqing Hu and Bing Liu, and "nrc" developed by
Mohammad, Saif M. and Turney, Peter D. Applicable references are available
in README.md and in the documentation for the "get_sentiment" function.
The package also provides a hack for implementing Stanford's coreNLP
sentiment parser. The package provides several methods for plot arc
normalization.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
