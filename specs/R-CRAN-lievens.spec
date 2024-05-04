%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lievens
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Real-Time PCR Data Sets by Lievens et al. (2012)

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-tibble 

%description
Real-time quantitative polymerase chain reaction (qPCR) data sets by
Lievens et al. (2012) <doi:10.1093/nar/gkr775>. Provides one single
tabular tidy data set in long format, encompassing three dilution series,
targeted against the soybean Lectin endogene. Each dilution series was
assayed in one of the following PCR-efficiency-modifying conditions: no
PCR inhibition, inhibition by isopropanol and inhibition by tannic acid.
The inhibitors were co-diluted along with the dilution series. The
co-dilution series consists of a five-point, five-fold serial dilution.
For each concentration there are 18 replicates. Each amplification curve
is 60 cycles long. Original raw data file is available at the
Supplementary Data section at Nucleic Acids Research Online
<doi:10.1093/nar/gkr775>.

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
