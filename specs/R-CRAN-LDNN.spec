%global __brp_check_rpaths %{nil}
%global packname  LDNN
%global packver   1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Longitudinal Data Neural Network

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-tensorflow 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-tensorflow 

%description
This is a Neural Network regression model implementation using 'Keras',
consisting of 10 Long Short-Term Memory layers that are fully connected
along with the rest of the inputs.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
