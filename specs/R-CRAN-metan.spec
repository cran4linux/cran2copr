%global packname  metan
%global packver   1.11.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi Environment Trials Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggrepel 
Requires:         R-grid 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mathjaxr 
Requires:         R-methods 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Performs stability analysis of multi-environment trial data using
parametric and non-parametric methods. Parametric methods includes
Additive Main Effects and Multiplicative Interaction (AMMI) analysis by
Gauch (2013) <doi:10.2135/cropsci2013.04.0241>, Ecovalence by Wricke
(1965), Genotype plus Genotype-Environment (GGE) biplot analysis by Yan &
Kang (2003) <doi:10.1201/9781420040371>, geometric adaptability index by
Mohammadi & Amri (2008) <doi:10.1007/s10681-007-9600-6>, joint regression
analysis by Eberhart & Russel (1966)
<doi:10.2135/cropsci1966.0011183X000600010011x>, genotypic confidence
index by Annicchiarico (1992), Murakami & Cruz's (2004) method
<doi:10.12702/1984-7033.v04n01a02>, power law residuals (POLAR) statistics
by Doring et al. (2015) <doi:10.1016/j.fcr.2015.08.005>, scale-adjusted
coefficient of variation by Doring & Reckling (2018)
<doi:10.1016/j.eja.2018.06.007>, stability variance by Shukla (1972)
<doi:10.1038/hdy.1972.87>, weighted average of absolute scores by Olivoto
et al. (2019a) <doi:10.2134/agronj2019.03.0220>, and multi-trait stability
index by Olivoto et al. (2019b) <doi:10.2134/agronj2019.03.0221>.
Non-parametric methods includes superiority index by Lin & Binns (1988)
<doi:10.4141/cjps88-018>, nonparametric measures of phenotypic stability
by Huehn (1990) <https://link.springer.com/article/10.1007/BF00024241>,
TOP third statistic by Fox et al. (1990) <doi:10.1007/BF00040364>.
Functions for computing biometrical analysis such as path analysis,
canonical correlation, partial correlation, clustering analysis, and tools
for inspecting, manipulating, summarizing and plotting typical
multi-environment trial data are also provided.

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
