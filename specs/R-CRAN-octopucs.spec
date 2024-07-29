%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  octopucs
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Support for Hierarchical Clusters

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-progress 

%description
Generates n hierarchical clustering hypotheses on subsets of classifiers
(usually species in community ecology studies). The n clustering
hypotheses are combined to generate a generalized cluster, and computes
three metrics of support. 1) The average proportion of elements conforming
the group in each of the n clusters (integrity). And 2) the contamination,
i.e., the average proportion of elements from other groups that enter a
focal group. 3) The probability of existence of the group gives the
integrity and contamination in a Bayesian approach.

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
