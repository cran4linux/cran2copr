%global packname  Hmisc
%global packver   4.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.4.1
Release:          1%{?dist}
Summary:          Harrell Miscellaneous

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-survival >= 3.1.6
BuildRequires:    R-CRAN-ggplot2 >= 2.2
BuildRequires:    R-CRAN-htmlTable >= 1.11.0
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-cluster 
BuildRequires:    R-rpart 
BuildRequires:    R-nnet 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-survival >= 3.1.6
Requires:         R-CRAN-ggplot2 >= 2.2
Requires:         R-CRAN-htmlTable >= 1.11.0
Requires:         R-lattice 
Requires:         R-CRAN-Formula 
Requires:         R-methods 
Requires:         R-CRAN-latticeExtra 
Requires:         R-cluster 
Requires:         R-rpart 
Requires:         R-nnet 
Requires:         R-foreign 
Requires:         R-CRAN-gtable 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-base64enc 

%description
Contains many functions useful for data analysis, high-level graphics,
utility operations, functions for computing sample size and power,
importing and annotating datasets, imputing missing values, advanced table
making, variable clustering, character string manipulation, conversion of
R objects to LaTeX and html code, and recoding variables.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
