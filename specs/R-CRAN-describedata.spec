%global __brp_check_rpaths %{nil}
%global packname  describedata
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Miscellaneous Descriptive Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-rlang 

%description
Helper functions for descriptive tasks such as making print-friendly
bivariate tables, sample size flow counts, and visualizing sample
distributions. Also contains 'R' approximations of some common 'SAS' and
'Stata' functions such as 'PROC MEANS' from 'SAS' and 'ladder', 'gladder',
and 'pwcorr' from 'Stata'.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
