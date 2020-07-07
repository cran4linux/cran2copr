%global packname  disaggregation
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}
Summary:          Disaggregation Modelling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-sparseMVN 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-sp 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-rgdal 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-sparseMVN 
Requires:         R-utils 

%description
Fits disaggregation regression models using 'TMB' ('Template Model
Builder'). When the response data are aggregated to polygon level but the
predictor variables are at a higher resolution, these models can be
useful. Regression models with spatial random fields. A useful reference
for disaggregation modelling is Lucas et al. (2019) <doi:10.1101/548719>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
