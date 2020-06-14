%global packname  actel
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Acoustic Telemetry Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-DiagrammeRsvg 
BuildRequires:    R-CRAN-fasttime 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-svglite 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rsvg 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-DiagrammeRsvg 
Requires:         R-CRAN-fasttime 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-svglite 
Requires:         R-graphics 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rsvg 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Designed for studies where fish tagged with acoustic tags are expected to
move through receiver arrays. This package combines the advantages of
automatic sorting and checking of fish movements with the possibility for
user intervention on tags that deviate from expected behaviour. The three
analysis functions (explore(), migration() and residency()) allow the
users to analyse their data in a systematic way, making it easy to compare
results from different studies. CJS calculations are based on Perry et al.
(2012)
<https://www.researchgate.net/publication/256443823_Using_mark-recapture_models_to_estimate_survival_from_telemetry_data>.

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
%doc %{rlibdir}/%{packname}/example_shapefile.cpg
%doc %{rlibdir}/%{packname}/example_shapefile.dbf
%doc %{rlibdir}/%{packname}/example_shapefile.prj
%doc %{rlibdir}/%{packname}/example_shapefile.qpj
%doc %{rlibdir}/%{packname}/example_shapefile.shp
%doc %{rlibdir}/%{packname}/example_shapefile.shx
%doc %{rlibdir}/%{packname}/example_spatial.csv
%{rlibdir}/%{packname}/INDEX
