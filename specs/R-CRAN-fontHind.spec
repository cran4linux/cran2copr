%global packname  fontHind
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Additional 'ggplot2' Themes Using 'Hind' Fonts

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-hrbrthemes 
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-hrbrthemes 
Requires:         R-CRAN-extrafont 
Requires:         R-CRAN-ggplot2 

%description
Provides 'ggplot2' themes based on the 'Hind' fonts. 'Hind' is an open
source 'typeface' supporting the 'Devanagari' and Latin scripts. Developed
explicitly for use in User Interface design, the 'Hind' font family
includes five styles. More information about the font can be found at
<https://fonts.google.com/specimen/Hind>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/fonts
%{rlibdir}/%{packname}/INDEX
