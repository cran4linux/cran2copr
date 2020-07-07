%global packname  misty
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          2%{?dist}
Summary:          Miscellaneous Functions 'T. Yanagida'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.3
Requires:         R-core >= 3.3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-readxl 

%description
Miscellaneous functions for descriptive statistics (e.g., frequency table,
cross tabulation, multilevel descriptive statistics, coefficient alpha and
omega, and various effect size measures), missing data (e.g., descriptive
statistics for missing data, missing data pattern and auxiliary variable
analysis), data management (e.g., grand-mean and group-mean centering,
recode variables and reverse code items, scale and group scores, reading
and writing SPSS and Excel files), and statistical analysis (e.g.,
confidence intervals, collinearity diagnostics, Levene's test, z-test, and
sample size determination).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
