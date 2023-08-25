%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  UNCOVER
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Utilising Normalisation Constant Optimisation via Edge Removal (UNCOVER)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cachem 
BuildRequires:    R-CRAN-ggnewscale 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-cachem 
Requires:         R-CRAN-ggnewscale 

%description
Model data with a suspected clustering structure (either in co-variate
space, regression space or both) using a Bayesian product model with a
logistic regression likelihood. Observations are represented graphically
and clusters are formed through various edge removals or additions.
Cluster quality is assessed through the log Bayesian evidence of the
overall model, which is estimated using either a Sequential Monte Carlo
sampler or a suitable transformation of the Bayesian Information Criterion
as a fast approximation of the former. The internal Iterated Batch
Importance Sampling scheme (Chopin (2002 <doi:10.1093/biomet/89.3.539>))
is made available as a free standing function.

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
