%global packname  SK
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}
Summary:          Segment-Based Ordinary Kriging and Segment-Based RegressionKriging for Spatial Prediction

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-GD 
BuildRequires:    R-CRAN-rtop 
BuildRequires:    R-CRAN-FitAR 
BuildRequires:    R-MASS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-GD 
Requires:         R-CRAN-rtop 
Requires:         R-CRAN-FitAR 
Requires:         R-MASS 

%description
Segment-based Kriging methods, including segment-based ordinary Kriging
(SOK) and segment-based regression Kriging (SRK) for spatial prediction of
line segment spatial data as described in Yongze Song (2018)
<doi:10.1109/TITS.2018.2805817>. Includes the spatial prediction and
spatial visualisation. The descriptions of the methods and case datasets
refer to the citation information below.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
