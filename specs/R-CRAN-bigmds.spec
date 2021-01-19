%global packname  bigmds
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multidimensional Scaling for Big Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pdist 
Requires:         R-CRAN-MCMCpack 
Requires:         R-stats 
Requires:         R-CRAN-pdist 

%description
We present a set of algorithms for Multidimensional Scaling (MDS) to be
used with large datasets. MDS is a statistic tool for reduction of
dimensionality, using as input a distance matrix of dimensions n × n. When
n is large, classical algorithms suffer from computational problems and
MDS configuration can not be obtained. With this package, we address these
problems by means of three algorithms: Divide and Conquer MDS, Fast MDS
and MDS based on Gower interpolation. The main idea of these methods is
based on partitioning the dataset into small pieces, where classical
methods can work.

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
