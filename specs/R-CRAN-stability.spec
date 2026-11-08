%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stability
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Genotype-by-Environment Interaction and Yield Stability Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-grDevices 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 

%description
Analyses multi-environment trials of plant breeding, laid out in
randomized complete blocks in every environment, to find genotypes that
are high-yielding and stable: analyses of variance in each environment and
combined; Eberhart and Russell's analysis (1966)
<doi:10.2135/cropsci1966.0011183X000600010011x> and Finlay and Wilkinson's
regression (1963) <doi:10.1071/AR9630742>; Wricke's ecovalence, Shukla's
stability variance (1972) <doi:10.1038/hdy.1972.87> and Kang and Pham's
yield-stability statistic (1991)
<doi:10.2134/agronj1991.00021962008300010037x>; Kang's rank-sum and Fox's
top-third ranking; Eskridge's safety-first indices (1990), Annicchiarico's
reliability index (1992), Lin and Binns' superiority measure (1988) and
Huehn's nonparametric statistics (1979) with tests; additive main effects
and multiplicative interaction (AMMI) analysis with biplots and AMMI
stability values on any number of axes; the GGE biplot with
which-won-where, mean-stability and discrimination views in three
scalings; and a plain-language interpretation of every result, computed
from its numbers.

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
