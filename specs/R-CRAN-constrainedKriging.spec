%global packname  constrainedKriging
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          Constrained, Covariance-Matching Constrained and Universal Pointor Block Kriging

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildRequires:    R-CRAN-RandomFields >= 1.3.41
BuildRequires:    R-CRAN-sp >= 0.9.60
BuildRequires:    R-CRAN-spatialCovariance >= 0.6.4
BuildRequires:    R-CRAN-rgeos >= 0.2.17
BuildRequires:    R-methods 
Requires:         R-CRAN-RandomFields >= 1.3.41
Requires:         R-CRAN-sp >= 0.9.60
Requires:         R-CRAN-spatialCovariance >= 0.6.4
Requires:         R-CRAN-rgeos >= 0.2.17
Requires:         R-methods 

%description
Provides functions for efficient computations of nonlinear spatial
predictions with local change of support. This package supplies functions
for tow-dimensional spatial interpolation by constrained,
covariance-matching constrained and universal (external drift) kriging for
points or block of any shape for data with a nonstationary mean function
and an isotropic weakly stationary variogram. The linear spatial
interpolation methods, constrained and covariance-matching constrained
kriging, provide approximately unbiased prediction for nonlinear target
values under change of support. This package extends the range of
geostatistical tools available in R and provides a veritable alternative
to conditional simulation for nonlinear spatial prediction problems with
local change of support.

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
%doc %{rlibdir}/%{packname}/ChangeLog.txt
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
