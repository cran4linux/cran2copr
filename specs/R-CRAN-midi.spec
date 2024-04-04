%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  midi
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Microstructure Information from Diffusion Imaging

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-withr 

%description
An implementation of a taxonomy of models of restricted diffusion in
biological tissues parametrized by the tissue geometry (axis, diameter,
density, etc.). This is primarily used in the context of diffusion
magnetic resonance (MR) imaging to model the MR signal attenuation in the
presence of diffusion gradients. The goal is to provide tools to simulate
the MR signal attenuation predicted by these models under different
experimental conditions. The package feeds a companion 'shiny' app
available at <https://midi-pastrami.apps.math.cnrs.fr> that serves as a
graphical interface to the models and tools provided by the package.
Models currently available are the ones in Neuman (1974)
<doi:10.1063/1.1680931>, Van Gelderen et al. (1994)
<doi:10.1006/jmrb.1994.1038>, Stanisz et al. (1997)
<doi:10.1002/mrm.1910370115>, Soderman & Jonsson (1995)
<doi:10.1006/jmra.1995.0014> and Callaghan (1995)
<doi:10.1006/jmra.1995.1055>.

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
