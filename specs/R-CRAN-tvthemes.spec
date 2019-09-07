%global packname  tvthemes
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          TV Show Themes and Color Palettes for 'ggplot2' Graphics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grDevices >= 3.5.3
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-magick >= 2.0
BuildRequires:    R-CRAN-glue >= 1.3.1
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-extrafont >= 0.17
Requires:         R-grDevices >= 3.5.3
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-magick >= 2.0
Requires:         R-CRAN-glue >= 1.3.1
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-extrafont >= 0.17

%description
Contains various 'ggplot2' themes and color palettes based on TV shows
such as 'Game of Thrones', 'Brooklyn Nine-Nine', 'Avatar: The Last
Airbender', 'Spongebob Squarepants', and more.

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
%doc %{rlibdir}/%{packname}/backgrounds
%doc %{rlibdir}/%{packname}/fonts
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
