%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DEGRE
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Inferring Differentially Expressed Genes using Generalized Linear Mixed Models

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-parglm 
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-utils 
Requires:         R-CRAN-parglm 
Requires:         R-CRAN-glmmTMB 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-car 
Requires:         R-CRAN-dplyr 

%description
Genes that are differentially expressed between two or more experimental
conditions can be detected in RNA-Seq. A high biological variability may
impact the discovery of these genes once it may be divergent between the
fixed effects. However, this variability can be covered by the random
effects. 'DEGRE' was designed to identify the differentially expressed
genes considering fixed and random effects on individuals. These effects
are identified earlier in the experimental design matrix. 'DEGRE' has the
implementation of preprocessing procedures to clean the near zero gene
reads in the count matrix, normalize by 'RLE' published in the 'DESeq2'
package, 'Love et al. (2014)' <doi:10.1186/s13059-014-0550-8> and it fits
a regression for each gene using the Generalized Linear Mixed Model with
the negative binomial distribution, followed by a Wald test to assess the
regression coefficients.

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
