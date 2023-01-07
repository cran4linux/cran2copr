%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pcds
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Proximity Catch Digraphs and Their Applications

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-CRAN-gMOIP 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-interp 
Requires:         R-CRAN-gMOIP 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-plotrix 

%description
Contains the functions for generating patterns of segregation,
association, complete spatial randomness (CSR)) and Uniform data in one,
two and three dimensional cases, for testing these patterns based on two
invariants of various families of the proximity catch digraphs (PCDs) (see
(Ceyhan (2005) ISBN:978-3-639-19063-2). The graph invariants used in
testing spatial point data are the domination number (Ceyhan (2011)
<doi:10.1080/03610921003597211>) and arc density (Ceyhan et al. (2006)
<doi:10.1016/j.csda.2005.03.002>; Ceyhan et al. (2007)
<doi:10.1002/cjs.5550350106>) of for two-dimensional data for
visualization of PCDs for one, two and three dimensional data. The PCD
families considered are Arc-Slice PCDs, Proportional-Edge PCDs and Central
Similarity PCDs.

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
