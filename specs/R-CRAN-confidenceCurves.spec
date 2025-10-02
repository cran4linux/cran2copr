%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  confidenceCurves
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Frequentist Confidence Analysis for Clinical Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-cowplot >= 1.1.3
BuildRequires:    R-CRAN-DescTools >= 0.99.54
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-cowplot >= 1.1.3
Requires:         R-CRAN-DescTools >= 0.99.54

%description
Frequentist confidence analysis answers the question: How confident are we
in a particular treatment effect?  This package calculates the frequentist
confidence in a treatment effect of interest given observed data, and
returns the family of confidence curves associated with that data.

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
