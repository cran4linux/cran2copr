%global packname  DiversityOccupancy
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Building Diversity Models from Multiple Species Occupancy Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-unmarked 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmulti 
BuildRequires:    R-CRAN-qpcR 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-unmarked 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmulti 
Requires:         R-CRAN-qpcR 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-vegan 

%description
Predictions of alpha diversity are fitted from presence data, first
abundance is modeled from occupancy models and then, several diversity
indices are calculated and finally GLM models are used to predict
diversity in different environments and select priority areas.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
