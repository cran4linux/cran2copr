%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  enrichwith
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Methods to Enrich R Objects with Extra Components

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch

%description
Provides the "enrich" method to enrich list-like R objects with new,
relevant components. The current version has methods for enriching objects
of class 'family', 'link-glm', 'lm', 'glm' and 'betareg'. The resulting
objects preserve their class, so all methods associated with them still
apply. The package also provides the 'enriched_glm' function that has the
same interface as 'glm' but results in objects of class 'enriched_glm'. In
addition to the usual components in a `glm` object, 'enriched_glm' objects
carry an object-specific simulate method and functions to compute the
scores, the observed and expected information matrix, the first-order
bias, as well as model densities, probabilities, and quantiles at
arbitrary parameter values. The package can also be used to produce
customizable source code templates for the structured implementation of
methods to compute new components and enrich arbitrary objects.

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
