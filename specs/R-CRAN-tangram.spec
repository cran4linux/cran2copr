%global packname  tangram
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          3%{?dist}
Summary:          The Grammar of Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-htmltools 

%description
Provides an extensible formula system to quickly and easily create
production quality tables. The steps of the process are formula parser,
statistical content generation from data, to rendering. Each step of the
process is separate and user definable thus creating a set of building
blocks for highly extensible table generation. A user is not limited by
any of the choices of the package creator other than the formula grammar.
For example, one could chose to add a different S3 rendering function and
output a format not provided in the default package. Or possibly one would
rather have Gini coefficients for their statistical content. Routines to
achieve New England Journal of Medicine style, Lancet style and
Hmisc::summaryM() statistics are provided. The package contains rendering
for HTML5, Rmarkdown and an indexing format for use in tracing and
tracking are provided.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
