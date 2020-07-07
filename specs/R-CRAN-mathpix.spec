%global packname  mathpix
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          2%{?dist}
Summary:          Support for the 'Mathpix' API (Image to 'LaTeX')

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-texPreview 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-texPreview 
Requires:         R-CRAN-magick 
Requires:         R-utils 

%description
Given an image of a formula (typeset or handwritten) this package provides
calls to the 'Mathpix' service to produce the 'LaTeX' code which should
generate that image, and pastes it into a (e.g. an 'rmarkdown') document.
See <https://docs.mathpix.com/> for full details. 'Mathpix' is an external
service and use of the API is subject to their terms and conditions.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
