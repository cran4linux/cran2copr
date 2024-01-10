%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bigmds
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multidimensional Scaling for Big Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-svd 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-svd 
Requires:         R-CRAN-corpcor 
Requires:         R-parallel 
Requires:         R-stats 

%description
MDS is a statistic tool for reduction of dimensionality, using as input a
distance matrix of dimensions n × n. When n is large, classical algorithms
suffer from computational problems and MDS configuration can not be
obtained. With this package, we address these problems by means of six
algorithms, being two of them original proposals: - Landmark MDS proposed
by De Silva V. and JB. Tenenbaum (2004). - Interpolation MDS proposed by
Delicado P. and C. Pachón-García (2021) <arXiv:2007.11919> (original
proposal). - Reduced MDS proposed by Paradis E (2018). - Pivot MDS
proposed by Brandes U. and C. Pich (2007) - Divide-and-conquer MDS
proposed by Delicado P. and C. Pachón-García (2021) <arXiv:2007.11919>
(original proposal). - Fast MDS, proposed by Yang, T., J. Liu, L. McMillan
and W. Wang (2006).

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
