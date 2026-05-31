%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tmfast
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Topic Models Using Varimax

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-cli 

%description
Fits topic models using varimax-rotated principal component analysis
(PCA), following the "vintage factor analysis" approach of Rohe & Zheng
(2020) <doi:10.48550/arXiv.2004.05387>. Leverages truncated PCA via
'irlba' for sparse matrices, enabling fast model fitting on large corpora.
Includes an information-theoretic approach to vocabulary selection,
'broom'-compatible tidiers for extracting word-topic and topic-document
matrices into a tidy data workflow, and samplers for constructing
simulated corpora for benchmarking and method evaluation.

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
