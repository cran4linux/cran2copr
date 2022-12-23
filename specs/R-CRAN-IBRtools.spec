%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IBRtools
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Integrating Biomarker-Based Assessments and Radarchart Creation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.9
BuildRequires:    R-CRAN-tibble >= 3.0.4
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.13.2
BuildRequires:    R-CRAN-tidyr >= 1.1.3
BuildRequires:    R-CRAN-dplyr >= 1.0.6
BuildRequires:    R-CRAN-binhf >= 1.0.3
BuildRequires:    R-CRAN-fmsb >= 0.7.1
Requires:         R-CRAN-gtools >= 3.9
Requires:         R-CRAN-tibble >= 3.0.4
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-data.table >= 1.13.2
Requires:         R-CRAN-tidyr >= 1.1.3
Requires:         R-CRAN-dplyr >= 1.0.6
Requires:         R-CRAN-binhf >= 1.0.3
Requires:         R-CRAN-fmsb >= 0.7.1

%description
Several functions to calculate two important indexes (IBR (Integrated
Biomarker Response) and IBRv2 (Integrated Biological Response version 2)),
it also calculates the standardized values for enzyme activity for each
index, and it has a graphing function to perform radarplots that make
great data visualization for this type of data. Beliaeff, B., & Burgeot,
T. (2002). <https://pubmed.ncbi.nlm.nih.gov/12069320/>. Sanchez, W.,
Burgeot, T., & Porcher, J.-M. (2013).<doi:10.1007/s11356-012-1359-1>.
Devin, S., Burgeot, T., Giambérini, L., Minguez, L., & Pain-Devin, S.
(2014). <doi:10.1007/s11356-013-2169-9>. Minato N. (2022).
<https://minato.sip21c.org/msb/>.

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
