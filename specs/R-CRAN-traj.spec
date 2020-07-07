%global packname  traj
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          2%{?dist}
Summary:          Trajectory Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-pastecs 
BuildRequires:    R-CRAN-NbClust 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-GPArotation 
Requires:         R-cluster 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-pastecs 
Requires:         R-CRAN-NbClust 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-GPArotation 

%description
Implements the three-step procedure proposed by Leffondree et al. (2004)
to identify clusters of individual longitudinal trajectories. The
procedure involves (1) calculating 24 measures describing the features of
the trajectories; (2) using factor analysis to select a subset of the 24
measures and (3) using cluster analysis to identify clusters of
trajectories, and classify each individual trajectory in one of the
clusters.

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

%files
%{rlibdir}/%{packname}
