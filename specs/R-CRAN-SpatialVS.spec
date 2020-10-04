%global packname  SpatialVS
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Spatial Variable Selection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-fields 
Requires:         R-MASS 
Requires:         R-nlme 
Requires:         R-CRAN-fields 

%description
Perform variable selection for the spatial Poisson regression model under
the adaptive elastic net penalty. Spatial count data with covariates is
the input. We use a spatial Poisson regression model to link the spatial
counts and covariates. For maximization of the likelihood under adaptive
elastic net penalty, we implemented the penalized quasi-likelihood (PQL)
and the approximate penalized loglikelihood (APL) methods. The proposed
methods can automatically select important covariates, while adjusting for
possible spatial correlations among the responses. More details are
available in Xie et al. (2018, <arXiv:1809.06418>). The package also
contains the Lyme disease dataset, which consists of the disease case data
from 2006 to 2011, and demographic data and land cover data in Virginia.
The Lyme disease case data were collected by the Virginia Department of
Health. The demographic data (e.g., population density, median income, and
average age) are from the 2010 census. Land cover data were obtained from
the Multi-Resolution Land Cover Consortium for 2006.

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
