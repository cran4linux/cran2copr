%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pangoling
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Access to Large Language Model Predictions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidytable >= 0.7.2
BuildRequires:    R-CRAN-cachem 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
Requires:         R-CRAN-tidytable >= 0.7.2
Requires:         R-CRAN-cachem 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-rstudioapi 
Requires:         R-stats 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 

%description
Provides access to word predictability estimates using large language
models (LLMs) based on 'transformer' architectures via integration with
the 'Hugging Face' ecosystem <https://huggingface.co/>. The package
interfaces with pre-trained neural networks and supports both
causal/auto-regressive LLMs (e.g., 'GPT-2') and masked/bidirectional LLMs
(e.g., 'BERT') to compute the probability of words, phrases, or tokens
given their linguistic context. For details on GPT-2 and causal models,
see Radford et al. (2019)
<https://storage.prod.researchhub.com/uploads/papers/2020/06/01/language-models.pdf>,
for details on BERT and masked models, see Devlin et al. (2019)
<doi:10.48550/arXiv.1810.04805>. By enabling a straightforward estimation
of word predictability, the package facilitates research in
psycholinguistics, computational linguistics, and natural language
processing (NLP).

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
