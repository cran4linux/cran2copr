%global packname  ruimtehol
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Learn Text 'Embeddings' with 'Starspace'

License:          MPL-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 

%description
Wraps the 'StarSpace' library
<https://github.com/facebookresearch/StarSpace> allowing users to
calculate word, sentence, article, document, webpage, link and entity
'embeddings'. By using the 'embeddings', you can perform text based
multi-label classification, find similarities between texts and
categories, do collaborative-filtering based recommendation as well as
content-based recommendation, find out relations between entities,
calculate graph 'embeddings' as well as perform semi-supervised learning
and multi-task learning on plain text. The techniques are explained in
detail in the paper: 'StarSpace: Embed All The Things!' by Wu et al.
(2017), available at <arXiv:1709.03856>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/PATENTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
