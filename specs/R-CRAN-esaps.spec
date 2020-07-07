%global packname  esaps
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Indicators of Electoral Systems and Party Systems

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-readODS >= 1.6.4
BuildRequires:    R-CRAN-readxl >= 1.0.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-readODS >= 1.6.4
Requires:         R-CRAN-readxl >= 1.0.0

%description
It allows to construct two types of indicators used in the study of
Electoral Systems and Party Systems starting from electoral results data.
The Effective Number of Parties (Laakso and Taagepera (1979)
<doi:10.1177/001041407901200101>) and Electoral Volatility in its three
versions (Pedersen (1979) <doi:10.1111/j.1475-6765.1979.tb01267.x>, Powell
and Tucker (2014) <doi:10.1017/S0007123412000531> and Torcal and Lago
(2015, ISBN:9788415260356)).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
