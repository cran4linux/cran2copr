%global packname  psidR
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          2%{?dist}
Summary:          Build Panel Data Sets from PSID Raw Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-SAScii 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-futile.logger 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-RCurl 
Requires:         R-foreign 
Requires:         R-CRAN-SAScii 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-futile.logger 

%description
Makes it easy to build panel data in wide format from Panel Survey of
Income Dynamics ('PSID') delivered raw data. Downloads data directly from
the PSID server using the 'SAScii' package. 'psidR' takes care of merging
data from each wave onto a cross-period index file, so that individuals
can be followed over time. The user must specify which years they are
interested in, and the 'PSID' variable names (e.g. ER21003) for each year
(they differ in each year). The package offers helper functions to
retrieve variable names from different waves. There are different panel
data designs and sample subsetting criteria implemented ("SRC", "SEO",
"immigrant" and "latino" samples).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/psid-lists
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
