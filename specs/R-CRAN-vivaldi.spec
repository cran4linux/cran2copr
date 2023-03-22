%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vivaldi
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Viral Variant Location and Diversity

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-seqinr >= 4.2.8
BuildRequires:    R-CRAN-plotly >= 4.10.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-glue >= 1.4.2
BuildRequires:    R-CRAN-vcfR >= 1.12.0
BuildRequires:    R-CRAN-tidyr >= 1.1.2
BuildRequires:    R-CRAN-tidyselect >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-seqinr >= 4.2.8
Requires:         R-CRAN-plotly >= 4.10.0
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-glue >= 1.4.2
Requires:         R-CRAN-vcfR >= 1.12.0
Requires:         R-CRAN-tidyr >= 1.1.2
Requires:         R-CRAN-tidyselect >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.0.2

%description
Analysis of minor alleles in Illumina sequencing data of viral genomes.
Functions in 'vivaldi' primarily operate on vcf files.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
