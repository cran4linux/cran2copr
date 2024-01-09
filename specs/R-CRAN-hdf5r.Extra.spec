%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hdf5r.Extra
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Extensions for 'HDF5' R Interfaces

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-hdf5r >= 1.3.8
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-easy.utils 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MatrixExtra 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-hdf5r >= 1.3.8
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-easy.utils 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MatrixExtra 
Requires:         R-CRAN-rlang 

%description
Some methods to manipulate 'HDF5' files, extending the 'hdf5r' package.
Reading and writing R objects to 'HDF5' formats follow the specification
of 'AnnData'
<https://anndata.readthedocs.io/en/latest/fileformat-prose.html>.

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
