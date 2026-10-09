%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  throughyear
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Linking, Routing and Fairness for Through-Year Assessment

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Treats a through-year assessment system (interims during the year feeding
a multistage summative) as the unit of analysis. Links interims to the
summative scale with a latent multivariate normal model that carries each
score's measurement error forward and handles missing interims, estimated
by the EM algorithm (Dempster, Laird and Rubin, 1977,
<doi:10.1111/j.2517-6161.1977.tb01600.x>) with SQUAREM acceleration
(Varadhan and Roland, 2008, <doi:10.1111/j.1467-9469.2007.00585.x>);
simulates cold-start versus prior-informed routing in a two-stage
multistage test; checks whether priors disadvantage late enrollers, low
scorers or fast growers; and evaluates decision accuracy and consistency
of through-year scores against a single summative.

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
