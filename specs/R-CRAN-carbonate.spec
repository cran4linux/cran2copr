%global __brp_check_rpaths %{nil}
%global packname  carbonate
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Interact with 'carbon.js'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-details 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-RSelenium 
BuildRequires:    R-CRAN-rtweet 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-wdman 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-details 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-RSelenium 
Requires:         R-CRAN-rtweet 
Requires:         R-utils 
Requires:         R-CRAN-wdman 
Requires:         R-CRAN-yaml 

%description
Create beautiful images of source code using
'carbon.js'<https://carbon.now.sh/about>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/figures
%{rlibdir}/%{packname}/INDEX
