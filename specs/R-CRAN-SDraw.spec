%global packname  SDraw
%global packver   2.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.8
Release:          1%{?dist}
Summary:          Spatially Balanced Samples of Spatial Objects

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spsurvey 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-stats 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spsurvey 
Requires:         R-utils 
Requires:         R-CRAN-rgeos 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-deldir 
Requires:         R-stats 

%description
Routines for drawing samples from spatial objects, focused on spatially
balanced algorithms. Draws Halton Iterative Partition (HIP) (Robertson et
al., 2018; <doi:10.1007/s10651-018-0406-6>), Balanced Acceptance Samples
(BAS) (Robertson et al., 2013; <doi:10.1111/biom.12059>), Generalized
Random Tessellation Stratified (GRTS) (Stevens and Olsen, 2004;
<doi:10.1198/016214504000000250>), Simple Systematic Samples (SSS) and
Simple Random Samples (SRS) from point, line, and polygon resources.
Frames are 'SpatialPoints', 'SpatialLines', or 'SpatialPolygons' objects
from package 'sp'.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
