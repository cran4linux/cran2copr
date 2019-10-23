%global packname  CensSpatial
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Censored Spatial Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-geoR 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-lattice 
Requires:         R-CRAN-geoR 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-moments 
Requires:         R-lattice 

%description
Fits linear regression models for censored spatial data. Provides
different estimation methods as the SAEM (Stochastic Approximation of
Expectation Maximization) algorithm and seminaive that uses Kriging
prediction to estimate the response at censored locations and predict new
values at unknown locations. Also offers graphical tools for assessing the
fitted model.

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
