%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  freebird
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Inference for High Dimensional Mediation and Surrogate Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-scalreg 
BuildRequires:    R-CRAN-Rmosek 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-scalreg 
Requires:         R-CRAN-Rmosek 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-MASS 

%description
Estimates and provides inference for quantities that assess high
dimensional mediation and potential surrogate markers including the direct
effect of treatment, indirect effect of treatment, and the proportion of
treatment effect explained by a surrogate/mediator; details are described
in Zhou et al (2022) <doi:10.1002/sim.9352> and Zhou et al (2020)
<doi:10.1093/biomet/asaa016>. This package relies on the optimization
software 'MOSEK', <https://www.mosek.com>.

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
