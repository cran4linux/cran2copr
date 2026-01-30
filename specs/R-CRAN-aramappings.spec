%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aramappings
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Computes Adaptable Radial Axes Mappings

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-clarabel 
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-glpkAPI 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
Requires:         R-CRAN-clarabel 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-glpkAPI 
Requires:         R-CRAN-Matrix 
Requires:         R-parallel 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-stats 

%description
Computes low-dimensional point representations of high-dimensional
numerical data according to the data visualization method Adaptable Radial
Axes described in: Manuel Rubio-Sánchez, Alberto Sanchez, and Dirk J.
Lehmann (2017) "Adaptable radial axes plots for improved multivariate data
visualization" <doi:10.1111/cgf.13196>.

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
