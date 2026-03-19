%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PCSinR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Constraint Satisfaction Networks in R

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch

%description
Parallel Constraint Satisfaction (PCS) models are an increasingly common
class of models in Psychology, with applications to reading and word
recognition (McClelland & Rumelhart, 1981;
doi{10.1037/0033-295X.88.5.375}), judgment and decision making (Glöckner
& Betsch, 2008 doi{10.1017/S1930297500002424}; Glöckner, Hilbig, & Jekel,
2014 doi{10.1016/j.cognition.2014.08.017}), and several other fields. In
each of these fields, they provide a quantitative model of psychological
phenomena, with precise predictions regarding choice probabilities,
decision times, and often the degree of confidence. This package provides
the necessary functions to create and simulate basic Parallel Constraint
Satisfaction networks within R.

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
