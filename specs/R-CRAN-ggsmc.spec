%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggsmc
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualising Output from Sequential Monte Carlo and Ensemble-Based Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.50
Requires:         R-core >= 3.50
BuildArch:        noarch
BuildRequires:    R-CRAN-poorman 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gganimate 
Requires:         R-CRAN-poorman 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gganimate 

%description
Functions for plotting, and animating, the output of importance samplers,
sequential Monte Carlo samplers (SMC) and ensemble-based methods. The
package can be used to plot and animate histograms, densities, scatter
plots and time series, and to plot the genealogy of an SMC or
ensemble-based algorithm. These functions all rely on algorithm output to
be supplied in tidy format. A function is provided to transform algorithm
output from matrix format (one Monte Carlo point per row) to the tidy
format required by the plotting and animating functions.

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
