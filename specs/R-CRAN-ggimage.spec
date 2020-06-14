%global packname  ggimage
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          2%{?dist}
Summary:          Use Image in 'ggplot2'

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rvcheck >= 0.1.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
Requires:         R-CRAN-rvcheck >= 0.1.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggplotify 
Requires:         R-grid 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magick 
Requires:         R-methods 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tibble 
Requires:         R-tools 

%description
Supports image files and graphic objects to be visualized in 'ggplot2'
graphic system.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
