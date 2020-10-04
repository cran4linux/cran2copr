%global packname  mvmesh
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Multivariate Meshes and Histograms in Arbitrary Dimensions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rcdd 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-SimplicialCubature 
Requires:         R-CRAN-rcdd 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-SimplicialCubature 

%description
Define, manipulate and plot meshes on simplices, spheres, balls,
rectangles and tubes. Directional and other multivariate histograms are
provided.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
