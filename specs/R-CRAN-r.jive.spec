%global __brp_check_rpaths %{nil}
%global packname  r.jive
%global packver   2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Perform JIVE Decomposition for Multi-Source Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-abind 
Requires:         R-graphics 
Requires:         R-stats 

%description
Performs the Joint and Individual Variation Explained (JIVE) decomposition
on a list of data sets when the data share a dimension, returning low-rank
matrices that capture the joint and individual structure of the data
[O'Connell, MJ and Lock, EF (2016) <doi:10.1093/bioinformatics/btw324>].
It provides two methods of rank selection when the rank is unknown, a
permutation test and a Bayesian Information Criterion (BIC) selection
algorithm. Also included in the package are three plotting functions for
visualizing the variance attributed to each data source: a bar plot that
shows the percentages of the variability attributable to joint and
individual structure, a heatmap that shows the structure of the
variability, and principal component plots.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
