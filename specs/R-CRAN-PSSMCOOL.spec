%global __brp_check_rpaths %{nil}
%global packname  PSSMCOOL
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Features Extracted from Position Specific Scoring Matrix (PSSM)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-phonTools 
BuildRequires:    R-CRAN-dtt 
Requires:         R-utils 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-phonTools 
Requires:         R-CRAN-dtt 

%description
Returns almost all features that has been extracted from Position Specific
Scoring Matrix (PSSM) so far, which is a matrix of L rows (L is protein
length) and 20 columns produced by 'PSI-BLAST' which is a program to
produce PSSM Matrix from multiple sequence alignment of proteins see
<https://www.ncbi.nlm.nih.gov/books/NBK2590/> for mor details. some of
these features are described in Zahiri, J., et al.(2013)
<DOI:10.1016/j.ygeno.2013.05.006>, Saini, H., et al.(2016)
<DOI:10.17706/jsw.11.8.756-767>, Ding, S., et al.(2014)
<DOI:10.1016/j.biochi.2013.09.013>, Cheng, C.W., et al.(2008)
<DOI:10.1186/1471-2105-9-S12-S6>, Juan, E.Y., et al.(2009)
<DOI:10.1109/CISIS.2009.194>.

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
