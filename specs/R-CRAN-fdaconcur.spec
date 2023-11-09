%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fdaconcur
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Concurrent Regression and History Index Models for Functional Data

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fdapace 
BuildRequires:    R-stats 
Requires:         R-CRAN-fdapace 
Requires:         R-stats 

%description
Provides an implementation of concurrent or varying coefficient regression
methods for functional data. The implementations are done for both dense
and sparsely observed functional data. Pointwise confidence bands can be
constructed for each case. Further, the influence of past predictor values
are modeled by a smooth history index function, while the effects on the
response are described by smooth varying coefficient functions, which are
very useful in analyzing real data such as COVID data. References: Yao,
F., Müller, H.G., Wang, J.L. (2005) <doi: 10.1214/009053605000000660>.
Sentürk, D., Müller, H.G. (2010) <doi: 10.1198/jasa.2010.tm09228>.

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
