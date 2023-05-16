%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GWASinspector
%global packver   1.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.4
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive and Easy to Use Quality Control of GWAS Results

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.0
BuildRequires:    R-tools >= 3.0
BuildRequires:    R-CRAN-ggplot2 >= 3.0
BuildRequires:    R-CRAN-hash >= 2.2
BuildRequires:    R-CRAN-rmarkdown >= 2.17
BuildRequires:    R-CRAN-futile.logger >= 1.4
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-knitr >= 1.1
BuildRequires:    R-CRAN-kableExtra >= 0.8
BuildRequires:    R-CRAN-ini >= 0.3
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R.utils 
Requires:         R-CRAN-openxlsx >= 4.0
Requires:         R-tools >= 3.0
Requires:         R-CRAN-ggplot2 >= 3.0
Requires:         R-CRAN-hash >= 2.2
Requires:         R-CRAN-rmarkdown >= 2.17
Requires:         R-CRAN-futile.logger >= 1.4
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-knitr >= 1.1
Requires:         R-CRAN-kableExtra >= 0.8
Requires:         R-CRAN-ini >= 0.3
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-RSQLite 
Requires:         R-methods 
Requires:         R-CRAN-R.utils 

%description
When evaluating the results of a genome-wide association study (GWAS), it
is important to perform a quality control to ensure that the results are
valid, complete, correctly formatted, and, in case of meta-analysis,
consistent with other studies that have applied the same analysis. This
package was developed to facilitate and streamline this process and
provide the user with a comprehensive report.

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
