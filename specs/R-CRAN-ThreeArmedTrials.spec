%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ThreeArmedTrials
%global packver   1.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Design and Analysis of Clinical Non-Inferiority or Superiority Trials with Active and Placebo Control

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 

%description
Design and analyze three-arm non-inferiority or superiority trials which
follow a gold-standard design, i.e. trials with an experimental treatment,
an active, and a placebo control. Method for the following distributions
are implemented: Poisson (Mielke and Munk (2009) <arXiv:0912.4169>),
negative binomial (Muetze et al. (2016) <doi:10.1002/sim.6738>), normal
(Pigeot et al. (2003) <doi:10.1002/sim.1450>; Hasler et al. (2009)
<doi:10.1002/sim.3052>), binary (Friede and Kieser (2007)
<doi:10.1002/sim.2543>), nonparametric (Muetze et al. (2017)
<doi:10.1002/sim.7176>), exponential (Mielke and Munk (2009)
<arXiv:0912.4169>).

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
