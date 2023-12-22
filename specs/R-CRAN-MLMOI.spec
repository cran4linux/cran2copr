%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MLMOI
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Frequencies, Prevalence and Multiplicity of Infection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.2.5.2
BuildRequires:    R-CRAN-Rdpack >= 2.6
BuildRequires:    R-CRAN-Rmpfr >= 0.9.3
Requires:         R-CRAN-openxlsx >= 4.2.5.2
Requires:         R-CRAN-Rdpack >= 2.6
Requires:         R-CRAN-Rmpfr >= 0.9.3

%description
The implemented methods reach out to scientists that seek to estimate
multiplicity of infection (MOI) and lineage (allele) frequencies and
prevalences at molecular markers using the maximum-likelihood method
described in Schneider (2018) <doi:10.1371/journal.pone.0194148>, and
Schneider and Escalante (2014) <doi:10.1371/journal.pone.0097899>. Users
can import data from Excel files in various formats, and perform
maximum-likelihood estimation on the imported data by the package's
moimle() function.

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
