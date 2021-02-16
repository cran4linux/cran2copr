%global packname  cmprskcoxmsm
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Use IPW to Estimate Treatment Effect under Competing Risks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-twang 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-CRAN-twang 
Requires:         R-graphics 
Requires:         R-CRAN-sandwich 

%description
Uses inverse probability weighting methods to estimate treatment effect
under marginal structure model for the cause-specific hazard of competing
risk events. Estimates also the cumulative incidence function (i.e. risk)
of the potential outcomes, and provides inference on risk difference and
risk ratio. Reference: Kalbfleisch & Prentice
(2002)<doi:10.1002/9781118032985>; Hernan et al
(2001)<doi:10.1198/016214501753168154>.

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
