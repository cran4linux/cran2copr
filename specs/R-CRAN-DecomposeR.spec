%global packname  DecomposeR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Empirical Mode Decomposition for Cyclostratigraphy

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-StratigrapheR >= 1.0.1
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-hht 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-StratigrapheR >= 1.0.1
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-hht 
Requires:         R-grid 
Requires:         R-CRAN-hexbin 
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-dplyr 

%description
Tools to apply Ensemble Empirical Mode Decomposition (EEMD) for
cyclostratigraphy purposes. Mainly: a new algorithm, extricate, that
performs EEMD in seconds, a linear interpolation algorithm using the
greatest rational common divisor of depth or time, different algorithms to
compute instantaneous amplitude, frequency and ratios of frequencies, and
functions to verify and visualise the outputs. The functions were
developed during the CRASH project (Checking the Reproducibility of
Astrochronology in the Hauterivian). When using for publication please
cite Wouters, S., Da Silva, A.C. Crucifix, M., Sinnesael, M., Zivanovic,
M., Boulvain, F., Devleeschouwer, X., 2019, "Litholog generation with the
'StratigrapheR' package and signal decomposition for cyclostratigraphic
purposes". Geophysical Research Abstracts Vol. 21, EGU2019-5520, 2019, EGU
General Assembly 2019. <http://hdl.handle.net/2268/234402>.

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
%{rlibdir}/%{packname}/INDEX
