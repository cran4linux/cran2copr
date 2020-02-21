%global packname  RMixpanel
%global packver   0.7-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}
Summary:          API for Mixpanel

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-base64enc 

%description
Provides an interface to many endpoints of Mixpanel's Data Export, Engage
and JQL API. The R functions allow for event and profile data export as
well as for segmentation, retention, funnel and addiction analysis.
Results are always parsed into convenient R objects. Furthermore it is
possible to load and update profiles.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
