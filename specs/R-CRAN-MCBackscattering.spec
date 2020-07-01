%global packname  MCBackscattering
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Monte Carlo Simulation for Surface Backscattering

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Monte Carlo simulation is a stochastic method computing trajectories of
photons in media. Surface backscattering is performing calculations in
semi-infinite media and summarizing photon flux leaving the surface. This
simulation is modeling the optical measurement of diffuse reflectance
using an incident light beam. The semi-infinite media is considered to
have flat surface. Media, typically biological tissue, is described by
four optical parameters: absorption coefficient, scattering coefficient,
anisotropy factor, refractive index. The media is assumed to be
homogeneous. Computational parameters of the simulation include: number of
photons, radius of incident light beam, lowest photon energy threshold,
intensity profile (halo) radius, spatial resolution of intensity profile.
You can find more information and validation in the Open Access paper.
Laszlo Baranyai (2020) <doi:10.1016/j.mex.2020.100958>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
