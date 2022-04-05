%global __brp_check_rpaths %{nil}
%global packname  transforEmotion
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sentiment Analysis for Text and Qualitative Data

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-osfr 
BuildRequires:    R-CRAN-LSAfun 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-remotes 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-osfr 
Requires:         R-CRAN-LSAfun 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-remotes 

%description
Implements sentiment analysis using huggingface <https://huggingface.co>
transformer zero-shot classification model pipelines. The default pipeline
is Cross-Encoder's DistilRoBERTa
<https://huggingface.co/cross-encoder/nli-distilroberta-base> trained on
the Stanford Natural Language Inference
<https://nlp.stanford.edu/projects/snli/> and Multi-Genre Natural Language
Inference <https://huggingface.co/datasets/multi_nli> datasets. Using
similar models, zero-shot classification transformers have demonstrated
superior performance relative to other natural language processing models
<arXiv:1909.00161>. All other zero-shot classification model pipelines can
be implemented using their model name from
<https://huggingface.co/models?pipeline_tag=zero-shot-classification>}.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
