%global packname  SpatialVx
%global packver   0.6-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.5
Release:          3%{?dist}
Summary:          Spatial Forecast Verification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fields >= 6.8
BuildRequires:    R-CRAN-spatstat >= 1.37.0
BuildRequires:    R-CRAN-smoothie 
BuildRequires:    R-CRAN-smatr 
BuildRequires:    R-CRAN-turboEM 
BuildRequires:    R-CRAN-distillery 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-CircStats 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-waveslim 
Requires:         R-CRAN-fields >= 6.8
Requires:         R-CRAN-spatstat >= 1.37.0
Requires:         R-CRAN-smoothie 
Requires:         R-CRAN-smatr 
Requires:         R-CRAN-turboEM 
Requires:         R-CRAN-distillery 
Requires:         R-CRAN-maps 
Requires:         R-boot 
Requires:         R-CRAN-CircStats 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-waveslim 

%description
Spatial forecast verification arose from verifying high-resolution
forecasts, where coarser-resolution models generally are favored even when
a human forecaster finds the higher-resolution model to be considerably
better.  Most newly proposed methods, which largely come from image
analysis, computer vision, and similar, are available, with more on the
way.

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
%{rlibdir}/%{packname}/INDEX
