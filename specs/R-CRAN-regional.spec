%global __brp_check_rpaths %{nil}
%global packname  regional
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Intra- and Inter-Regional Similarity

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-philentropy >= 0.6.0
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-philentropy >= 0.6.0
Requires:         R-CRAN-terra 

%description
Calculates intra-regional and inter-regional similarities based on
user-provided spatial vector objects (regions) and spatial raster objects
(cells with values). Implemented metrics include inhomogeneity, isolation
(Haralick and Shapiro (1985) <doi:10.1016/S0734-189X(85)90153-7>,
Jasiewicz et al. (2018) <doi:10.1016/j.cageo.2018.06.003>), and
distinction (Nowosad (2021) <doi:10.1080/13658816.2021.1893324>).

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
