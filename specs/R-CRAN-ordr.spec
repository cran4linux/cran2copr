%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ordr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A 'tidyverse' Extension for Ordinations and Biplots

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-labeling 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-labeling 
Requires:         R-CRAN-ggrepel 

%description
Ordination comprises several multivariate exploratory and explanatory
techniques with theoretical foundations in geometric data analysis; see
Podani (2000, ISBN:90-5782-067-6) for techniques and applications and Le
Roux & Rouanet (2005) <doi:10.1007/1-4020-2236-0> for foundations.
Greenacre (2010, ISBN:978-84-923846) shows how the most established of
these, including principal components analysis, correspondence analysis,
multidimensional scaling, factor analysis, and discriminant analysis, rely
on eigen-decompositions or singular value decompositions of pre-processed
numeric matrix data. These decompositions give rise to a set of shared
coordinates along which the row and column elements can be measured. The
overlay of their scatterplots on these axes, introduced by Gabriel (1971)
<doi:10.1093/biomet/58.3.453>, is called a biplot. 'ordr' provides
inspection, extraction, manipulation, and visualization tools for several
popular ordination classes supported by a set of recovery methods. It is
inspired by and designed to integrate into 'tidyverse' workflows provided
by Wickham et al (2019) <doi:10.21105/joss.01686>.

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
