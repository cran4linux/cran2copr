%global packname  spatialfusion
%global packver   0.6-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          3%{?dist}
Summary:          Multivariate Analysis of Spatial Data Using a Unifying SpatialFusion Framework

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-SDraw 
BuildRequires:    R-CRAN-fields 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-SDraw 
Requires:         R-CRAN-fields 

%description
Multivariate modelling of geostatistical (point), lattice (areal) and
point pattern data in a unifying spatial fusion framework. Details are
given in Wang and Furrer (2019) <arXiv:1906.00364>. Model inference is
done using either 'Stan' <https://mc-stan.org/> or 'INLA'
<http://www.r-inla.org>.

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
%doc %{rlibdir}/%{packname}/chunks
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
