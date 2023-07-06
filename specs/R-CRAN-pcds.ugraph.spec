%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pcds.ugraph
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Underlying Graphs of Proximity Catch Digraphs and Their Applications

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-pcds 
BuildRequires:    R-CRAN-interp 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-pcds 
Requires:         R-CRAN-interp 

%description
Contains the functions for construction and visualization of underlying
and reflexivity graphs of the three families of the proximity catch
digraphs (PCDs), see (Ceyhan (2005) ISBN:978-3-639-19063-2), and for
computing the edge density of these PCD-based graphs which are then used
for testing the patterns of segregation and association against complete
spatial randomness (CSR)) or uniformity in one and two dimensional cases.
The PCD families considered are Arc-Slice PCDs, Proportional-Edge (PE)
PCDs (Ceyhan et al. (2006) <doi:10.1016/j.csda.2005.03.002>) and Central
Similarity PCDs (Ceyhan et al. (2007) <doi:10.1002/cjs.5550350106>). See
also (Ceyhan (2016) <doi:10.1016/j.stamet.2016.07.003>) for edge density
of the underlying and reflexivity graphs of PE-PCDs. The package also has
tools for visualization of PCD-based graphs for one, two, and three
dimensional data.

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
