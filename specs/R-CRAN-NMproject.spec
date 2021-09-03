%global __brp_check_rpaths %{nil}
%global packname  NMproject
%global packver   0.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          Script Based 'NONMEM' Model Development

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-lifecycle >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.2
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-rlang >= 0.2.1
BuildRequires:    R-CRAN-git2r >= 0.18.0
BuildRequires:    R-CRAN-diffobj >= 0.1.11
BuildRequires:    R-CRAN-miniUI >= 0.1.1
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-usethis 
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-lifecycle >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.2
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-rlang >= 0.2.1
Requires:         R-CRAN-git2r >= 0.18.0
Requires:         R-CRAN-diffobj >= 0.1.11
Requires:         R-CRAN-miniUI >= 0.1.1
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-DT 
Requires:         R-methods 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rprojroot 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-usethis 

%description
Industrialisation of 'NONMEM' <https://www.iconplc.com/innovation/nonmem/>
via fully and rapidly reusable model development 'workflows' entirely
within 'RStudio'. Quickly get started with new models by importing
'NONMEM' templates from the built-in code library. Manipulate 'NONMEM'
code from within R either via the tracked 'manual edit' interface or
'programmatically' via convenience functions. Script 'workflows' by piping
sequences of model building steps from control file creation, to
execution, to post-processing and evaluation. Run caching makes
'workflows' R markdown friendly for easy documentation of thoughts and
modelling decisions alongside executable code. Share, reuse and recycle
'workflows' for new problems.

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
