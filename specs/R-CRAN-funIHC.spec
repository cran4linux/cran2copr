%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  funIHC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Iterative Hierarchical Clustering

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-mclust 
Requires:         R-CRAN-fda 
Requires:         R-stats 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-mclust 

%description
Functional clustering aims to group curves exhibiting similar temporal
behaviour and to obtain representative curves summarising the typical
dynamics within each cluster. A key challenge in this setting is class
imbalance, where some clusters contain substantially more curves than
others, which can adversely affect clustering performance. While class
imbalance has been extensively studied in supervised classification, it
has received comparatively little attention in unsupervised clustering.
This package implements functional iterative hierarchical clustering
('funIHC'), an adaptation of the iterative hierarchical clustering method
originally developed for multivariate data, to the functional data
setting. For further details, please see Higgins and Carey (2024)
<doi:10.1007/s11634-024-00611-8>.

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
