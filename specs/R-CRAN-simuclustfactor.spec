%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simuclustfactor
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Simultaneous Clustering and Factorial Decomposition of Three-Way Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Rdpack 

%description
Implements two iterative techniques called T3Clus and 3Fkmeans, aimed at
simultaneously clustering objects and a factorial dimensionality reduction
of variables and occasions on three-mode datasets developed by Vichi et
al. (2007) <doi:10.1007/s00357-007-0006-x>. Also, we provide a convex
combination of these two simultaneous procedures called CT3Clus and based
on a hyperparameter alpha (alpha in [0,1], with 3FKMeans for alpha=0 and
T3Clus for alpha= 1) also developed by Vichi et al. (2007)
<doi:10.1007/s00357-007-0006-x>. Furthermore, we implemented the
traditional tandem procedures of T3Clus (TWCFTA) and 3FKMeans (TWFCTA) for
sequential clustering-factorial decomposition (TWCFTA), and vice-versa
(TWFCTA) proposed by P. Arabie and L. Hubert (1996)
<doi:10.1007/978-3-642-79999-0_1>.

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
