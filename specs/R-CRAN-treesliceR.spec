%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  treesliceR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          To Slice Phylogenetic Trees and Infer Evolutionary Patterns Over Time

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.7
BuildRequires:    R-CRAN-ggplot2 >= 3.4.2
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-sf >= 1.0.9
BuildRequires:    R-CRAN-doParallel >= 1.0.17
Requires:         R-CRAN-ape >= 5.7
Requires:         R-CRAN-ggplot2 >= 3.4.2
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-sf >= 1.0.9
Requires:         R-CRAN-doParallel >= 1.0.17

%description
Provide a range of functions with multiple criteria for cutting
phylogenetic trees at any evolutionary depth. It enables users to cut
trees in any orientation, such as rootwardly (from root to tips) and
tipwardly (from tips to its root), or allows users to define a specific
time interval of interest. It can also be used to create multiple tree
pieces of equal temporal width. Moreover, it allows the assessment of
novel temporal rates for various phylogenetic indexes, which can be
quickly displayed graphically.

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
