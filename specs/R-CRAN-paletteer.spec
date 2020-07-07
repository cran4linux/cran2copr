%global packname  paletteer
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}
Summary:          Comprehensive Collection of Color Palettes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-prismatic 
BuildRequires:    R-CRAN-rematch2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-prismatic 
Requires:         R-CRAN-rematch2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rstudioapi 

%description
The choices of color palettes in R can be quite overwhelming with palettes
spread over many packages with many different API's. This packages aims to
collect all color palettes across the R ecosystem under the same package
with a streamlined API.

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
%doc %{rlibdir}/%{packname}/AUTHORS
%{rlibdir}/%{packname}/INDEX
