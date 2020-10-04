%global packname  meanr
%global packver   0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Sentiment Analysis Scorer

License:          BSD 2-clause License + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0

%description
Sentiment analysis is a popular technique in text mining that attempts to
determine the emotional state of some text. We provide a new
implementation of a common method for computing sentiment, whereby words
are scored as positive or negative according to a dictionary lookup. Then
the sum of those scores is returned for the document. We use the 'Hu' and
'Liu' sentiment dictionary ('Hu' and 'Liu', 2004)
<doi:10.1145/1014052.1014073> for determining sentiment. The scoring
function is 'vectorized' by document, and scores for multiple documents
are computed in parallel via 'OpenMP'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/sexputils
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
