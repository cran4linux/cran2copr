%global packname  CENFA
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Climate and Ecological Niche Factor Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-parallel >= 3.3.3
BuildRequires:    R-CRAN-raster >= 2.6.7
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-pbapply >= 1.3.3
BuildRequires:    R-CRAN-sp >= 1.2.7
BuildRequires:    R-CRAN-doSNOW >= 1.0.16
BuildRequires:    R-CRAN-snow >= 0.4.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
Requires:         R-parallel >= 3.3.3
Requires:         R-CRAN-raster >= 2.6.7
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-pbapply >= 1.3.3
Requires:         R-CRAN-sp >= 1.2.7
Requires:         R-CRAN-doSNOW >= 1.0.16
Requires:         R-CRAN-snow >= 0.4.2
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 

%description
Tools for climate- and ecological-niche factor analysis of spatial data,
including methods for visualization of spatial variability of species
sensitivity, exposure, and vulnerability to climate change. Processing of
large files and parallel methods are supported. Ecological-niche factor
analysis is described in Hirzel et al. (2002) <doi:10.2307/3071784> and
Basille et al. (2008) <doi:10.1016/j.ecolmodel.2007.09.006>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
