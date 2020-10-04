%global packname  CONCUR
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Copy Number Profile Curve-Based Association Test

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-mgcv 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-dplyr 
Requires:         R-mgcv 

%description
Implements a kernel-based association test for copy number variation (CNV)
aggregate analysis in a certain genomic region (e.g., gene set,
chromosome, or genome) that is robust to the within-locus and across-locus
etiological heterogeneity, and bypass the need to define a "locus" unit
for CNVs. Brucker, A., et al. (2020) <doi:10.1101/666875>.

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
