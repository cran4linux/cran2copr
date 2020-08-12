%global packname  KnockoffScreen
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Whole-Genome Sequencing Data Analysis via Knockoff Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-seqminer 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-SPAtest 
Requires:         R-Matrix 
Requires:         R-CRAN-seqminer 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-SPAtest 

%description
Functions for identification of putative causal loci in whole-genome
sequencing data. The functions allow genome-wide association scan. It also
includes an efficient knockoff generator for genetic data.

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
