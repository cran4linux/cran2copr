%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CAMAN
%global packver   0.77
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.77
Release:          1%{?dist}%{?buildtag}
Summary:          Finite Mixture Models and Meta-Analysis Tools - Based on C.A.MAN

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-mvtnorm 

%description
Tools for the analysis of finite semiparametric mixtures. These are useful
when data is heterogeneous, e.g. in pharmacokinetics or meta-analysis. The
NPMLE and VEM algorithms (flexible support size) and EM algorithms (fixed
support size) are provided for univariate (Bohning et al., 1992;
<doi:10.2307/2532756>) and bivariate data (Schlattmann et al., 2015;
<doi:10.1016/j.jclinepi.2014.08.013>).

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
