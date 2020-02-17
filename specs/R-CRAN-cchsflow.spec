%global packname  cchsflow
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}
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
Variable transformation and harmonization of the Canadian Community Health
Survey (CCHS) from 2001 to 2014. This is useful for researchers interested
in using Canadian population health data across multiple years as it helps
combine variables. This package relies on rec_with_table() which was based
off 'sjmisc' rec(). Lüdecke D (2018). "sjmisc: Data and Variable
Transformation Functions". Journal of Open Source Software, 3(26), 754.
<doi:10.21105/joss.00754>.

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
