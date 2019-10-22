%global packname  RAdwords
%global packver   0.1.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.18
Release:          1%{?dist}
Summary:          Loading Google Adwords Data into R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rjson 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rjson 

%description
Aims at loading Google Adwords data into R. Adwords is an online
advertising service that enables advertisers to display advertising copy
to web users (see <https://developers.google.com/adwords/> for more
information). Therefore the package implements three main features. First,
the package provides an authentication process for R with the Google
Adwords API (see <https://developers.google.com/adwords/api/> for more
information) via OAUTH2. Second, the package offers an interface to apply
the Adwords query language in R and query the Adwords API with ad-hoc
reports. Third, the received data are transformed into suitable data
formats for further data processing and data analysis.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
