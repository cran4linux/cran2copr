%global packname  VecStatGraphs3D
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          2%{?dist}
Summary:          Vector analysis using graphical and analytical methods in 3D

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.1
Requires:         R-core >= 2.10.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-misc3d 
BuildRequires:    R-tcltk 
BuildRequires:    R-MASS 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-misc3d 
Requires:         R-tcltk 
Requires:         R-MASS 

%description
This package performs a 3D statistical analysis, both numerical and
graphical, of a set of vectors. Since a vector has three components (a
module and two angles) vectorial analysis is performed in two stages:
modules are analyzed by means of linear statistics and orientations are
analyzed by spherical statistics. Tests and spherical statistic parameters
are accompanied by a graphs as: density maps, distribution modules and
angles. The tests, spherical statistic parameters and graphs allow us
detecting another distribution properties (i.e. anisotropy) and outliers.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
