%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  effectsize
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Indices of Effect Size

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-insight >= 1.3.0
BuildRequires:    R-CRAN-datawizard >= 1.1.0
BuildRequires:    R-CRAN-parameters >= 0.26.0
BuildRequires:    R-CRAN-bayestestR >= 0.16.0
BuildRequires:    R-CRAN-performance >= 0.14.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-insight >= 1.3.0
Requires:         R-CRAN-datawizard >= 1.1.0
Requires:         R-CRAN-parameters >= 0.26.0
Requires:         R-CRAN-bayestestR >= 0.16.0
Requires:         R-CRAN-performance >= 0.14.0
Requires:         R-stats 
Requires:         R-utils 

%description
Provide utilities to work with indices of effect size for a wide variety
of models and hypothesis tests (see list of supported models using the
function 'insight::supported_models()'), allowing computation of and
conversion between indices such as Cohen's d, r, odds, etc. References:
Ben-Shachar et al. (2020) <doi:10.21105/joss.02815>.

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
