%global packname  GPSCDF
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Generalized Propensity Score Cumulative Distribution Function

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.49
BuildRequires:    R-nnet >= 7.3.12
BuildRequires:    R-stats >= 3.4
BuildRequires:    R-utils >= 3.4
BuildRequires:    R-survival >= 2.41.3
BuildRequires:    R-CRAN-nbpMatching >= 1.5.1
BuildRequires:    R-CRAN-dplyr >= 0.7.6
Requires:         R-MASS >= 7.3.49
Requires:         R-nnet >= 7.3.12
Requires:         R-stats >= 3.4
Requires:         R-utils >= 3.4
Requires:         R-survival >= 2.41.3
Requires:         R-CRAN-nbpMatching >= 1.5.1
Requires:         R-CRAN-dplyr >= 0.7.6

%description
Implements the generalized propensity score cumulative distribution
function proposed by Greene (2017)
<https://digitalcommons.library.tmc.edu/dissertations/AAI10681743/>. A
single scalar balancing score is calculated for any generalized propensity
score vector with three or more treatments. This balancing score is used
for propensity score matching and stratification in outcome analyses when
analyzing either ordinal or multinomial treatments.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
