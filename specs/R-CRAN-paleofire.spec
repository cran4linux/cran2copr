%global __brp_check_rpaths %{nil}
%global packname  paleofire
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Charcoal Records from the Global Charcoal Database

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-GCD 
BuildRequires:    R-CRAN-locfit 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-lattice 
Requires:         R-methods 
Requires:         R-CRAN-GCD 
Requires:         R-CRAN-locfit 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rgdal 
Requires:         R-lattice 

%description
Tools to extract and analyse charcoal sedimentary data stored in the
Global Charcoal Database. Main functionalities includes data extraction
and sites selection, transformation and interpolation of the charcoal
records as well as compositing.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYING
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/THANKS
%{rlibdir}/%{packname}/INDEX
