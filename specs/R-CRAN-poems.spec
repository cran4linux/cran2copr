%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  poems
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Pattern-Oriented Ensemble Modeling System

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 3.6
BuildRequires:    R-CRAN-R6 >= 2.5.0
BuildRequires:    R-CRAN-abc >= 2.1
BuildRequires:    R-CRAN-foreach >= 1.5.1
BuildRequires:    R-CRAN-trend >= 1.1.4
BuildRequires:    R-CRAN-lhs >= 1.1.1
BuildRequires:    R-CRAN-doParallel >= 1.0.16
BuildRequires:    R-CRAN-truncnorm >= 1.0
BuildRequires:    R-CRAN-metRology >= 0.9.28.1
BuildRequires:    R-CRAN-fossil >= 0.4.0
BuildRequires:    R-CRAN-gdistance 
BuildRequires:    R-CRAN-qs 
Requires:         R-CRAN-raster >= 3.6
Requires:         R-CRAN-R6 >= 2.5.0
Requires:         R-CRAN-abc >= 2.1
Requires:         R-CRAN-foreach >= 1.5.1
Requires:         R-CRAN-trend >= 1.1.4
Requires:         R-CRAN-lhs >= 1.1.1
Requires:         R-CRAN-doParallel >= 1.0.16
Requires:         R-CRAN-truncnorm >= 1.0
Requires:         R-CRAN-metRology >= 0.9.28.1
Requires:         R-CRAN-fossil >= 0.4.0
Requires:         R-CRAN-gdistance 
Requires:         R-CRAN-qs 

%description
A framework of interoperable R6 classes (Chang, 2020,
<https://CRAN.R-project.org/package=R6>) for building ensembles of viable
models via the pattern-oriented modeling (POM) approach (Grimm et
al.,2005, <doi:10.1126/science.1116681>). The package includes classes for
encapsulating and generating model parameters, and managing the POM
workflow. The workflow includes: model setup; generating model parameters
via Latin hyper-cube sampling (Iman & Conover, 1980,
<doi:10.1080/03610928008827996>); running multiple sampled model
simulations; collating summary results; and validating and selecting an
ensemble of models that best match known patterns. By default, model
validation and selection utilizes an approximate Bayesian computation
(ABC) approach (Beaumont et al., 2002, <doi:10.1093/genetics/162.4.2025>),
although alternative user-defined functionality could be employed. The
package includes a spatially explicit demographic population model
simulation engine, which incorporates default functionality for density
dependence, correlated environmental stochasticity, stage-based
transitions, and distance-based dispersal. The user may customize the
simulator by defining functionality for translocations, harvesting,
mortality, and other processes, as well as defining the sequence order for
the simulator processes. The framework could also be adapted for use with
other model simulators by utilizing its extendable (inheritable) base
classes.

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
