%global packname  misty
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Miscellaneous Functions 'T. Yanagida'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.3
Requires:         R-core >= 3.3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-readxl 

%description
Miscellaneous functions for descriptive statistics (e.g., frequency table,
cross tabulation, multilevel descriptive statistics, coefficient alpha and
omega, and various effect size measures), missing data (e.g., descriptive
statistics for missing data, missing data pattern and auxiliary variable
analysis), data management (e.g., reading and writing SPSS and Excel
files, grand-mean and group-mean centering, recode variables and reverse
code items, and scale and group scores), and statistical analysis (e.g.,
confidence intervals, Levene's test, z-test, and sample size
determination).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
