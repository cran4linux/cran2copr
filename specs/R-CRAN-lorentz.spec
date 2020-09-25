%global packname  lorentz
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          The Lorentz Transform in Relativistic Physics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-emulator >= 1.2.20
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tensor 
BuildRequires:    R-CRAN-magic 
Requires:         R-CRAN-emulator >= 1.2.20
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tensor 
Requires:         R-CRAN-magic 

%description
The Lorentz transform in special relativity; also the gyrogroup structure
of three-velocities.  Includes active and passive transforms and the
ability to use units in which the speed of light is not one.  For general
relativity, see the 'schwarzschild' package.

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
