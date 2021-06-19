%global packname  wsyn
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Wavelet Approaches to Studies of Synchrony in Ecology and Other Fields

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fields >= 9.6
BuildRequires:    R-CRAN-MASS >= 7.3.47
BuildRequires:    R-graphics >= 3.4.4
BuildRequires:    R-grDevices >= 3.4.4
BuildRequires:    R-stats >= 3.4.4
Requires:         R-CRAN-fields >= 9.6
Requires:         R-CRAN-MASS >= 7.3.47
Requires:         R-graphics >= 3.4.4
Requires:         R-grDevices >= 3.4.4
Requires:         R-stats >= 3.4.4

%description
Tools for a wavelet-based approach to analyzing spatial synchrony,
principally in ecological data. Some tools will be useful for studying
community synchrony. See, for instance, Sheppard et al (2016) <doi:
10.1038/NCLIMATE2991>, Sheppard et al (2017) <doi:
10.1051/epjnbp/2017000>, Sheppard et al (2019) <doi:
10.1371/journal.pcbi.1006744>.

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
