%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hmer
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          History Matching and Emulation Package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-isoband 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-ggbeeswarm 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-isoband 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-ggbeeswarm 
Requires:         R-CRAN-stringr 

%description
A set of objects and functions for Bayes Linear emulation and history
matching. Core functionality includes automated training of emulators to
data, diagnostic functions to ensure suitability, and a variety of
proposal methods for generating 'waves' of points. For details on the
mathematical background, there are many papers available on the topic (see
references attached to function help files or the below references); for
details of the functions in this package, consult the manual or help
files. Iskauskas, A, et al. (2024) <doi:10.18637/jss.v109.i10>. Bower,
R.G., Goldstein, M., and Vernon, I. (2010) <doi:10.1214/10-BA524>. Craig,
P.S., Goldstein, M., Seheult, A.H., and Smith, J.A. (1997)
<doi:10.1007/978-1-4612-2290-3_2>.

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
