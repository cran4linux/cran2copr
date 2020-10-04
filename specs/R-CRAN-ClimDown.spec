%global packname  ClimDown
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Climate Downscaling Library for Daily Climate Model Output

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-PCICt 
BuildRequires:    R-CRAN-udunits2 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-seas 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-stats 
Requires:         R-CRAN-PCICt 
Requires:         R-CRAN-udunits2 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-seas 
Requires:         R-CRAN-abind 
Requires:         R-stats 

%description
A suite of routines for downscaling coarse scale global climate model
(GCM) output to a fine spatial resolution. Includes Bias-Corrected Spatial
Downscaling (BCDS), Constructed Analogues (CA), Climate Imprint (CI), and
Bias Correction/Constructed Analogues with Quantile mapping reordering
(BCCAQ). Developed by the the Pacific Climate Impacts Consortium (PCIC),
Victoria, British Columbia, Canada.

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
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/exec
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
