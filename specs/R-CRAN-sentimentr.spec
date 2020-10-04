%global packname  sentimentr
%global packver   2.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.1
Release:          3%{?dist}%{?buildtag}
Summary:          Calculate Text Polarity Sentiment

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-textshape >= 1.3.0
BuildRequires:    R-CRAN-lexicon >= 1.2.1
BuildRequires:    R-CRAN-textclean >= 0.6.1
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-syuzhet 
BuildRequires:    R-utils 
Requires:         R-CRAN-textshape >= 1.3.0
Requires:         R-CRAN-lexicon >= 1.2.1
Requires:         R-CRAN-textclean >= 0.6.1
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-syuzhet 
Requires:         R-utils 

%description
Calculate text polarity sentiment at the sentence level and optionally
aggregate by rows or grouping variable(s).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/sentiment_testing
%doc %{rlibdir}/%{packname}/sfp
%doc %{rlibdir}/%{packname}/the_case_for_sentimentr
%{rlibdir}/%{packname}/INDEX
