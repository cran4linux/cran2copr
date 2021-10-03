%global __brp_check_rpaths %{nil}
%global packname  bigmds
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multidimensional Scaling for Big Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-parallel 

%description
MDS is a statistic tool for reduction of dimensionality, using as input a
distance matrix of dimensions n × n. When n is large, classical algorithms
suffer from computational problems and MDS configuration can not be
obtained. With this package, we address these problems by means of three
algorithms: - Divide-and-conquer MDS developed by Delicado P. and C.
Pachon-Garcia (2021) <arXiv:2007.11919>. - Fast MDS, which is an
implementation of Yang, T., J. Liu, L. McMillan, and W. Wang (2006). -
Interpolation MDS, which uses Gower's interpolation formula as described
in Gower, J. C. and D. J. Hand (1995, ISBN: 978-0-412-71630-0). The main
idea of these algorithms is based on partitioning the data set into small
pieces, where classical methods can work. In order to align all the
solutions, it is used Procrustes formula as described in Borg, I. and P.
Groenen (2005, ISBN : 978-0-387-25150-9).

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
