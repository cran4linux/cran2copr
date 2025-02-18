%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  UAHDataScienceUC
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Learn Clustering Techniques Through Examples and Code

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.1
BuildRequires:    R-CRAN-proxy >= 0.4.27
Requires:         R-CRAN-cli >= 3.6.1
Requires:         R-CRAN-proxy >= 0.4.27

%description
A comprehensive educational package combining clustering algorithms with
detailed step-by-step explanations. Provides implementations of both
traditional (hierarchical, k-means) and modern (Density-Based Spatial
Clustering of Applications with Noise (DBSCAN), Gaussian Mixture Models
(GMM), genetic k-means) clustering methods as described in Ezugwu et. al.,
(2022) <doi:10.1016/j.engappai.2022.104743>. Includes educational datasets
highlighting different clustering challenges, based on 'scikit-learn'
examples (Pedregosa et al., 2011)
<https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html>. Features
detailed algorithm explanations, visualizations, and weighted distance
calculations for enhanced learning.

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
