%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  boxcoxmix
%global packver   0.46
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.46
Release:          1%{?dist}%{?buildtag}
Summary:          Box-Cox-Type Transformations for Linear and Logistic Models with Random Effects

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-statmod >= 1.4.27
BuildRequires:    R-CRAN-qicharts >= 0.5.4
BuildRequires:    R-CRAN-npmlreg >= 0.46.1
Requires:         R-CRAN-statmod >= 1.4.27
Requires:         R-CRAN-qicharts >= 0.5.4
Requires:         R-CRAN-npmlreg >= 0.46.1

%description
Box-Cox-type transformations for linear and logistic models with random
effects using non-parametric profile maximum likelihood estimation, as
introduced in Almohaimeed (2018) <http://etheses.dur.ac.uk/12831/> and
Almohaimeed and Einbeck (2022) <doi:10.1177/1471082X20966919>. The main
functions are 'optim.boxcox()' for linear models with random effects and
'boxcoxtype()' for logistic models with random effects.

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
