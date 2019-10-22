%global packname  RanglaPunjab
%global packver   2.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.4
Release:          1%{?dist}
Summary:          Displays Palette of 5 Colors

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-tidyverse 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-tidyverse 

%description
Displays palette of 5 colors based on photos depicting the unique and
vibrant culture of Punjab in Northern India. Since Punjab translates to
``Land of 5 Rivers'' there are 5 colors per palette. If users need more
than 5 colors, they can merge 2 to 3 palettes to create their own
color-combination, or they can cherry-pick their own custom colors. Users
can view up to 3 palettes together. Users can also list all the palette
choices. And last but not least, users can see the photo that inspired a
particular palette.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/img
%{rlibdir}/%{packname}/INDEX
