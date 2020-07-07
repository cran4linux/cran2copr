%global packname  RFmerge
%global packver   0.1-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.10
Release:          3%{?dist}
Summary:          Merging of Satellite Datasets with Ground Observations usingRandom Forests

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-zoo 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-pbapply 

%description
S3 implementation of the Random Forest MErging Procedure (RF-MEP), which
combines two or more satellite-based datasets (e.g., precipitation
products, topography) with ground observations to produce a new dataset
with improved spatio-temporal distribution of the target field. In
particular, this package was developed to merge different Satellite-based
Rainfall Estimates (SREs) with measurements from rain gauges, in order to
obtain a new precipitation dataset where the time series in the rain
gauges are used to correct different types of errors present in the SREs.
However, this package might be used to merge other
hydrological/environmental satellite fields with point observations. For
details, see Baez-Villanueva et al. (2020)
<doi:10.1016/j.rse.2019.111606>. Bugs / comments / questions /
collaboration of any kind are very welcomed.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
