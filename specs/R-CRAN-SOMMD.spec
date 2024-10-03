%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SOMMD
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Self Organising Maps for the Analysis of Molecular Dynamics Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-bio3d 
BuildRequires:    R-CRAN-kohonen 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-bio3d 
Requires:         R-CRAN-kohonen 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-cluster 
Requires:         R-methods 
Requires:         R-CRAN-igraph 

%description
Processes data from Molecular Dynamics simulations using Self Organising
Maps. Features include the ability to read different input formats.
Trajectories can be analysed to identify groups of important frames.
Output visualisation can be generated for maps and pathways.
Methodological details can be found in Motta S et al (2022)
<doi:10.1021/acs.jctc.1c01163>. I/O functions for xtc format files were
implemented using the 'xdrfile' library available under open source
license. The relevant information can be found in inst/COPYRIGHT.

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
