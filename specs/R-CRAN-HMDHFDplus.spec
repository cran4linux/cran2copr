%global __brp_check_rpaths %{nil}
%global packname  HMDHFDplus
%global packver   1.9.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.13
Release:          3%{?dist}%{?buildtag}
Summary:          Read Human Mortality Database and Human Fertility Database Datafrom the Web

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-httr 

%description
Utilities for reading data from the Human Mortality Database
(<https://www.mortality.org>), Human Fertility Database
(<https://www.humanfertility.org>), and similar databases from the web or
locally into an R session as data.frame objects. These are the two most
widely used sources of demographic data to study basic demographic change,
trends, and develop new demographic methods. Other supported databases at
this time include the Human Fertility Collection
(<http://www.fertilitydata.org/>), The Japanese Mortality Database
(<http://www.ipss.go.jp/p-toukei/JMD>), and the Canadian Human Mortality
Database (<http://www.bdlc.umontreal.ca/chmd/>). Arguments and data are
standardized.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
