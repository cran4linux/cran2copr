%global packname  secrlinear
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}
Summary:          Spatially Explicit Capture-Recapture for Linear Habitats

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-secr >= 3.0.1
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-secr >= 3.0.1
Requires:         R-CRAN-sp 
Requires:         R-CRAN-igraph 
Requires:         R-parallel 
Requires:         R-CRAN-maptools 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-rgdal 

%description
Tools for spatially explicit capture-recapture analysis of animal
populations in linear habitats, extending package 'secr'.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
