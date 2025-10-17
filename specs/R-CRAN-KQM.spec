%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KQM
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          K Quantiles Medoids (KQM) Clustering

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-cluster 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-cluster 

%description
K Quantiles Medoids (KQM) clustering applies quantiles to divide data of
each dimension into K mean intervals. Combining quantiles of all the
dimensions of the data and fully permuting quantiles on each dimension is
the strategy to determine a pool of candidate initial cluster centers. To
find the best initial cluster centers from the pool of candidate initial
cluster centers, two methods based on quantile strategy and PAM strategy
respectively are proposed. During a clustering process, medoids of
clusters are used to update cluster centers in each iteration. Comparison
between KQM and the method of randomly selecting initial cluster centers
shows that KQM is almost always getting clustering results with smaller
total sum squares of distances.

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
