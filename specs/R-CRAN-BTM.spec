%global packname  BTM
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          Biterm Topic Models for Short Text

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 

%description
Biterm Topic Models find topics in collections of short texts. It is a
word co-occurrence based topic model that learns topics by modeling
word-word co-occurrences patterns which are called biterms. This in
contrast to traditional topic models like Latent Dirichlet Allocation and
Probabilistic Latent Semantic Analysis which are word-document
co-occurrence topic models. A biterm consists of two words co-occurring in
the same short text window. This context window can for example be a
twitter message, a short answer on a survey, a sentence of a text or a
document identifier. The techniques are explained in detail in the paper
'A Biterm Topic Model For Short Text' by Xiaohui Yan, Jiafeng Guo, Yanyan
Lan, Xueqi Cheng (2013)
<https://github.com/xiaohuiyan/xiaohuiyan.github.io/blob/master/paper/BTM-WWW13.pdf>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
