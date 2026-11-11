%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vectorialcalculus
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Numerical Tools for University Calculus

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Independent reconstruction of numerical tools for teaching university
calculus. Provides finite difference derivative approximations with
numerical sensitivity diagnostics and local linear models. Optional
interactive graphics illustrate secants, tangents, differentials and
numerical Taylor polynomials of orders one and two. Includes finite limit
probes, critical-point and concavity analysis, and Newton iteration with
explicit numerical diagnostics. Provides signed Riemann sums, partition
refinement, fixed and adaptive quadrature with error diagnostics, and
optional interactive illustrations of numerical integration. Evaluates
accumulation functions and compares their numerical derivatives with
integrands while retaining quadrature and sensitivity diagnostics.
Computes geometric areas, graph lengths, revolution volumes and surface
areas, with separate interactive region and solid illustrations.
Approximates coordinate partials, gradients and line-restriction
directional derivatives without inferring total differentiability from
finite coordinate probes. Provides candidate affine models and total
differentials with actual-change comparisons and separate plane, section
and tangent illustrations. Supports rectangular Jacobians, direct Hessian
stencils and matrix refinement views with entry-level numerical
sensitivity and roundoff diagnostics. Searches for multivariable
stationary candidates with explicit starts, retained evaluation histories
and conditional second derivative classifications. Solves square nonlinear
systems with Newton iteration, Jacobian diagnostics, optional step damping
and independent zero-contour playback. Assesses equality-constrained
candidates using Lagrange multipliers, numerical rank and conditional
tangent-space curvature diagnostics. Integrates Cartesian type I and II
regions with nested fixed quadrature, retained inner diagnostics and
independent sampled-domain graphics. Supports polar regions with a radial
Jacobian and Cartesian domain views. Integrates nested Cartesian solids in
six coordinate orders, retaining slice diagnostics with independent fiber
and base-projection displays. Supports cylindrical-coordinate solids with
a radial Jacobian and separate Cartesian fiber and polar-base views.
Spherical regions use explicit azimuth, polar angle and radius with their
volume Jacobian and an independent Cartesian radial-fiber display.
Assesses implicit related rates with feasibility, differentiability
hypotheses, denominator sensitivity diagnostics and a separate local
velocity display. Provides product partitions, signed double Riemann
sample rules, sampled cell statistics, explicit domain indicators,
refinement tables and prism views. Samples standalone planar regions with
reusable strip grids and separate filled-domain or horizontal-plate
displays. Samples six faces of nested Cartesian solids with shared
endpoints and independent face/wireframe displays, without coupling
geometric sampling to quadrature. Maps stored cylindrical parameter
patches into Cartesian walls, caps and angular cuts with explicit seam and
axis-degeneracy limitations. Samples spherical radial shells and angular
cuts with explicit pole/origin degeneracies and separate stored-face
displays. Shows stored stationary candidates on sampled scalar graphs
without rerunning search or classification. Samples spatial parametric
curves, displays stored samples, and integrates speed using supplied
velocities or numerical Jacobians. Computes spatial Frenet directions,
curvature and signed torsion with derivative diagnostics and displays
stored results. Samples osculating circles and ribbons with explicit
geometry gaps and separate interactive views. Samples spatial vector
fields, estimates divergence and curl, and integrates streamlines or
time-dependent pathlines with fixed-step Runge-Kutta. Computes signed
scalar line integrals and oriented vector work in two and three
dimensions, with separate quadrature and derivative diagnostics. Samples
parametric and ruled surfaces and integrates scalar densities, area and
oriented flux over rectangular parameter domains. Compares the two
integrals in Green's circulation theorem over a planar strip and in
Stokes' theorem over a rectangular parameter patch. Compares outward flux
and integrated divergence over a Cartesian box.

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
