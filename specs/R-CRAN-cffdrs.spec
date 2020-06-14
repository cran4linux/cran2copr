%global packname  cffdrs
%global packver   1.8.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.18
Release:          2%{?dist}
Summary:          Canadian Forest Fire Danger Rating System

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-doParallel 

%description
This project provides a group of new functions to calculate the outputs of
the two main components of the Canadian Forest Fire Danger Rating System
(CFFDRS) Van Wagner and Pickett (1985)
<https://cfs.nrcan.gc.ca/publications?id=19973>) at various time scales:
the Fire Weather Index (FWI) System Wan Wagner (1985)
<https://cfs.nrcan.gc.ca/publications?id=19927> and the Fire Behaviour
Prediction (FBP) System Forestry Canada Fire Danger Group (1992)
<http://cfs.nrcan.gc.ca/pubwarehouse/pdfs/10068.pdf>. Some functions have
two versions, table and raster based.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
