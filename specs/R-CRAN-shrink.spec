%global __brp_check_rpaths %{nil}
%global packname  shrink
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Global, Parameterwise and Joint Shrinkage Factor Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-mfp 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-mfp 

%description
The predictive value of a statistical model can often be improved by
applying shrinkage methods. This can be achieved, e.g., by regularized
regression or empirical Bayes approaches. Various types of shrinkage
factors can also be estimated after a maximum likelihood. While global
shrinkage modifies all regression coefficients by the same factor,
parameterwise shrinkage factors differ between regression coefficients.
With variables which are either highly correlated or associated with
regard to contents, such as several columns of a design matrix describing
a nonlinear effect, parameterwise shrinkage factors are not interpretable
and a compromise between global and parameterwise shrinkage, termed 'joint
shrinkage', is a useful extension. A computational shortcut to
resampling-based shrinkage factor estimation based on DFBETA residuals can
be applied. Global, parameterwise and joint shrinkage for models fitted by
lm(), glm(), coxph(), or mfp() is available.

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
