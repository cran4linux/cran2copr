%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ClustBlock
%global packver   3.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering of Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FactoMineR 
Requires:         R-CRAN-FactoMineR 

%description
Hierarchical and partitioning algorithms of blocks of variables. The
partitioning algorithm includes an option called noise cluster to set
aside atypical blocks of variables. The CLUSTATIS method (for quantitative
blocks) (Llobell, Cariou, Vigneau, Labenne & Qannari (2020)
<doi:10.1016/j.foodqual.2018.05.013>, Llobell, Vigneau & Qannari (2019)
<doi:10.1016/j.foodqual.2019.02.017>) and the CLUSCATA method (for
Check-All-That-Apply data) (Llobell, Cariou, Vigneau, Labenne & Qannari
(2019) <doi:10.1016/j.foodqual.2018.09.006>, Llobell, Giacalone, Labenne &
Qannari (2019) <doi:10.1016/j.foodqual.2019.05.017>) are the core of this
package. The CATATIS methods allows to compute some indices and tests to
control the quality of CATA data. Multivariate analysis and clustering of
subjects for quantitative multiblock data, CATA, RATA, Free Sorting and
JAR experiments are available.

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
