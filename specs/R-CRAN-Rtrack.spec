%global packname  Rtrack
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Spatial Navigation Strategy Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-crayon 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Hmisc 
Requires:         R-KernSmooth 
Requires:         R-methods 
Requires:         R-CRAN-openxlsx 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
A toolkit for the analysis of paths from spatial tracking experiments
(such as the Morris water maze) and calculation of goal-finding
strategies. This package is centered on an approach using machine learning
for path classification.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
