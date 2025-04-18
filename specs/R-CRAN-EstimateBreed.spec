%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EstimateBreed
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Environmental Variables and Genetic Parameters

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-hrbrthemes 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-nasapower 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-sommer 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-minque 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-lmtest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-hrbrthemes 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggrepel 
Requires:         R-grid 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-nasapower 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-sommer 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-minque 
Requires:         R-utils 
Requires:         R-CRAN-car 
Requires:         R-CRAN-lmtest 

%description
Performs analyzes and estimates of environmental covariates and genetic
parameters related to selection strategies and development of superior
genotypes. It has two main functionalities, the first being about
prediction models of covariates and environmental processes, while the
second deals with the estimation of genetic parameters and selection
strategies. Designed for researchers and professionals in genetics and
environmental sciences, the package combines statistical methods for
modeling and data analysis. This includes the plastochron estimate
proposed by Porta et al. (2024)
<doi:10.1590/1807-1929/agriambi.v28n10e278299>, Stress indices for
genotype selection referenced by Ghazvini et al. (2024)
<doi:10.1007/s10343-024-00981-1>, the Environmental Stress Index described
by Tazzo et al. (2024) <https://revistas.ufg.br/vet/article/view/77035>,
industrial quality indices of wheat genotypes (Szareski et al., 2019),
<doi:10.4238/gmr18223>, Ear Indexes estimation (Rigotti et al., 2024),
<doi:10.13083/reveng.v32i1.17394>, Selection index for protein and grain
yield (de Pelegrin et al., 2017), <doi:10.4236/ajps.2017.813224>,
Estimation of the ISGR - Genetic Selection Index for Resilience for
environmental resilience (Bandeira et al., 2024)
<https://www.cropj.com/Carvalho_18_12_2024_825_830.pdf>, estimation of
Leaf Area Index (Meira et al., 2015)
<https://www.fag.edu.br/upload/revista/cultivando_o_saber/55d1ef202e494.pdf>,
Restriction of control variability (Carvalho et al., 2023)
<doi:10.4025/actasciagron.v45i1.56156>, Risk of Disease Occurrence in
Soybeans described by Engers et al. (2024)
<doi:10.1007/s40858-024-00649-1> and estimation of genetic parameters for
selection based on balanced experiments (Yadav et al., 2024)
<doi:10.1155/2024/9946332>.

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
