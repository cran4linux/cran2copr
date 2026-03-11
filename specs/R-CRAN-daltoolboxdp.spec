%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  daltoolboxdp
%global packver   1.2.747
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.747
Release:          1%{?dist}%{?buildtag}
Summary:          Deep Python Extensions for 'daltoolbox'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tspredit 
BuildRequires:    R-CRAN-daltoolbox 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-tspredit 
Requires:         R-CRAN-daltoolbox 
Requires:         R-CRAN-reticulate 

%description
Extends 'daltoolbox' with Python-backed components for deep learning,
scikit-learn classification, and time-series forecasting through
'reticulate'. The package provides objects that follow the 'daltoolbox'
architecture while delegating model creation, fitting, encoding, and
prediction to Python libraries such as 'torch' and 'scikit-learn'. In the
package name, 'dp' stands for 'Deep Python'. The overall workflow is
inspired by the Experiment Lines approach described in Ogasawara et al.
(2009) <doi:10.1007/978-3-642-02279-1_20>.

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
