%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rUM
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Templates from the University of Miami

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtsummary >= 2.0.3
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-conflicted 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-quarto 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-table1 
BuildRequires:    R-CRAN-tidymodels 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-usethis 
Requires:         R-CRAN-gtsummary >= 2.0.3
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-conflicted 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-here 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-quarto 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-table1 
Requires:         R-CRAN-tidymodels 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-usethis 

%description
This holds r markdown and quarto templates for academic papers and slide
decks. It also has templates to create research projects which contain
academic papers as vignettes.

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
