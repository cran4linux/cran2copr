%global packname  iemisc
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          1%{?dist}
Summary:          Irucka Embry's Miscellaneous Functions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.10.2
BuildRequires:    R-CRAN-gsubfn >= 0.7
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-iemiscdata 
BuildRequires:    R-CRAN-import 
BuildRequires:    R-CRAN-fpCompare 
BuildRequires:    R-CRAN-listless 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-CHNOSZ 
BuildRequires:    R-CRAN-IAPWS95 
BuildRequires:    R-CRAN-testit 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-data.table >= 1.10.2
Requires:         R-CRAN-gsubfn >= 0.7
Requires:         R-stats 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-iemiscdata 
Requires:         R-CRAN-import 
Requires:         R-CRAN-fpCompare 
Requires:         R-CRAN-listless 
Requires:         R-CRAN-units 
Requires:         R-CRAN-CHNOSZ 
Requires:         R-CRAN-IAPWS95 
Requires:         R-CRAN-testit 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 

%description
A collection of Irucka Embry's miscellaneous functions (Engineering
Economics, Civil & Environmental/Water Resources Engineering, Geometry,
Statistics, GNU Octave length functions, Trigonometric functions in
degrees, etc.).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
