%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggplot2.utils
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Selected Utilities Extending 'ggplot2'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggpp 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggpp 

%description
Selected utilities, in particular 'geoms' and 'stats' functions, extending
the 'ggplot2' package. Note that this package does not define the
functions itself, but instead imports them from a collection of other
packages and then exports them. These functions are tested as well to make
sure that they work reliably. Currently, the selected functions are from
'EnvStats' <doi:10.1007/978-1-4614-8456-1>, 'GGally'
<doi:10.5281/zenodo.5009047> and 'ggpp'
<https://CRAN.R-project.org/package=ggpp>.

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
