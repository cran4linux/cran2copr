%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tseffects
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Inferences from Time Series (with Interactions)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mpoly 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-mpoly 
Requires:         R-CRAN-car 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-utils 

%description
Autoregressive distributed lag (A[R]DL) models (and their reparameterized
equivalent, the Generalized Error-Correction Model [GECM]) are the
workhorse models in uncovering dynamic inferences. ADL models are simple
to estimate; this is what makes them attractive. Once these models are
estimated, what is less clear is how to uncover a rich set of dynamic
inferences from these models. We provide tools for recovering those
inferences. These tools apply to traditional time-series quantities of
interest: especially instantaneous effects for any period and cumulative
effects for any period (including the long-run effect). They also allow
for a variety of shock histories to be applied to the independent variable
(beyond just a one-time, one-unit increase) as well as the recovery of
inferences in levels for shocks applies to (in)dependent variables in
differences (what we call the Generalized Dynamic Response Function).
These effects are also available for the general conditional dynamic model
advocated by Warner, Vande Kamp, and Jordan (2026
<doi:10.1017/psrm.2026.10087>). We also provide the actual formulae for
these effects.

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
