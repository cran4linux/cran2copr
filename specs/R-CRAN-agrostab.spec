%global packname  agrostab
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Stability Analysis for Agricultural Research

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-rlang 

%description
Statistical procedures to perform stability analysis in plant breeding and
to identify stable genotypes under diverse environments. It is possible to
calculate coefficient of homeostaticity by Khangildin et al. (1979),
variance of specific adaptive ability by Kilchevsky&Khotyleva (1989),
weighted homeostaticity index by Martynov (1990), steadiness of stability
index by Udachin (1990), superiority measure by Lin&Binn (1988)
<doi:10.4141/cjps88-018>, regression on environmental index by
Erberhart&Rassel (1966) <doi:10.2135/cropsci1966.0011183X000600010011x>,
Tai's (1971) stability parameters
<doi:10.2135/cropsci1971.0011183X001100020006x>, stability variance by
Shukla (1972) <doi:10.1038/hdy.1972.87>, ecovalence by Wricke (1962),
nonparametric stability parameters by Nassar&Huehn (1987)
<doi:10.2307/2531947>, Francis&Kannenberg's parameters of stability (1978)
<doi:10.4141/cjps78-157>.

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
