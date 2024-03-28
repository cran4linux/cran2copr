%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HTSeed
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting of Hydrotime Model for Seed Germination Time Course

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-dplyr 

%description
The seed germination process starts with water uptake by the seed and ends
with the protrusion of radicle and plumule under varying temperatures and
soil water potential. Hydrotime is a way to describe the relationship
between water potential and seed germination rates at germination
percentages. One important quantity before applying hydrotime modeling of
germination percentages is to consider the proportion of viable seeds that
could germinate under saturated conditions. This package can be used to
apply correction factors at various water potentials before estimating
parameters like stress tolerance, and uniformity of the hydrotime model.
Three different distributions namely, Gaussian, Logistic, and Extreme
value distributions have been considered to fit the model to the seed
germination time course. Details can be found in Bradford (2002)
<https://www.jstor.org/stable/4046371>, and Bradford and Still(2004)
<https://www.jstor.org/stable/23433495>.

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
