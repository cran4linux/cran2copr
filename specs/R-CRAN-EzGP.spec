%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EzGP
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easy-to-Interpret Gaussian Process Models for Computer Experiments

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.2.0
BuildRequires:    R-methods >= 4.2.0
BuildRequires:    R-CRAN-nloptr >= 2.0.3
Requires:         R-stats >= 4.2.0
Requires:         R-methods >= 4.2.0
Requires:         R-CRAN-nloptr >= 2.0.3

%description
Fit model for datasets with easy-to-interpret Gaussian process modeling,
predict responses for new inputs. The input variables of the datasets can
be quantitative, qualitative/categorical or mixed. The output variable of
the datasets is a scalar (quantitative). The optimization of the
likelihood function can be chosen by the users (see the documentation of
EzGP_fit()). The modeling method is published in "EzGP: Easy-to-Interpret
Gaussian Process Models for Computer Experiments with Both Quantitative
and Qualitative Factors" by Qian Xiao, Abhyuday Mandal, C. Devon Lin, and
Xinwei Deng (2022) <doi:10.1137/19M1288462>.

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
