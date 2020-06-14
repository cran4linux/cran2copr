%global packname  ppitables
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          2%{?dist}
Summary:          Lookup Tables to Generate Poverty Likelihoods and Rates usingthe Poverty Probability Index (PPI)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
The Poverty Probability Index (PPI) is a poverty measurement tool for
organizations and businesses with a mission to serve the poor. The PPI is
statistically-sound, yet simple to use: the answers to 10 questions about
a household’s characteristics and asset ownership are scored to compute
the likelihood that the household is living below the poverty line – or
above by only a narrow margin. This package contains country-specific
lookup data tables used as reference to determine the poverty likelihood
of a household based on their score from the country-specific PPI
questionnaire. These lookup tables have been extracted from documentation
of the PPI found at <https://www.povertyindex.org> and managed by
Innovations for Poverty Action <https://www.poverty-action.org>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/createHexSticker.R
%doc %{rlibdir}/%{packname}/figures
%{rlibdir}/%{packname}/INDEX
