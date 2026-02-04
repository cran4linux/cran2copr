%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gipsDA
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Training DA Models Utilizing 'gips'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gips 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-permutations 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gips 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-permutations 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-numbers 
Requires:         R-CRAN-stringi 

%description
Extends classical linear and quadratic discriminant analysis by
incorporating permutation group symmetries into covariance matrix
estimation. The package leverages methodology from the 'gips' framework to
identify and impose permutation structures that act as a form of
regularization, improving stability and interpretability in settings with
symmetric or exchangeable features. Several discriminant analysis variants
are provided, including pooled and class-specific covariance models, as
well as multi-class extensions with shared or independent symmetry
structures. For more details about 'gips' methodology see and Graczyk et
al. (2022) <doi:10.1214/22-AOS2174> and Chojecki, Morgen, Kołodziejek
(2025, <doi:10.18637/jss.v112.i07>).

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
