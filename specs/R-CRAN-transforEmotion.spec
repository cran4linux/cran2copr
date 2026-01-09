%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  transforEmotion
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Sentiment Analysis for Text, Image and Video using Transformer Models

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-googledrive 
BuildRequires:    R-CRAN-LSAfun 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-textdata 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-googledrive 
Requires:         R-CRAN-LSAfun 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-textdata 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-httr 

%description
Implements sentiment analysis using huggingface <https://huggingface.co>
transformer zero-shot classification model pipelines for text and image
data. The default text pipeline is Cross-Encoder's DistilRoBERTa
<https://huggingface.co/cross-encoder/nli-distilroberta-base> and default
image/video pipeline is Open AI's CLIP
<https://huggingface.co/openai/clip-vit-base-patch32>. All other zero-shot
classification model pipelines can be implemented using their model name
from
<https://huggingface.co/models?pipeline_tag=zero-shot-classification>.

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
