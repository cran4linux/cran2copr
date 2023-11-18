%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ANOFA
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analyses of Frequency Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-rrapply >= 1.2.6
BuildRequires:    R-CRAN-superb >= 0.95.0
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-rrapply >= 1.2.6
Requires:         R-CRAN-superb >= 0.95.0
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-stats 
Requires:         R-utils 

%description
Analyses of frequencies can be performed using an alternative test based
on the G statistic. The test has similar type-I error rates and power as
the chi-square test. However, it is based on a total statistic that can be
decomposed in an additive fashion into interaction effects, main effects,
simple effects, contrast effects, etc., mimicking precisely the logic of
ANOVA. We call this set of tools 'ANOFA' (Analysis of Frequency data) to
highlight its similarities with ANOVA. This framework also renders plots
of frequencies along with confidence intervals. Finally, effect sizes and
planning statistical power are easily done under this framework. The ANOFA
is a tool that assesses the significance of effects instead of the
significance of parameters; as such, it is more intuitive to most
researchers than alternative approaches based on generalized linear
models. See Laurencelle and Cousineau (2023)
<doi:10.20982/tqmp.19.2.p173>.

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
