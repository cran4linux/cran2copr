%global __brp_check_rpaths %{nil}
%global packname  sandwich
%global packver   3.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Covariance Matrix Estimators

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
Object-oriented software for model-robust covariance matrix estimators.
Starting out from the basic robust Eicker-Huber-White sandwich covariance
methods include: heteroscedasticity-consistent (HC) covariances for
cross-section data; heteroscedasticity- and autocorrelation-consistent
(HAC) covariances for time series data (such as Andrews' kernel HAC,
Newey-West, and WEAVE estimators); clustered covariances (one-way and
multi-way); panel and panel-corrected covariances;
outer-product-of-gradients covariances; and (clustered) bootstrap
covariances. All methods are applicable to (generalized) linear model
objects fitted by lm() and glm() but can also be adapted to other classes
through S3 methods. Details can be found in Zeileis et al. (2020)
<doi:10.18637/jss.v095.i01>, Zeileis (2004) <doi:10.18637/jss.v011.i10>
and Zeileis (2006) <doi:10.18637/jss.v016.i09>.

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
