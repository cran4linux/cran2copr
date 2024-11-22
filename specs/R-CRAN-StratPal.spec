%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StratPal
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stratigraphic Paleobiology Modeling Pipelines

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-admtools >= 0.4.0
BuildRequires:    R-CRAN-paleoTS 
Requires:         R-CRAN-admtools >= 0.4.0
Requires:         R-CRAN-paleoTS 

%description
The fossil record is a joint expression of ecological, taphonomic,
evolutionary, and stratigraphic processes (Holland and Patzkowsky, 2012,
ISBN:978-0226649382). This package allowing to simulate biological
processes in the time domain (e.g., trait evolution, fossil abundance),
and examine how their expression in the rock record (stratigraphic domain)
is influenced based on age-depth models, ecological niche models, and
taphonomic effects. Functions simulating common processes used in modeling
trait evolution or event type data such as first/last occurrences are
provided and can be used standalone or as part of a pipeline. The package
comes with example data sets and tutorials in several vignettes, which can
be used as a template to set up one's own simulation.

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
