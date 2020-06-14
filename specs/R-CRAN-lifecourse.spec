%global packname  lifecourse
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          2%{?dist}
Summary:          Quantification of Lifecourse Fluidity

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-TraMineR 
BuildRequires:    R-graphics 
Requires:         R-CRAN-TraMineR 
Requires:         R-graphics 

%description
Provides in built datasets and three functions. These functions are
mobility_index, nonStanTest and linkedLives.  The mobility_index function
facilitates the calculation of lifecourse fluidity, whilst the nonStanTest
and the linkedLives functions allow the user to determine the probability
that the observed sequence data was due to chance.  The linkedLives
function acknowledges the fact that some individuals may have identical
sequences. The datasets available provide sequence data on marital
status(maritalData) and mobility (mydata) for a selected group of
individuals from the British Household Panel Study (BHPS).  In addition,
personal and house ID's for 100 individuals are provided in a third
dataset (myHouseID) from the BHPS.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
