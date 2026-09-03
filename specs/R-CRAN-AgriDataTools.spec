%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AgriDataTools
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Statistical Analysis and Tools for Agricultural Research

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-ggrepel 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 

%description
A comprehensive suite of statistical tools tailored for agricultural and
plant breeding research. Provides automated pipelines for analysis of
variance and covariance under randomized complete block designs and
completely randomized designs, descriptive summary statistics, and
post-hoc multiple range tests including Least Significant Difference,
Tukey, and Scheffe based on Steel et al. (1997) <isbn:978-0070610286>.
Quantitative genetic parameters including genotypic, phenotypic, and
environmental variance components and broad-sense heritability follow
Burton and Devane (1953) <doi:10.2134/agronj1953.00021962004500100005x>.
Genetic advance and genetic advance as percentage of mean estimation
follow Johnson et al. (1955)
<doi:10.2134/agronj1955.00021962004700070009x>. Genotypic, phenotypic, and
environmental correlations follow Miller et al. (1958)
<doi:10.2134/agronj1958.00021962005000100020x>. Genotypic and phenotypic
path coefficient analysis direct and indirect effects decomposition
follows Dewey and Lu (1959)
<doi:10.2134/agronj1959.00021962005100090002x>. Principal component
analysis follows Jolliffe (2002) <isbn:978-0387954424> and hierarchical
clustering follows Sneath and Sokal (1973) <isbn:978-0716706977>.

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
