%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MixSim
%global packver   1.1-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Simulating Data to Study Performance of Clustering Algorithms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MASS 

%description
The utility of this package is in simulating mixtures of Gaussian
distributions with different levels of overlap between mixture components.
Pairwise overlap, defined as a sum of two misclassification probabilities,
measures the degree of interaction between components and can be readily
employed to control the clustering complexity of datasets simulated from
mixtures. These datasets can then be used for systematic performance
investigation of clustering and finite mixture modeling algorithms. Among
other capabilities of 'MixSim', there are computing the exact overlap for
Gaussian mixtures, simulating Gaussian and non-Gaussian data, simulating
outliers and noise variables, calculating various measures of agreement
between two partitionings, and constructing parallel distribution plots
for the graphical display of finite mixture models.

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
