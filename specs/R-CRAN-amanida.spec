%global __brp_check_rpaths %{nil}
%global packname  amanida
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Meta-Analysis for Non-Integral Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.6.0
BuildRequires:    R-stats >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-rmarkdown >= 2.9
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-knitr >= 1.33
BuildRequires:    R-CRAN-kableExtra >= 1.3.0
BuildRequires:    R-CRAN-tidyverse >= 1.3.0
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-webchem >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-readr >= 1.0.0
BuildRequires:    R-CRAN-readxl >= 1.0.0
BuildRequires:    R-CRAN-ggrepel >= 0.9.0
Requires:         R-methods >= 3.6.0
Requires:         R-stats >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-rmarkdown >= 2.9
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-knitr >= 1.33
Requires:         R-CRAN-kableExtra >= 1.3.0
Requires:         R-CRAN-tidyverse >= 1.3.0
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-webchem >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-readr >= 1.0.0
Requires:         R-CRAN-readxl >= 1.0.0
Requires:         R-CRAN-ggrepel >= 0.9.0

%description
Combination of results for meta-analysis using significance and effect
size only. P-values and fold-change are combined to obtain a global
significance on each metabolite. Produces a volcano plot summarising the
relevant results from meta-analysis. Vote-counting reports for
metabolites. And explore plot to detect discrepancies between studies at a
first glance. Methodology is described in the Llambrich et al. (2021)
<doi:10.1093/bioinformatics/btab591>.

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
