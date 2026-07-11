%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  inferencer
%global packver   0.1.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Unified Wrappers for Hosted Foundation Model Inference APIs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 

%description
Provides lightweight R wrappers for querying and listing models from
several hosted foundation model inference platforms, currently including
Google Gemini, Groq, OpenRouter, Cerebras, and Ollama Cloud. The package
is designed for simple inference workflows and quick experimentation, with
minimal abstraction and a consistent interface across providers. It
includes helper functions for model discovery, text generation,
embeddings, image generation, and multimodal inputs, while leaving room
for future support of provider-specific parameters and advanced options.

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
