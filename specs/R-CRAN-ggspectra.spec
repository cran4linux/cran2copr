%global __brp_check_rpaths %{nil}
%global packname  ggspectra
%global packver   0.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          Extensions to 'ggplot2' for Radiation Spectra

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-tibble >= 3.0.3
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-tidyr >= 1.0.2
BuildRequires:    R-CRAN-ggrepel >= 0.8.2
BuildRequires:    R-CRAN-photobiologyWavebands >= 0.4.3
BuildRequires:    R-CRAN-photobiology >= 0.10.5
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-tibble >= 3.0.3
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-tidyr >= 1.0.2
Requires:         R-CRAN-ggrepel >= 0.8.2
Requires:         R-CRAN-photobiologyWavebands >= 0.4.3
Requires:         R-CRAN-photobiology >= 0.10.5

%description
Additional annotations, stats, geoms and scales for plotting "light"
spectra with 'ggplot2', together with specializations of ggplot() and
autoplot() methods for spectral data and waveband definitions stored in
objects of classes defined in package 'photobiology'. Part of the
'r4photobiology' suite, Aphalo P. J. (2015)
<doi:10.19232/uv4pb.2015.1.14>.

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
