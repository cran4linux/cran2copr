%global packname  elsa
%global packver   1.1-28
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.28
Release:          2%{?dist}
Summary:          Entropy-Based Local Indicator of Spatial Association

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-sp >= 1.2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
Requires:         R-CRAN-sp >= 1.2.0
Requires:         R-methods 
Requires:         R-CRAN-raster 

%description
A framework that provides the methods for quantifying entropy-based local
indicator of spatial association (ELSA) that can be used for both
continuous and categorical data. In addition, this package offers other
methods to measure local indicators of spatial associations (LISA).
Furthermore, global spatial structure can be measured using a
variogram-like diagram, called entrogram. For more information, please
check that paper: Naimi, B., Hamm, N. A., Groen, T. A., Skidmore, A. K.,
Toxopeus, A. G., & Alibakhshi, S. (2019)
<doi:10.1016/j.spasta.2018.10.001>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/external
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
