%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spconf
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Computing Scales of Spatial Smoothing for Confounding Adjustment

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-CRAN-mgcv 
Requires:         R-CRAN-flexclust 
Requires:         R-CRAN-mgcv 

%description
Computes the effective range of a smoothing matrix, which is a measure of
the distance to which smoothing occurs. This is motivated by the
application of spatial splines for adjusting for unmeasured spatial
confounding in regression models, but the calculation of effective range
can be applied to smoothing matrices in other contexts. For algorithmic
details, see Rainey and Keller (2024) "spconfShiny: an R Shiny
application..." <doi:10.1371/journal.pone.0311440> and Keller and Szpiro
(2020) "Selecting a Scale for Spatial Confounding Adjustment"
<doi:10.1111/rssa.12556>.

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
