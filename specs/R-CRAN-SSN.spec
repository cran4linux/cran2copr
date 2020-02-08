%global packname  SSN
%global packver   1.1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.13
Release:          1%{?dist}
Summary:          Spatial Modeling on Stream Networks

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-rgdal >= 1.2.5
BuildRequires:    R-CRAN-RSQLite >= 1.1.2
BuildRequires:    R-CRAN-igraph >= 1.0.0
BuildRequires:    R-CRAN-rgeos >= 0.3.22
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-lattice 
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-rgdal >= 1.2.5
Requires:         R-CRAN-RSQLite >= 1.1.2
Requires:         R-CRAN-igraph >= 1.0.0
Requires:         R-CRAN-rgeos >= 0.3.22
Requires:         R-CRAN-sp 
Requires:         R-MASS 
Requires:         R-CRAN-maptools 
Requires:         R-lattice 
Requires:         R-methods 
Requires:         R-Matrix 

%description
Spatial statistical modeling and prediction for data on stream networks,
including models based on in-stream distance (Ver Hoef, J.M. and Peterson,
E.E., 2010. <DOI:10.1198/jasa.2009.ap08248>.) Models are created using
moving average constructions. Spatial linear models, including explanatory
variables, can be fit with (restricted) maximum likelihood.  Mapping and
other graphical functions are included.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/lsndata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
