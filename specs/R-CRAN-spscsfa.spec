%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spscsfa
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Semiparametric Smooth-Coefficient Stochastic Frontier Analysis

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-stats 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-np 
Requires:         R-stats 

%description
Provides semiparametric smooth-coefficient stochastic frontier analysis
following Sun and Kumbhakar (2013) <doi:10.1016/j.econlet.2013.05.001>
where the coefficients of the parametric part vary smoothly with a set of
nonparametric variables. Inefficiency term is allowed to depend on a set
of determinants through heteroskedasticity. Smooth coefficients are
estimated using nonparametric regression and the remaining frontier
parameters are estimated by maximum likelihood. Technical efficiency and
inefficiency are computed using the Battese and Coelli (1988)
<doi:10.1016/0304-4076(88)90053-X> and Jondrow et al. (1982)
<doi:10.1016/0304-4076(82)90004-5> methods, respectively. Confidence
intervals for technical efficiency are computed using the approach of
Horrace and Schmidt (1996) <doi:10.1007/BF00157044>.

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
