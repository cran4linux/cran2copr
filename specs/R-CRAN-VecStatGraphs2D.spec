%global __brp_check_rpaths %{nil}
%global packname  VecStatGraphs2D
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          3%{?dist}%{?buildtag}
Summary:          Vector Analysis using Graphical and Analytical Methods in 2D

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.1
Requires:         R-core >= 2.10.1
BuildArch:        noarch
BuildRequires:    R-MASS 
Requires:         R-MASS 

%description
A 2D statistical analysis is performed, both numerical and graphical, of a
set of vectors. Since a vector has two components (module and azimuth)
vector analysis is performed in three stages: modules are analyzed by
means of linear statistics, azimuths are analyzed by circular statistics,
and the joint analysis of modules and azimuths is done using density maps
that allow detecting another distribution properties (i.e. anisotropy) and
outliers. Tests and circular statistic parameters have associated a full
range of graphing: histograms, maps of distributions, point maps, vector
maps, density maps, distribution modules and azimuths.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
