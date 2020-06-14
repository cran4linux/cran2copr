%global packname  eRTG3D
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          2%{?dist}
Summary:          Empirically Informed Random Trajectory Generation in 3-D

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.9.0
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-raster >= 2.9.5
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-pbapply >= 1.4.1
BuildRequires:    R-CRAN-sp >= 1.3.1
BuildRequires:    R-CRAN-rasterVis >= 0.45
BuildRequires:    R-CRAN-CircStats >= 0.2.6
BuildRequires:    R-CRAN-tiff >= 0.1.5
Requires:         R-CRAN-plotly >= 4.9.0
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-raster >= 2.9.5
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-pbapply >= 1.4.1
Requires:         R-CRAN-sp >= 1.3.1
Requires:         R-CRAN-rasterVis >= 0.45
Requires:         R-CRAN-CircStats >= 0.2.6
Requires:         R-CRAN-tiff >= 0.1.5

%description
Creates realistic random trajectories in a 3-D space between two given fix
points, so-called conditional empirical random walks (CERWs). The
trajectory generation is based on empirical distribution functions
extracted from observed trajectories (training data) and thus reflects the
geometrical movement characteristics of the mover. A digital elevation
model (DEM), representing the Earth's surface, and a background layer of
probabilities (e.g. food sources, uplift potential, waterbodies, etc.) can
be used to influence the trajectories. Unterfinger M (2018). "3-D
Trajectory Simulation in Movement Ecology: Conditional Empirical Random
Walk". Master's thesis, University of Zurich.
<https://www.geo.uzh.ch/dam/jcr:6194e41e-055c-4635-9807-53c5a54a3be7/MasterThesis_Unterfinger_2018.pdf>.
Technitis G, Weibel R, Kranstauber B, Safi K (2016). "An algorithm for
empirically informed random trajectory generation between two endpoints".
GIScience 2016: Ninth International Conference on Geographic Information
Science, 9, online. <doi:10.5167/uzh-130652>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
