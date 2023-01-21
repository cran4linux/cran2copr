%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CJIVE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Canonical Joint and Individual Variation Explained (CJIVE)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-psych 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-psych 

%description
Joint and Individual Variation Explained (JIVE) is a method for
decomposing multiple datasets obtained on the same subjects into shared
structure, structure unique to each dataset, and noise. The two most
common implementations are R.JIVE, an iterative approach, and AJIVE, which
uses principal angle analysis. JIVE estimates subspaces but interpreting
these subspaces can be challenging with AJIVE or R.JIVE. We expand upon
insights into AJIVE as a canonical correlation analysis (CCA) of principal
component scores. This reformulation, which we call CJIVE, 1) provides an
ordering of joint components by the degree of correlation between
corresponding canonical variables; 2) uses a computationally efficient
permutation test for the number of joint components, which provides a
p-value for each component; and 3) can be used to predict subject scores
for out-of-sample observations. Please cite the following article when
utilizing this package: Murden, R., Zhang, Z., Guo, Y., & Risk, B. (2022)
<doi:10.3389/fnins.2022.969510>.

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
