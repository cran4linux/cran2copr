%global packname  spatsurv
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          3%{?dist}
Summary:          Bayesian Spatial Survival Analysis with Parametric ProportionalHazards Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-survival 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-RandomFields 
Requires:         R-CRAN-fields 
Requires:         R-Matrix 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-methods 
Requires:         R-CRAN-lubridate 

%description
Bayesian inference for parametric proportional hazards spatial survival
models; flexible spatial survival models. See Benjamin M. Taylor, Barry S.
Rowlingson (2017) <doi:10.18637/jss.v077.i04>.

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
%{rlibdir}/%{packname}/INDEX
