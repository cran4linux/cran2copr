%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  castgen
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Sample Size for Population Genomic Studies

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel >= 4.0.0
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-vcfR >= 1.15.0
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-doParallel >= 1.0.17
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-parallel >= 4.0.0
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-vcfR >= 1.15.0
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-doParallel >= 1.0.17
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-stats 
Requires:         R-utils 

%description
Estimate sample sizes needed to capture target levels of genetic diversity
from a population (multivariate allele frequencies) for applications like
germplasm conservation and breeding efforts. Compares bootstrap samples to
a full population using linear regression, employing the R-squared value
to represent the proportion of diversity captured. Iteratively increases
sample size until a user-defined target R-squared is met. Offers a
parallelized R implementation of a previously developed 'python' method.
All ploidy levels are supported. For more details, see Sandercock et al.
(2024) <doi:10.1073/pnas.2403505121>.

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
