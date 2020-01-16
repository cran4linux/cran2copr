%global packname  SMARTAR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Sequential Multiple Assignment Randomized Trial and AdaptiveRandomization

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-MASS 

%description
Primary data analysis for sequential multiple assignment randomization
trial (SMART) and calibration tools for clinical trial planning purposes.
The methods used for this package include: (1) Likelihood-based global
test (hypothesis test, power calculation) by in Zhong X., Cheng, B., Qian
M., Cheung Y.K. (2019) <doi:10.1016/j.cct.2019.105830>. (2) IPWE-based
global test (hypotehsis test, power calculation) by Ogbagaber S.B., Karp
J., Wahed A.S. (2016) <doi:10.1002/sim.6747>. (3) G estimates (pairwise
comparison, power calculation) by Lavori R., Dawson P.W. (2012)
<doi:10.1093/biostatistics/kxr016>. (4) IPW estimates (pairwise
comparison, power calculation) by Murphy S.A. (2005)
<doi:10.1002/sim.2022>. (5) SAMRT with adaptive randomization by Cheung
Y.K. (2015) <doi:10.1111/biom.12258>.

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
