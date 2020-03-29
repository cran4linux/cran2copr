%global packname  autoimage
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Multiple Heat Maps for Projected Coordinates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-MBA 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-mapproj 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-MBA 

%description
Functions for displaying multiple images or scatterplots with a color
scale, i.e., heat maps, possibly with projected coordinates.  The package
relies on the base graphics system, so graphics are rendered rapidly.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
