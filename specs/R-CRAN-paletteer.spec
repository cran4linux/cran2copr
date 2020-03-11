%global packname  paletteer
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Comprehensive Collection of Color Palettes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggthemes >= 4.0.0
BuildRequires:    R-CRAN-harrypotter >= 2.1.0
BuildRequires:    R-CRAN-gameofthrones >= 1.0.0
BuildRequires:    R-CRAN-jcolors 
BuildRequires:    R-CRAN-oompaBase 
BuildRequires:    R-CRAN-palr 
BuildRequires:    R-CRAN-pals 
BuildRequires:    R-CRAN-scico 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rematch2 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-prismatic 
Requires:         R-CRAN-ggthemes >= 4.0.0
Requires:         R-CRAN-harrypotter >= 2.1.0
Requires:         R-CRAN-gameofthrones >= 1.0.0
Requires:         R-CRAN-jcolors 
Requires:         R-CRAN-oompaBase 
Requires:         R-CRAN-palr 
Requires:         R-CRAN-pals 
Requires:         R-CRAN-scico 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rematch2 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-prismatic 

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
