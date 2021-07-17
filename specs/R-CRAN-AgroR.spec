%global __brp_check_rpaths %{nil}
%global packname  AgroR
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Experimental Statistics and Graphics for Agricultural Sciences

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-ScottKnott 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-ARTool 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-hnp 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-drc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-ScottKnott 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-crayon 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-ARTool 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-hnp 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-drc 

%description
Performs the analysis of completely randomized experimental designs (CRD),
randomized blocks (RBD) and Latin square (LSD), experiments in double and
triple factorial scheme (in CRD and RBD), experiments in subdivided plot
scheme (in CRD and RBD), subdivided and joint analysis of experiments in
CRD and RBD, linear regression analysis, test for two samples. The package
performs analysis of variance, ANOVA assumptions and multiple comparison
test of means or regression, according to Pimentel-Gomes (2009, ISBN:
978-85-7133-055-9), nonparametric test (Conover, 1999, ISBN: 0471160687),
test for two samples, joint analysis of experiments according to Ferreira
(2018, ISBN: 978-85-7269-566-4), Anova of aligned ranks (Wobbrock, JO,
Findlater, L., Gergle, D., Higgins , JJ (2011), <doi:
10.1145/1978942.1978963>) and generalized linear model (glm) for binomial
and Poisson family in CRD and RBD (Carvalho, FJ (2019), <doi:
10.14393/ufu.te.2019.1244>). It can also be used to obtain descriptive
measures and graphics, in addition to correlations and creative graphics
used in agricultural sciences (Agronomy, Zootechnics, Food Science and
related areas).

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
