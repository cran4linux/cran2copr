%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  relm
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Local Large Language Models as Base-R Objects

License:          MIT + file LICENSE | Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nanoarrow 
Requires:         R-methods 
Requires:         R-CRAN-nanoarrow 

%description
Load and run local large language models (through a vendored, patched
'llama.cpp') from R and work with them as plain data frames and matrices
in base-R idiom. Provides model loading and tokenization (llm(),
llm_tokens()), text generation (llm_generate()), next-token distributions
(llm_logits()), embeddings (llm_embed()), and mechanistic interpretability
tools -- activation tracing (llm_trace()), activation steering
(llm_steer()), neuron ablation (llm_ablate()), and grouped statistical
probes (llm_probe()). Vision-language models loaded with their projector
take image input in generation and embeddings. A checksum-verified
downloader (llm_download()) fetches pinned models.

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
