%global packname  litteR
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Litter Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-yaml >= 2.2.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-fs >= 1.3.1
BuildRequires:    R-CRAN-rmarkdown >= 1.14
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-tcltk 
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-yaml >= 2.2.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-fs >= 1.3.1
Requires:         R-CRAN-rmarkdown >= 1.14
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-tcltk 

%description
Data sets on various litter types like beach litter, riverain litter,
floating litter, and seafloor litter are rapidly growing. This package
offers a simple user interface to analyse these litter data in a
consistent and reproducible way. It also provides functions to facilitate
several kinds of litter analysis, e.g., trend analysis, power analysis,
and baseline analysis. Under the hood, these functions are also used by
the user interface. See Schulz et al. (2019)
<doi:10.1016/j.envpol.2019.02.030> for details.

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
%doc %{rlibdir}/%{packname}/app
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
