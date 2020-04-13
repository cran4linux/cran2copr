%global packname  metan
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          Multi Environment Trials Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-FWDselect 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-FWDselect 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-grid 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Performs stability analysis of multi-environment trial data using
parametric and non-parametric methods. Parametric methods includes
Additive Main Effects and Multiplicative Interaction (AMMI) analysis by
Gauch (2013) <doi:10.2135/cropsci2013.04.0241>, Genotype plus
Genotype-Environment (GGE) biplot analysis by Yan & Kang (2003)
<doi:10.1201/9781420040371>, joint Regression Analysis by Eberhart &
Russel (1966) (<doi:10.2135/cropsci1966.0011183X000600010011x>),
ecovalence by Wricke (1965), genotypic confidence index by Annicchiarico
(1992), Murakami & Cruz's (2004) method
<doi:10.12702/1984-7033.v04n01a02>, stability variance by Shukla (1972)
<doi:10.1038/hdy.1972.87>, weighted average of absolute scores by Olivoto
et al. (2019a) <doi:10.2134/agronj2019.03.0220>, and multi-trait stability
index by Olivoto et al. (2019b) <doi:10.2134/agronj2019.03.0221>.
Non-parametric methods includes superiority index by Lin & Binns (1988)
<doi:10.4141/cjps88-018>, nonparametric measures of phenotypic stability
by Huehn (1990) <https://link.springer.com/article/10.1007/BF00024241>,
TOP third statistic by Fox et al. (1990) <doi:10.1007/BF00040364>,
geometric adaptability index described by Shahbazi (2019)
<doi:10.1016/j.scienta.2019.04.047>. Functions for computing biometrical
analysis such as path analysis, canonical correlation, partial
correlation, clustering analysis, and tools for inspecting, manipulating,
summarizing and plotting typical multi-environment trial data are also
provided.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
