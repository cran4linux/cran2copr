%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hyper.fit
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          N-Dimensional Hyperplane Fitting with Errors

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildArch:        noarch
BuildRequires:    R-CRAN-magicaxis 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-LaplacesDemon 
Requires:         R-CRAN-magicaxis 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-LaplacesDemon 

%description
High level functions for hyperplane fitting (hyper.fit()) and visualising
(hyper.plot2d() / hyper.plot3d()). In simple terms this allows the user to
produce robust 1D linear fits for 2D x vs y type data, and robust 2D plane
fits to 3D x vs y vs z type data. This hyperplane fitting works
generically for any N-1 hyperplane model being fit to a N dimension
dataset. All fits include intrinsic scatter in the generative model
orthogonal to the hyperplane.

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
