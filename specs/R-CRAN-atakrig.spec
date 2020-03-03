%global packname  atakrig
%global packver   0.9.6-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6.2
Release:          1%{?dist}
Summary:          Area-to-Area Kriging

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-snow 
Requires:         R-CRAN-FNN 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-Rcpp 

%description
Point-scale variogram deconvolution from irregular/regular spatial support
according to Goovaerts, P., (2008) <doi: 10.1007/s11004-007-9129-1>;
ordinary area-to-area (co)Kriging and area-to-point (co)Kriging.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
