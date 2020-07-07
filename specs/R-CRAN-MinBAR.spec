%global packname  MinBAR
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}
Summary:          Determining the Minimal Background Area for Species DistributionModels

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ecospat >= 2.2
BuildRequires:    R-CRAN-geosphere >= 1.5.5
BuildRequires:    R-CRAN-dismo >= 1.1.4
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-maxnet 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
Requires:         R-CRAN-ecospat >= 2.2
Requires:         R-CRAN-geosphere >= 1.5.5
Requires:         R-CRAN-dismo >= 1.1.4
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-maxnet 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 

%description
A versatile tool that aims at (1) defining what is the minimum background
extent necessary to fit good partial species distribution models and/or
(2) determining if the background area used to fit a partial species
distribution model is reliable enough to extract ecologically relevant
conclusions from it. See Rotllan-Puig, X. & Traveset, A. (2019)
<doi:10.1101/571182>.

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
