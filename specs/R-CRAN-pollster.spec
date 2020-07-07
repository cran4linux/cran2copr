%global packname  pollster
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          Calculate Crosstab and Topline Tables of Weighted Survey Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-labelled >= 2.0.0
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-forcats 
Requires:         R-CRAN-labelled >= 2.0.0
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-forcats 

%description
Calculate common types of tables for weighted survey data. Options include
topline and (2-way and 3-way) crosstab tables of categorical or ordinal
data as well as summary tables of weighted numeric variables. Optionally,
include the margin of error at selected confidence intervals including the
design effect. The design effect is calculated as described by Kish (1965)
<doi:10.1002/bimj.19680100122> beginning on page 257. Output takes the
form of tibbles (simple data frames). This package conveniently handles
labelled data, such as that commonly used by 'Stata' and 'SPSS.' Complex
survey design is not supported at this time.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
