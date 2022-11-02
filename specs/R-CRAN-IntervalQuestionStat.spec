%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IntervalQuestionStat
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Deal with Interval-Valued Responses in Questionnaires

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
A user-friendly toolbox for doing the statistical analysis of
interval-valued responses in questionnaires measuring intrinsically
imprecise human attributes or features (attitudes, perceptions, opinions,
feelings, etc.). In particular, this package provides S4 classes, methods,
and functions in order to compute basic arithmetic and statistical
operations with interval-valued data; prepare customized plots; associate
each interval-valued response to its equivalent Likert-type and visual
analogue scales answers through the minimum theta-distance and the
mid-point criteria; analyze the reliability of respondents' answers from
the internal consistency point of view by means of Cronbach's alpha
coefficient; and simulate interval-valued responses in this type of
questionnaires. The package also incorporates some real-life data that can
be used to illustrate its working with several non-trivial reproducible
examples. The methodology used in this package is based in many
theoretical and applied publications from SMIRE+CoDiRE (Statistical
Methods with Imprecise Random Elements and Comparison of Distributions of
Random Elements) Research Group
(<https://bellman.ciencias.uniovi.es/smire+codire/>) from the University
of Oviedo (Spain).

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
