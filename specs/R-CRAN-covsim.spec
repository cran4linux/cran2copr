%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  covsim
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          VITA, IG and PLSIM Simulation for Given Covariance and Marginals

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.6.5
BuildRequires:    R-CRAN-rvinecopulib >= 0.5.1.1.0
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-PearsonDS 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-lavaan >= 0.6.5
Requires:         R-CRAN-rvinecopulib >= 0.5.1.1.0
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-PearsonDS 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-Matrix 

%description
Random sampling from distributions with user-specified population
covariance matrix. Marginal information may be fully specified, for which
the package implements the VITA (VIne-To-Anything) algorithm Grønneberg
and Foldnes (2017) <doi:10.1007/s11336-017-9569-6>.  See also Grønneberg,
Foldnes and Marcoulides (2022) <doi:10.18637/jss.v102.i03>. Alternatively,
marginal skewness and kurtosis may be specified, for which the package
implements the IG (independent generator) and PLSIM (piecewise linear)
algorithms, see Foldnes and Olsson (2016)
<doi:10.1080/00273171.2015.1133274> and Foldnes and Grønneberg (2021)
<doi:10.1080/10705511.2021.1949323>, respectively.

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
