%global __brp_check_rpaths %{nil}
%global packname  micEconCES
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis with the Constant Elasticity of Substitution (CES) Function

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DEoptim >= 2.0.4
BuildRequires:    R-CRAN-car >= 2.0.0
BuildRequires:    R-CRAN-minpack.lm >= 1.1.4
BuildRequires:    R-CRAN-systemfit >= 1.0.0
BuildRequires:    R-CRAN-micEcon >= 0.6.1
BuildRequires:    R-CRAN-miscTools >= 0.6.1
Requires:         R-CRAN-DEoptim >= 2.0.4
Requires:         R-CRAN-car >= 2.0.0
Requires:         R-CRAN-minpack.lm >= 1.1.4
Requires:         R-CRAN-systemfit >= 1.0.0
Requires:         R-CRAN-micEcon >= 0.6.1
Requires:         R-CRAN-miscTools >= 0.6.1

%description
Tools for econometric analysis and economic modelling with the traditional
two-input Constant Elasticity of Substitution (CES) function and with
nested CES functions with three and four inputs. The econometric
estimation can be done by the Kmenta approximation, or non-linear
least-squares using various gradient-based or global optimisation
algorithms. Some of these algorithms can constrain the parameters to
certain ranges, e.g. economically meaningful values. Furthermore, the
non-linear least-squares estimation can be combined with a grid-search for
the rho-parameter(s).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
