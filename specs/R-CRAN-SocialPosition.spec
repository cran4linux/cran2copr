%global packname  SocialPosition
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Social Position Indicators Construction Toolbox

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides to sociologists (and related scientists) a toolbox to facilitate
the construction of social position indicators from survey data. Social
position indicators refer to what is commonly known as social class and
social status. There exists in the sociological literature many
theoretical conceptualisation and empirical operationalization of social
class and social status. This first version of the package offers tools to
construct the International Socio-Economic Index of Occupational Status
(ISEI) and the Oesch social class schema. It also provides tools to
convert several occupational classifications (PCS82, PCS03, and ISCO08)
into a common one (ISCO88) to facilitate data harmonisation work, and
tools to collapse (i.e. group) modalities of social position indicators.

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
