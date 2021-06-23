%global __brp_check_rpaths %{nil}
%global packname  riverdist
%global packver   0.15.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.15.3
Release:          2%{?dist}%{?buildtag}
Summary:          River Network Distance Computation and Applications

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp >= 1.0.15
BuildRequires:    R-CRAN-rgdal >= 0.9.1
BuildRequires:    R-methods 
Requires:         R-CRAN-sp >= 1.0.15
Requires:         R-CRAN-rgdal >= 0.9.1
Requires:         R-methods 

%description
Reads river network shape files and computes network distances. Also
included are a variety of computation and graphical tools designed for
fisheries telemetry research, such as minimum home range, kernel density
estimation, and clustering analysis using empirical k-functions with a
bootstrap envelope.  Tools are also provided for editing the river
networks, meaning there is no reliance on external software.

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
