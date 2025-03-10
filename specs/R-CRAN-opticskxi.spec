%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  opticskxi
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          OPTICS K-Xi Density-Based Clustering

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-rlang 

%description
Density-based clustering methods are well adapted to the clustering of
high-dimensional data and enable the discovery of core groups of various
shapes despite large amounts of noise. This package provides a novel
density-based cluster extraction method, OPTICS k-Xi, and a framework to
compare k-Xi models using distance-based metrics to investigate datasets
with unknown number of clusters. The vignette first introduces
density-based algorithms with simulated datasets, then presents and
evaluates the k-Xi cluster extraction method. Finally, the models
comparison framework is described and experimented on 2 genetic datasets
to identify groups and their discriminating features. The k-Xi algorithm
is a novel OPTICS cluster extraction method that specifies directly the
number of clusters and does not require fine-tuning of the steepness
parameter as the OPTICS Xi method. Combined with a framework that compares
models with varying parameters, the OPTICS k-Xi method can identify groups
in noisy datasets with unknown number of clusters. Results on summarized
genetic data of 1,200 patients are in Charlon T. (2019)
<doi:10.13097/archive-ouverte/unige:161795>. A short video tutorial can be
found at <https://www.youtube.com/watch?v=P2XAjqI5Lc4/>.

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
