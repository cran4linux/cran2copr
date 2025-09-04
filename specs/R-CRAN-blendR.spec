%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blendR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Blended Survival Curves

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-manipulate 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-survHE 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-manipulate 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-survHE 
Requires:         R-CRAN-tibble 

%description
Create a blended curve from two survival curves, which is particularly
useful for survival extrapolation in health technology assessment. The
main idea is to mix a flexible model that fits the observed data well with
a parametric model that encodes assumptions about long-term survival. The
two curves are blended into a single survival curve that is identical to
the first model over the range of observed times and gradually approaches
the parametric model over the extrapolation period based on a given weight
function. This approach allows for the inclusion of external information,
such as data from registries or expert opinion, to guide long-term
extrapolations, especially when dealing with immature trial data. See Che
et al. (2022) <doi:10.1177/0272989X221134545>.

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
