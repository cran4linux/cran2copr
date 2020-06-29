%global packname  GD
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          1%{?dist}
Summary:          Geographical Detectors for Assessing Spatial Factors

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-badger 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-badger 

%description
Geographical detectors for measuring spatial stratified heterogeneity, as
described in Jinfeng Wang (2010) <doi:10.1080/13658810802443457> and
Jinfeng Wang (2016) <doi:10.1016/j.ecolind.2016.02.052>. Includes the
optimal discretization of continuous data, four primary functions of
geographical detectors, comparison of size effects of spatial unit and the
visualizations of results. To use the package and to refer the
descriptions of the package, methods and case datasets, please cite Yongze
Song (2020) <doi:10.1080/15481603.2020.1760434>. The model has been
applied in factor exploration of road performance and multi-scale spatial
segmentation for network data, as described in Yongze Song (2018)
<doi:10.3390/rs10111696> and Yongze Song (2020)
<doi:10.1109/TITS.2020.3001193>, respectively.

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
