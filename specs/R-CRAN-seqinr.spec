%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  seqinr
%global packver   4.2-36
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.36
Release:          1%{?dist}%{?buildtag}
Summary:          Biological Sequences Retrieval and Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-segmented 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-segmented 

%description
Exploratory data analysis and data visualization for biological sequence
(DNA and protein) data. Seqinr includes utilities for sequence data
management under the ACNUC system described in Gouy, M. et al. (1984)
Nucleic Acids Res. 12:121-127 <doi:10.1093/nar/12.1Part1.121>.

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
