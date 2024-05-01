%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  karlen
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Real-Time PCR Data Sets by Karlen et al. (2007)

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
Karlen et al. (2007) <doi:10.1186/1471-2105-8-131>. Provides one single
tabular tidy data set in long format, encompassing 32 dilution series, for
seven PCR targets and four biological samples. The targeted amplicons are
within the murine genes: Cav1, Ccn2, Eln, Fn1, Rpl27, Hspg2, and Serpine1,
respectively. Dilution series: scheme 1 (Cav1, Eln, Hspg2, Serpine1):
1-fold, 10-fold, 50-fold, and 100-fold; scheme 2 (Ccn2, Rpl27, Fn1):
1-fold, 10-fold, 50-fold, 100-fold and 1000-fold. For each concentration
there are five replicates, except for the 1000-fold concentration, where
only two replicates were performed. Each amplification curve is 40 cycles
long. Original raw data file is Additional file 2 from "Statistical
significance of quantitative PCR" by Y. Karlen, A. McNair, S. Perseguers,
C. Mazza, and N. Mermod (2007)
<https://static-content.springer.com/esm/art%%3A10.1186%%2F1471-2105-8-131/MediaObjects/12859_2006_1503_MOESM2_ESM.ZIP>.

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
