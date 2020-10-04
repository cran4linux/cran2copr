%global packname  bdvis
%global packver   0.2.22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.22
Release:          3%{?dist}%{?buildtag}
Summary:          Biodiversity Data Visualizations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-taxize 
BuildRequires:    R-CRAN-treemap 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-leafletR 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-taxize 
Requires:         R-CRAN-treemap 
Requires:         R-CRAN-ggplot2 
Requires:         R-lattice 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-leafletR 
Requires:         R-CRAN-rgdal 

%description
Provides a set of functions to create basic visualizations to quickly
preview different aspects of biodiversity information such as inventory
completeness, extent of coverage (taxonomic, temporal and geographic),
gaps and biases.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
