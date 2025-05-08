%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CBAModel
%global packver   0.0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Stochastic 3D Structure Model for Binder-Conductive Additive Phase

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-pracma 

%description
Simulation of the stochastic 3D structure model for the nanoporous
binder-conductive additive phase in battery cathodes introduced in P.
Gräfensteiner, M. Osenberg, A. Hilger, N. Bohn, J. R. Binder, I. Manke, V.
Schmidt, M. Neumann (2024) <doi:10.48550/arXiv.2409.11080>. The model is
developed for a binder-conductive additive phase of consisting of carbon
black, polyvinylidene difluoride binder and graphite particles. For its
stochastic 3D modeling, a three-step procedure based on methods from
stochastic geometry is used. First, the graphite particles are described
by a Boolean model with ellipsoidal grains. Second, the mixture of carbon
black and binder is modeled by an excursion set of a Gaussian random field
in the complement of the graphite particles. Third, large pore regions
within the mixture of carbon black and binder are described by a Boolean
model with spherical grains.

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
