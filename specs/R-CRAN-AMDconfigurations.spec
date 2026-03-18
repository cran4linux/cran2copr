%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AMDconfigurations
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Geometric Analysis of Configurations in High-Dimensional Spaces

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-stats 
Requires:         R-CRAN-e1071 
Requires:         R-stats 

%description
Tools for analysing the geometry of configurations in high-dimensional
spaces using the Average Membership Degree (AMD) framework and synthetic
configuration generation. The package supports a domain-agnostic approach
to studying the shape, dispersion, and internal structure of point clouds,
with applications across biological and ecological datasets, including
those derived from deep-time records. The AMD framework builds on the idea
that strongly coupled systems may occupy a limited set of recurrent
regimes in state space, producing high-occupancy regions separated by
sparsely populated transitional configurations. The package focuses on
detecting these concentration patterns and quantifying their geometric
definition without assuming any underlying dynamical model. It provides
AMD curve computation, cluster assignment, and sigma-equivalent
estimation, together with S3 methods for plotting, printing, and
summarising AMD and sigma-equivalent objects. Mendoza (2025)
<https://mmendoza1967.github.io/AMDconfigurations/>.

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
