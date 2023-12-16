%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tightenBlock
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Tightens an Observational Block Design by Balanced Subset Matching

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rcbalance 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rcbalance 

%description
Tightens an observational block design into a smaller design with either
smaller or fewer blocks while controlling for covariates. The method uses
fine balance, optimal subset matching (Rosenbaum, 2012
<doi:10.1198/jcgs.2011.09219>) and two-criteria matching (Zhang et al 2023
<doi:10.1080/01621459.2021.1981337>).  The main function is tighten().
The suggested 'rrelaxiv' package for solving minimum cost flow problems:
(i) derives from Bertsekas and Tseng (1988) <doi:10.1007/BF02288322>, (ii)
is not available on CRAN due to its academic license, (iii) may be
downloaded from GitHub at <https://github.com/josherrickson/rrelaxiv/>,
(iv) is not essential to use the package.

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
