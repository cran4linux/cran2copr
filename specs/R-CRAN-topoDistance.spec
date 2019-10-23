%global packname  topoDistance
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Calculating Topographic Paths and Distances

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-gdistance 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-gdistance 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sp 

%description
A toolkit for calculating topographic distances and identifying and
plotting topographic paths. Topographic distances can be calculated along
shortest topographic paths (Wang (2009)
<doi:10.1111/j.1365-294X.2009.04338.x>), weighted topographic paths (Zhan
et al. (1993) <doi:10.1007/3-540-57207-4_29>), and topographic least cost
paths (Wang and Summers (2010) <doi:10.1111/j.1365-294X.2009.04465.x>).
Functions can map topographic paths on colored or hill shade maps and plot
topographic cross sections (elevation profiles) for the paths.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
