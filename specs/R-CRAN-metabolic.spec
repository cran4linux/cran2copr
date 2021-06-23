%global __brp_check_rpaths %{nil}
%global packname  metabolic
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Datasets and Functions for Reproducing Meta-Analyses

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-meta >= 4.11.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-cli >= 2.0.1
BuildRequires:    R-CRAN-tidyr >= 1.0.2
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-patchwork >= 1.0.0
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-ggfittext 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggimage 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-meta >= 4.11.0
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-cli >= 2.0.1
Requires:         R-CRAN-tidyr >= 1.0.2
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-patchwork >= 1.0.0
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-ggfittext 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggimage 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-rmarkdown 

%description
Dataset and functions from the meta-analysis published in Medicine &
Science in Sports & Exercise. It contains all the data and functions to
reproduce the analysis. "Effectiveness of HIIE versus MICT in Improving
Cardiometabolic Risk Factors in Health and Disease: A Meta-analysis".
Felipe Mattioni Maturana, Peter Martus, Stephan Zipfel, Andreas M Nieß
(2020) <doi:10.1249/MSS.0000000000002506>.

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
