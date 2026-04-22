%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  raretrans
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Priors for Matrix Population Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-stats 

%description
Provides functions to correct biased transition and fertility estimates in
population projection matrices caused by small sample sizes. Small or
short-term studies frequently produce structural zeros (biologically
possible transitions never observed) and structural ones (transitions
estimated at 100%% survival, stasis, or mortality that are biologically
implausible). Both distort matrix structure and bias estimates of
population growth. Implements a multinomial-Dirichlet Bayesian prior for
transition probabilities and a Gamma-Poisson prior for reproduction,
allowing analysts to incorporate prior biological knowledge and regularise
estimates from rare or unobserved events. Includes functions to compute
marginal posterior credible intervals for all transition probabilities
(transition_CrI()), visualise those intervals as point-range plots
(plot_transition_CrI()), and display the full posterior beta density for
each matrix entry (plot_transition_density()). Methods are described in
Tremblay et al. (2021) <doi:10.1016/j.ecolmodel.2021.109526>.

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
