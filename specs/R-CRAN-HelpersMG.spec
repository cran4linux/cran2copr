%global packname  HelpersMG
%global packver   3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.9
Release:          1%{?dist}
Summary:          Tools for Environmental Analyses, Ecotoxicology and Various RFunctions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-coda 

%description
Contains many functions useful for managing 'NetCDF' files (see
<http://en.wikipedia.org/wiki/NetCDF>), get tide levels on any point of
the globe, get moon phase and time for sun rise and fall, analyse and
reconstruct periodic time series of temperature with irregular sinusoidal
pattern, show scales and wind rose in plot with change of color of text,
Metropolis-Hastings algorithm for Bayesian MCMC analysis, plot graphs or
boxplot with error bars, search files in disk by there names or their
content, read the contents of all files from a folder at one time.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
