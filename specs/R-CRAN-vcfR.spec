%global packname  vcfR
%global packver   1.11.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11.0
Release:          1%{?dist}
Summary:          Manipulate and Visualize VCF Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    devscripts-checkbashisms
BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-memuse 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pinfsc50 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-memuse 
Requires:         R-methods 
Requires:         R-CRAN-pinfsc50 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-viridisLite 

%description
Facilitates easy manipulation of variant call format (VCF) data. Functions
are provided to rapidly read from and write to VCF files. Once VCF data is
read into R a parser function extracts matrices of data. This information
can then be used for quality control or other purposes. Additional
functions provide visualization of genomic data. Once processing is
complete data may be written to a VCF file (*.vcf.gz). It also may be
converted into other popular R objects (e.g., genlight, DNAbin). VcfR
provides a link between VCF data and familiar R software.

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

%files
%{rlibdir}/%{packname}
