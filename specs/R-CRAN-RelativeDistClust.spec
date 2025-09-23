%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RelativeDistClust
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering with a Novel Non Euclidean Relative Distance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-compositions 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-compositions 
Requires:         R-CRAN-proxy 
Requires:         R-utils 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-ggplot2 

%description
Using the novel Relative Distance to cluster datasets. Implementation of a
clustering approach based on the k-means algorithm that can be used with
any distance. In addition, implementation of the Hartigan and Wong method
to accommodate alternative distance metrics. Both methods can operate with
any distance measure, provided a suitable method is available to compute
cluster centers under the chosen metric. Additionally, the k-medoids
algorithm is implemented, offering a robust alternative for clustering
without the need of computing cluster centers under the chosen metric. All
three methods are designed to support Relative distances, Euclidean
distances, and any user-defined distance functions. The Hartigan and Wong
method is described in Hartigan and Wong (1979) <doi:10.2307/2346830> and
an explanation of the k-medoids algorithm can be found in Reynolds et al
(2006) <doi:10.1007/s10852-005-9022-1>.

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
