%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  woylier
%global packver   0.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Alternative Tour Frame Interpolation Method

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tourr 
BuildRequires:    R-CRAN-geozoo 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-tourr 
Requires:         R-CRAN-geozoo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 

%description
This method generates a tour path by interpolating between d-D frames in
p-D using Givens rotations. The algorithm arises from the problem of
zeroing elements of a matrix. This interpolation method is useful for
showing specific d-D frames in the tour, as opposed to d-D planes, as done
by the geodesic interpolation. It is useful for projection pursuit indexes
which are not s invariant. See more details in Buj, Cook, Asimov and
Hurley (2005) <doi:10.1016/S0169-7161(04)24014-7> and Batsaikhan, Cook and
Laa (2023) <doi:10.48550/arXiv.2311.08181>.

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
