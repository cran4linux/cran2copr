%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cdlogit
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Context-Dependent Discrete Choice Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-randtoolbox 
Requires:         R-CRAN-randtoolbox 

%description
Implements a class of context-dependent discrete choice models, including
the standard random utility maximization (RUM) model, classical and
generalized random regret minimization (RRM) models, the random advantage
maximization (RAM) model, as well as the Emergent Value (EV) model and the
contextual random utility maximization (CRUM) model, which explicitly
incorporate measures of context dependence. In addition, pairwise
normalization (PN) and range normalization (RN) models are supported. Both
fixed-parameter and random-parameter specifications can be estimated, the
latter allowing for preference heterogeneity. All models are formulated
within a logit framework under the assumption of independently and
identically distributed (i.i.d.) Gumbel error terms. The implemented
methods are based on Tversky and Simonson (1993)
<doi:10.1287/mnsc.39.10.1179>, Chorus et al. (2014)
<doi:10.1016/j.jbusres.2014.02.010>, Rooderkerk et al. (2011)
<doi:10.1509/jmkr.48.4.767>, Guevara and Fukushi (2016)
<doi:10.1016/j.trb.2016.07.012>, Landry and Webb (2021)
<doi:10.1016/j.jet.2021.105221>, and Daviet and Webb (2023)
<doi:10.1016/j.jmp.2022.102741>.

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
