%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OryzaProbe
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rice Microarray Probe ID Conversion, from Probe ID to RAP-DB ID

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Microarray probe ID is not convenient for further enrichment analysis and
target gene selection. The package is created for the rice microarray
probe ID conversion. This package can convert microarray probe ID from
GPL6864 <https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL6864>,
GPL8852 <https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL8852>, and
GPL2025 <https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL2025>
platforms to RAP-DB ID. RAP-DB "The Rice Annotation Project Database"
<https://rapdb.dna.affrc.go.jp> is a well-known database for rice Oryza
sativa, and the gene ID in this database is widely used in many areas
related to rice research. For multiple probes representing a single gene,
This package can merge them by taking the mean, max, or min value of these
probes. Or we can keep multiple probes by appending sequence numbers to
duplicate the RAP-DB ID.

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
