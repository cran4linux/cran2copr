%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EMMIXmfa
%global packver   2.0.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.14
Release:          1%{?dist}%{?buildtag}
Summary:          Mixture Models with Component-Wise Factor Analyzers

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
Requires:         R-methods 

%description
We provide functions to fit finite mixtures of multivariate normal or
t-distributions to data with various factor analytic structures adopted
for the covariance/scale matrices. The factor analytic structures
available include mixtures of factor analyzers and mixtures of common
factor analyzers. The latter approach is so termed because the matrix of
factor loadings is common to components before the component-specific
rotation of the component factors to make them white noise. Note that the
component-factor loadings are not common after this rotation. Maximum
likelihood estimators of model parameters are obtained via the
Expectation-Maximization algorithm. See descriptions of the algorithms
used in McLachlan GJ, Peel D (2000) <doi:10.1002/0471721182.ch8> McLachlan
GJ, Peel D (2000) <ISBN:1-55860-707-2> McLachlan GJ, Peel D, Bean RW
(2003) <doi:10.1016/S0167-9473(02)00183-4> McLachlan GJ, Bean RW,
Ben-Tovim Jones L (2007) <doi:10.1016/j.csda.2006.09.015> Baek J,
McLachlan GJ, Flack LK (2010) <doi:10.1109/TPAMI.2009.149> Baek J,
McLachlan GJ (2011) <doi:10.1093/bioinformatics/btr112> McLachlan GJ, Baek
J, Rathnayake SI (2011) <doi:10.1002/9781119995678.ch9>.

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
