%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vermeulen
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Biomarker Data Set by Vermeulen et al. (2009)

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-memoise 
Requires:         R-CRAN-memoise 

%description
The biomarker data set by Vermeulen et al. (2009)
<doi:10.1016/S1470-2045(09)70154-8> is provided. The data source, however,
is by Ruijter et al. (2013) <doi:10.1016/j.ymeth.2012.08.011>. The
original data set may be downloaded from
<https://medischebiologie.nl/wp-content/uploads/2019/02/qpcrdatamethods.zip>.
This data set is for a real-time quantitative polymerase chain reaction
(PCR) experiment that comprises the raw fluorescence data of 24,576
amplification curves. This data set comprises 59 genes of interest and 5
reference genes. Each gene was assessed on 366 neuroblastoma complementary
DNA (cDNA) samples and on 18 standard dilution series samples (10-fold
5-point dilution series x 3 replicates + no template controls (NTC) x 3
replicates).

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
