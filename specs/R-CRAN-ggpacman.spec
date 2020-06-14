%global packname  ggpacman
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          A 'ggplot2' and 'gganimate' Version of Pac-Man

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-gganimate >= 1.0.5
BuildRequires:    R-CRAN-tidyr >= 1.0.2
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-ggforce >= 0.3.1
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-gganimate >= 1.0.5
Requires:         R-CRAN-tidyr >= 1.0.2
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-ggforce >= 0.3.1
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-stats 
Requires:         R-utils 

%description
A funny coding challenge to reproduce the game Pac-Man using 'ggplot2' and
'gganimate'. It provides a pre-defined moves set for Pac-Man and the
ghosts for the first level of the game Pac-Man as well as polygon datasets
to draw ghosts in 'ggplot2'.

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
%doc %{rlibdir}/%{packname}/fun
%{rlibdir}/%{packname}/INDEX
