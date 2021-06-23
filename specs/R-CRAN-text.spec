%global __brp_check_rpaths %{nil}
%global packname  text
%global packver   0.9.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.10
Release:          1%{?dist}%{?buildtag}
Summary:          Analyses of Text using Natural Language Processing and Machine Learning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.00
Requires:         R-core >= 4.00
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tokenizers 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-CRAN-workflows 
BuildRequires:    R-CRAN-yardstick 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tokenizers 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-tune 
Requires:         R-CRAN-workflows 
Requires:         R-CRAN-yardstick 
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 

%description
Transforms text variables to word embeddings; where the word embeddings
are used to statistically test the mean difference between set of texts,
compute semantic similarity scores between texts, predict numerical
variables, and visual statistically significant words according to various
dimensions etc. For more information see <https://www.r-text.org>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
