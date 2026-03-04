%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RChASM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Detection of Chromosomal Aneuploidies in Ancient DNA Studies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggsci 
BuildRequires:    R-CRAN-ggstar 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-rstatix 
BuildRequires:    R-CRAN-sirt 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggsci 
Requires:         R-CRAN-ggstar 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-rstatix 
Requires:         R-CRAN-sirt 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readr 

%description
An R implementation of ChASM (Chromosomal Aneuploidy Screening
Methodology): a statistically rigorous Bayesian approach for screening
data sets for autosomal and sex chromosomal aneuploidies. This package
takes as input the number of (deduplicated) reads mapping to chromosomes
1-22 and the X and Y chromosomes, and models these using a
Dirichlet-multinomial distribution. From this, This package returns
posterior probabilities of sex chromosomal karyotypes (XX, XY, XXY, XYY,
XXX and X) and full autosomal aneuploidies (trisomy 13, trisomy 18 and
trisomy 21). This package also returns two diagnostic statistics: (i) a
posterior probability addressing whether contamination between XX and XY
may explain the observed sex chromosomal aneuploidy, and (ii) a
chi-squared statistic measuring whether the observed read counts are too
divergent from the underlying distribution (and may represent abnormal
sequencing/quality issues).

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
