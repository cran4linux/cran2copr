%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  llamaR
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Interface for Large Language Models via 'llama.cpp'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-ggmlR 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggmlR 
Requires:         R-CRAN-jsonlite 
Requires:         R-utils 

%description
Provides 'R' bindings to 'llama.cpp' for running Large Language Models
('LLMs') locally with optional 'Vulkan' GPU acceleration via 'ggmlR'.
Supports model loading, text generation, 'tokenization', token-to-piece
conversion, 'embeddings' (single and batch), encoder-decoder inference,
low-level batch management, chat templates, 'LoRA' adapters, explicit
backend/device selection, multi-GPU split, and 'NUMA' optimization.
Includes a high-level 'ragnar'-compatible embedding provider
('embed_llamar'). Built on top of 'ggmlR' for efficient tensor operations.

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
