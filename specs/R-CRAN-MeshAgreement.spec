%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MeshAgreement
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Agreement Measures for 3D Meshes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rvcg 
BuildRequires:    R-CRAN-cgalMeshes 
Requires:         R-stats 
Requires:         R-CRAN-Rvcg 
Requires:         R-CRAN-cgalMeshes 

%description
Calculates distance-based and volume-overlap-based agreement measures for
triangular 3D meshes. These include the Hausdorff distance, the average
surface distance, the Dice similarity coefficient, and the Jaccard
similarity coefficient as documented in Stockinger et al. (2021)
<doi:10.1186/s13014-021-01965-5>. Overall agreement for a set of meshes is
calculated as the aggregate agreement for all pairwise comparisons. Based
on algorithms provided by the 'VCGLIB' <http://vcg.isti.cnr.it/vcglib/>
and 'CGAL' <https://www.cgal.org/> libraries. Includes web-based graphical
user interface.

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
