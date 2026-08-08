%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  acR
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Content Analysis in R: Integrated Qualitative (LLMs) and Quantitative Pipeline

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-yaml 

%description
Provides an integrated pipeline for content analysis combining qualitative
coding assisted by large language models (LLMs) with classical
quantitative text analysis. Includes modules for pre-processing
(tokenization, stopwords for Brazilian Portuguese), descriptive
statistics, keyness, co-occurrence networks, word clouds (including
comparative and X-ray variants), sentiment analysis via OpLexicon, Latent
Dirichlet Allocation (LDA), inter-coder reliability metrics (Krippendorff,
Gwet), and modern visualizations based on ggplot2. Special focus on
Brazilian corpora and political-institutional codebooks. Inspired by Maerz
and Benoit (2025) <https://quallmer.github.io/quallmer/>.

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
