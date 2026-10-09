%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SINT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation and Analysis of Social Influence Network Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Tools for specifying, analyzing and simulating models of social influence
network theory based on the Friedkin-Johnsen model, Friedkin and Johnsen
(1990) <doi:10.1080/0022250X.1990.9990069>, which includes the consensus
model of DeGroot (1974) <doi:10.1080/01621459.1974.10480137> as a special
case. Equilibrium opinions, total influence matrices and convergence
diagnostics are computed in closed form, also for signed networks with
antagonistic ties, Altafini (2013) <doi:10.1109/TAC.2012.2224251>.
Simulations allow influence weights and susceptibilities to depend on time
and on the state of the system, and can couple latent opinions with
manifest responses through logistic or threshold response functions, whose
results are aggregated into collective outcomes by quota rules.

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
