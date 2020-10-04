%global packname  unine
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Unine Light Stemmer

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-methods 

%description
Implementation of "light" stemmers for French, German, Italian, Spanish,
Portuguese, Finnish, Swedish. They are based on the same work as the
"light" stemmers found in 'SolR' <https://lucene.apache.org/solr/> or
'ElasticSearch' <https://www.elastic.co/fr/products/elasticsearch>. A
"light" stemmer consists in removing inflections only for noun and
adjectives. Indexing verbs for these languages is not of primary
importance compared to nouns and adjectives. The stemming procedure for
French is described in (Savoy, 1999)
<doi:10.1002/(SICI)1097-4571(1999)50:10%3C944::AID-ASI9%3E3.3.CO;2-H>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
