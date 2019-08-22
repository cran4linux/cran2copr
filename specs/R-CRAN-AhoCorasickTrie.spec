%global packname  AhoCorasickTrie
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Fast Searching for Multiple Keywords in Multiple Texts

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-Rcpp >= 0.12.5

%description
Aho-Corasick is an optimal algorithm for finding many keywords in a text.
It can locate all matches in a text in O(N+M) time; i.e., the time needed
scales linearly with the number of keywords (N) and the size of the text
(M). Compare this to the naive approach which takes O(N*M) time to loop
through each pattern and scan for it in the text. This implementation
builds the trie (the generic name of the data structure) and runs the
search in a single function call. If you want to search multiple texts
with the same trie, the function will take a list or vector of texts and
return a list of matches to each text. By default, all 128 ASCII
characters are allowed in both the keywords and the text. A more efficient
trie is possible if the alphabet size can be reduced. For example, DNA
sequences use at most 19 distinct characters and usually only 4; protein
sequences use at most 26 distinct characters and usually only 20. UTF-8
(Unicode) matching is not currently supported.

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
%{rlibdir}/%{packname}/libs
