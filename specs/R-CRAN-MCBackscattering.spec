%global packname  MCBackscattering
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
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

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
