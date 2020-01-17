%global packname  gen5helper
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Processing 'Gen5' 2.06 Exported Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-naturalsort 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-CRAN-naturalsort 
Requires:         R-CRAN-rlang 

%description
A collection of functions for processing 'Gen5' 2.06 exported data. 'Gen5'
is an essential data analysis software for BioTek plate readers
<https://www.biotek.com/products/software-robotics-software/gen5-microplate-reader-and-imager-software/>.
This package contains functions for data cleaning, modeling and plotting
using exported data from 'Gen5' version 2.06. It exports technically
correct data defined in (Edwin de Jonge and Mark van der Loo (2013)
<https://cran.r-project.org/doc/contrib/de_Jonge+van_der_Loo-Introduction_to_data_cleaning_with_R.pdf>)
for customized analysis. It contains Boltzmann fitting for general kinetic
analysis. See <https://www.github.com/yanxianUCSB/gen5helper> for more
information, documentation and examples.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
