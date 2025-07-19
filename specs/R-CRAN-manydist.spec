%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  manydist
%global packver   0.4.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.8
Release:          1%{?dist}%{?buildtag}
Summary:          Unbiased Distances for Mixed-Type Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-philentropy 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-distances 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-philentropy 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-distances 

%description
A comprehensive framework for calculating unbiased distances in datasets
containing mixed-type variables (numerical and categorical). The package
implements a general formulation that ensures multivariate additivity and
commensurability, meaning that variables contribute equally to the overall
distance regardless of their type, scale, or distribution. Supports
multiple distance measures including Gower's distance, Euclidean distance,
Manhattan distance, and various categorical variable distances such as
simple matching, Eskin, occurrence frequency, and association-based
distances. Provides tools for variable scaling (standard deviation, range,
robust range, and principal component scaling), and handles both
independent and association-based category dissimilarities. Implements
methods to correct for biases that typically arise from different variable
types, distributions, and number of categories. Particularly useful for
cluster analysis, data visualization, and other distance-based methods
when working with mixed data. Methods based on van de Velden et al. (2024)
<doi:10.48550/arXiv.2411.00429> "Unbiased mixed variables distance".

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
