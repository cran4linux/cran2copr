%global __brp_check_rpaths %{nil}
%global packname  eemR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Pre-Processing Emission-Excitation-Matrix (EEM)Fluorescence Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-R.matlab 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-R.matlab 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-assertthat 

%description
Provides various tools for preprocessing Emission-Excitation-Matrix (EEM)
for Parallel Factor Analysis (PARAFAC). Different methods are also
provided to calculate common metrics such as humification index and
fluorescence index.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
