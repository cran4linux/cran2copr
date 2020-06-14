%global packname  cchsflow
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          2%{?dist}
Summary:          Transforming and Harmonizing CCHS Variables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-haven >= 1.1.2
BuildRequires:    R-CRAN-sjlabelled >= 1.0.17
BuildRequires:    R-CRAN-dplyr >= 0.8.2
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-haven >= 1.1.2
Requires:         R-CRAN-sjlabelled >= 1.0.17
Requires:         R-CRAN-dplyr >= 0.8.2
Requires:         R-CRAN-magrittr 

%description
Supporting the use of the Canadian Community Health Survey (CCHS) by
transforming variables from each cycle into harmonized, consistent
versions that span survey cycles (currently, 2001 to 2014). CCHS data used
in this library is accessed and adapted in accordance to the Statistics
Canada Open Licence Agreement. This package uses rec_with_table(), which
was developed from 'sjmisc' rec(). Lüdecke D (2018). "sjmisc: Data and
Variable Transformation Functions". Journal of Open Source Software,
3(26), 754. <doi:10.21105/joss.00754>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
