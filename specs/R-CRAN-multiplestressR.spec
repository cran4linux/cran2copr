%global __brp_check_rpaths %{nil}
%global packname  multiplestressR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Additive and Multiplicative Null Models for Multiple Stressor Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-viridis 

%description
An implementation of the additive (Gurevitch et al., 2000
<doi:10.1086/303337>) and multiplicative (Lajeunesse, 2011
<doi:10.1890/11-0423.1>) factorial null models for multiple stressor data
(Burgess et al., 2021 <doi:10.1101/2021.07.21.453207>). Effect sizes are
able to be calculated for either null model, and subsequently classified
into one of four different interaction classifications (e.g., antagonistic
or synergistic interactions). Analyses can be conducted on data for single
experiments through to large meta-analytical datasets. Minimal input (or
statistical knowledge) is required, with any output easily understood.
Summary figures are also able to be easily generated.

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
