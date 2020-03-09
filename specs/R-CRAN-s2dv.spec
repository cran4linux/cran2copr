%global packname  s2dv
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          A Set of Common Tools for Seasonal to Decadal Verification

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-CRAN-multiApply >= 2.0.0
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-GEOmap 
BuildRequires:    R-CRAN-geomapdata 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ClimProjDiags 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ncdf4 
Requires:         R-CRAN-multiApply >= 2.0.0
Requires:         R-CRAN-maps 
Requires:         R-methods 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-GEOmap 
Requires:         R-CRAN-geomapdata 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-mapproj 
Requires:         R-parallel 
Requires:         R-CRAN-ClimProjDiags 
Requires:         R-stats 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ncdf4 

%description
The advanced version of package 's2dverification', which the details can
be found in Manubens et al. (2018) <doi:10.1016/j.envsoft.2018.01.018>. It
is intended for 'seasonal to decadal' (s2d) climate forecast verification,
but it can also be used in other kinds of forecasts or general climate
analysis. This package is specially designed for the comparison between
the experimental and observational datasets. The functionality of the
included functions covers from data retrieval, data post-processing, skill
scores against observation, to visualization. Compared to
's2dverification', 's2dv' is more compatible with the package 'startR',
able to use multiple cores for computation and handle multi-dimensional
arrays with a higher flexibility.

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
%doc %{rlibdir}/%{packname}/config
%{rlibdir}/%{packname}/INDEX
