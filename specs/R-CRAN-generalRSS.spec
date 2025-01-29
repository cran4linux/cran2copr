%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  generalRSS
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tools for Balanced and Unbalanced Ranked Set Sampling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-emplik 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-emplik 
Requires:         R-CRAN-rootSolve 

%description
Ranked Set Sampling (RSS) is a stratified sampling method known for its
efficiency compared to Simple Random Sampling (SRS). When sample
allocation is equal across strata, it is referred to as balanced RSS
(BRSS) whereas unequal allocation is called unbalanced RSS (URSS), which
is particularly effective for asymmetric or skewed distributions. This
package offers practical statistical tools and sampling methods for both
BRSS and URSS, emphasizing flexible sampling designs and inference for
population means, medians, proportions, and Area Under the Curve (AUC). It
incorporates parametric and nonparametric tests, including empirical
likelihood ratio (LR) methods. The package provides ranked set sampling
methods from a given population, including sampling with imperfect ranking
using auxiliary variables. Furthermore, it provides tools for efficient
sample allocation in URSS, ensuring greater efficiency than SRS and BRSS.
For more details, refer e.g. to Chen et al. (2003)
<doi:10.1007/978-0-387-21664-5>, Ahn et al. (2022)
<doi:10.1007/978-3-031-14525-4_3>, and Ahn et al. (2024)
<doi:10.1111/insr.12589>.

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
