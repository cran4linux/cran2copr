%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dragonfarm
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Fine-Tune Small Language Models with LoRA from R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.8.0
BuildRequires:    R-CRAN-reticulate >= 1.41.0
BuildRequires:    R-CRAN-bslib >= 0.6.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-ps 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sortable 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-shiny >= 1.8.0
Requires:         R-CRAN-reticulate >= 1.41.0
Requires:         R-CRAN-bslib >= 0.6.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-ps 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sortable 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-zip 

%description
Fine-tune small (100M to 3B parameter) causal language models with LoRA
(Low-Rank Adaptation) from R. Datasets are mapped to chat-format prompts
and responses, training runs in a background 'Python' process built on
Hugging Face 'transformers' and 'peft', and a 'shiny' app offers
drag-and-drop dataset upload and column mapping. 'Python' dependencies are
declared through 'reticulate' and resolved automatically on first use.

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
