%global packname  ForestTools
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}
Summary:          Analyzing Remotely Sensed Forest Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-radiomics 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-APfun 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgeos 
Requires:         R-methods 
Requires:         R-CRAN-radiomics 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doSNOW 
Requires:         R-parallel 
Requires:         R-CRAN-APfun 

%description
Provides tools for analyzing remotely sensed forest data, including
functions for detecting treetops from canopy models (Popescu & Wynne,
2004), outlining tree crowns (Meyer & Beucher, 1990) and generating
spatial statistics.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
