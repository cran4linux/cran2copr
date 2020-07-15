%global packname  texreg
%global packver   1.37.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.37.5
Release:          3%{?dist}
Summary:          Conversion of R Regression Output to LaTeX or HTML Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-httr 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-httr 

%description
Converts coefficients, standard errors, significance stars, and
goodness-of-fit statistics of statistical models into LaTeX tables or HTML
tables/MS Word documents or to nicely formatted screen output for the R
console for easy model comparison. A list of several models can be
combined in a single table. The output is highly customizable. New model
types can be easily implemented. (If the Zelig package, which this package
enhances, cannot be found on CRAN, you can find it at
<https://github.com/IQSS/Zelig>.)

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
