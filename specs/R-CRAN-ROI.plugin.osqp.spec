%global __brp_check_rpaths %{nil}
%global packname  ROI.plugin.osqp
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          'osqp' Plugin for the 'R' Optimization Infrastructure

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ROI >= 0.2.5
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-ROI >= 0.2.5
Requires:         R-methods 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-osqp 
Requires:         R-Matrix 

%description
Enhances the 'R' Optimization Infrastructure ('ROI') package with the
quadratic solver 'OSQP'. More information about 'OSQP' can be found at
<https://osqp.org>.

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
