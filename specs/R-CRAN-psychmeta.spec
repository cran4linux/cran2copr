%global packname  psychmeta
%global packver   2.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Psychometric Meta-Analysis Toolkit

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-data.table 

%description
Tools for computing bare-bones and psychometric meta-analyses and for
generating psychometric data for use in meta-analysis simulations.
Supports bare-bones, individual-correction, and artifact-distribution
methods for meta-analyzing correlations and d values. Includes tools for
converting effect sizes, computing sporadic artifact corrections,
reshaping meta-analytic databases, computing multivariate corrections for
range variation, and more. Bugs can be reported to
<https://github.com/psychmeta/psychmeta/issues> or <issues@psychmeta.com>.

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
