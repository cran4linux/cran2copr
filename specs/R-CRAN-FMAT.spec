%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FMAT
%global packver   2023.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2023.8
Release:          1%{?dist}%{?buildtag}
Summary:          The Fill-Mask Association Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-PsychWordVec 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-text 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-PsychWordVec 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-text 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 

%description
The Fill-Mask Association Test ('FMAT') is an integrative, versatile, and
probability-based method that uses Masked Language Models to measure
conceptual associations or relations (e.g., attitudes, biases,
stereotypes, social norms, cultural values) as propositional
representations in natural language. The supported language models include
'BERT' (Devlin et al., 2018) <arXiv:1810.04805> and its model variants
available at 'Hugging Face'
<https://huggingface.co/models?pipeline_tag=fill-mask>. 'Python' ('conda')
environment and the 'transformers' module can be installed automatically
using the FMAT_load() function. Methodological references and technical
details are provided at <https://psychbruce.github.io/FMAT/>.

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
