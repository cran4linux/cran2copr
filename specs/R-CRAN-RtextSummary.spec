%global packname  RtextSummary
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Summarizes Text by Extracting Relevant Sentences

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-mlapi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tokenizers 
BuildRequires:    R-CRAN-text2vec 
BuildRequires:    R-CRAN-Matrix.utils 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-mlapi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tokenizers 
Requires:         R-CRAN-text2vec 
Requires:         R-CRAN-Matrix.utils 
Requires:         R-CRAN-dplyr 

%description
Build a text summary by extracting relevant sentences from your text. The
training dataset should consist of several documents, each document should
have sentences separated by a period. While fitting the model, the 'term
frequency - inverse document frequency' (TF-IDF) matrix that reflects how
important a word is to a document is calculated first. Then vector
representations for words are obtained from the 'global vectors for word
representation' algorithm (GloVe). While applying the model on new data,
the GloVe word vectors for each word are weighted by their TF-IDF weights
and averaged to give a sentence vector or a document vector. The magnitude
of this sentence vector gives the importance of that sentence within the
document. Another way to obtain the importance of the sentence is to
calculate cosine similarity between the sentence vector and the document
vector. The output can either be at the sentence level (sentences and
weights are returned) or at a document level (the summary for each
document is returned). It is useful to first get a sentence level output
and get quantiles of the sentence weights to determine a cutoff threshold
for the weights. This threshold can then be used in the document level
output. This method is a variation of the TF-IDF extractive summarization
method mentioned in a review paper by Gupta (2010)
<doi:10.4304/jetwi.2.3.258-268>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
