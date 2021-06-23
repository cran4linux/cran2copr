%global __brp_check_rpaths %{nil}
%global packname  rvmethod
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Radial Velocity Method for Detecting Exoplanets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-locfit 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-parallel 
Requires:         R-CRAN-locfit 
Requires:         R-CRAN-assertthat 

%description
Has various functions designed to implement the Hermite-Gaussian Radial
Velocity (HGRV) estimation approach of Holzer et al. (2020)
<arXiv:2005.14083>, which is a particular application of the radial
velocity method for detecting exoplanets. The overall approach consists of
four sequential steps, each of which has a function in this package: (1)
estimate the template spectrum with the function estimate_template(), (2)
find absorption features in the estimated template with the function
findabsorptionfeatures(), (3) fit Gaussians to the absorption features
with the function Gaussfit(), (4) apply the HGRV with simple linear
regression by calling the function hgrv(). This package is meant to be
open source. But please cite the paper Holzer et al. (2020)
<arXiv:2005.14083> when publishing results that use this package.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
