%global packname  forestmangr
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}
Summary:          Functions for Forest Mensuration and Management

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-systemfit 
BuildRequires:    R-CRAN-ggpmisc 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-FinCal 
BuildRequires:    R-CRAN-formattable 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 >= 2.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-systemfit 
Requires:         R-CRAN-ggpmisc 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-car 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-FinCal 
Requires:         R-CRAN-formattable 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-gridExtra 

%description
Set of functions for processing forest inventory data with methods such as
simple random sampling, stratified random sampling and systematic
sampling. There are also functions for yield and growth predictions and
model fitting, linear and non linear grouped data fitting, and statistical
tests.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
