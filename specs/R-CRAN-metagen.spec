%global packname  metagen
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Inference in Meta Analysis and Meta Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-ParamHelpers 
BuildRequires:    R-CRAN-BatchJobs 
BuildRequires:    R-CRAN-BatchExperiments 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-metafor 
Requires:         R-MASS 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-ParamHelpers 
Requires:         R-CRAN-BatchJobs 
Requires:         R-CRAN-BatchExperiments 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-metafor 

%description
Provides methods for making inference in the random effects meta
regression model such as point estimates and confidence intervals for the
heterogeneity parameter and the regression coefficients vector.  Inference
methods are based on different approaches to statistical inference.
Methods from three different schools are included: methods based on the
method of moments approach, methods based on likelihood, and methods based
on generalised inference.  The package also includes tools to run
extensive simulation studies in parallel on high performance clusters in a
modular way.  This allows extensive testing of custom inferential methods
with all implemented state-of-the-art methods in a standardised way.
Tools for evaluating the performance of both point and interval estimates
are provided.  Also, a large collection of different pre-defined plotting
functions is implemented in a ready-to-use fashion.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
