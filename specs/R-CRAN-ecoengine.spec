%global packname  ecoengine
%global packver   1.12.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.12.0
Release:          1%{?dist}
Summary:          Programmatic Interface to the Web Service Methods Provided by UCBerkeley's Natural History Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 0.3
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-whisker 
Requires:         R-CRAN-httr >= 0.3
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-whisker 

%description
The ecoengine ('ecoengine'; <https://ecoengine.berkeley.edu/>). provides
access to more than 5 million georeferenced specimen records from the
University of California, Berkeley's Natural History Museums.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/browse_photos.png
%doc %{rlibdir}/%{packname}/figure
%doc %{rlibdir}/%{packname}/map.png
%doc %{rlibdir}/%{packname}/sensor_plot.png
%doc %{rlibdir}/%{packname}/Using_ecoengine.html
%doc %{rlibdir}/%{packname}/Using_ecoengine.md
%doc %{rlibdir}/%{packname}/Using_ecoengine.pdf
%doc %{rlibdir}/%{packname}/Using_ecoengine.Rmd
%{rlibdir}/%{packname}/INDEX
