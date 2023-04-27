%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TrueSkillThroughTime
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Skill Estimation Based on a Single Bayesian Network

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-hash 
Requires:         R-methods 
Requires:         R-stats 

%description
Most estimators implemented by the video game industry cannot obtain
reliable initial estimates nor guarantee comparability between distant
estimates. TrueSkill Through Time solves all these problems by modeling
the entire history of activities using a single Bayesian network allowing
the information to propagate correctly throughout the system. This
algorithm requires only a few iterations to converge, allowing millions of
observations to be analyzed using any low-end computer. The core ideas
implemented in this project were developed by Dangauthier P, Herbrich R,
Minka T, Graepel T (2007). "Trueskill through time: Revisiting the history
of chess." <https://dl.acm.org/doi/10.5555/2981562.2981605>.

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
