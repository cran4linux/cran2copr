%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  socialSim
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate and Analyse Social Interaction Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 

%description
Provides tools to simulate and analyse datasets of social interactions
between individuals using hierarchical Bayesian models implemented in
Stan. The package interacts with Stan via 'cmdstanr' (available from
<https://mc-stan.org/r-packages/>) or 'rstan', depending on user setup.
Users can generate realistic interaction data where individual phenotypes
influence and respond to those of their partners, with control over
sampling design parameters such as the number of individuals, partners,
and repeated dyads. The simulation framework allows flexible control over
variation and correlation in mean trait values, social responsiveness, and
social impact, making it suitable for research on interacting phenotypes
and on direct and indirect genetic effects ('DGEs' and 'IGEs'). The
package also includes functions to fit and compare alternative models of
social effects, including impact–responsiveness, variance–partitioning,
and trait-based models, and to summarise model performance in terms of
bias and dispersion. For more details on the study of social interactions
and impact-responsiveness, see Moore et al. (1997)
<doi:10.1111/j.1558-5646.1997.tb01458.x> and de Groot et al. (2022)
<doi:10.1016/j.neubiorev.2022.104996>.

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
