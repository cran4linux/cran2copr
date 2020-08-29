%global packname  rsnps
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Get 'SNP' ('Single-Nucleotide' 'Polymorphism') Data on the Web

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crul >= 0.5.2
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-crul >= 0.5.2
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-httr 

%description
A programmatic interface to various 'SNP' 'datasets' on the web: 'OpenSNP'
(<https://opensnp.org>), and 'NBCIs' 'dbSNP' database
(<https://www.ncbi.nlm.nih.gov/projects/SNP/>). Functions are included for
searching for 'NCBI'. For 'OpenSNP', functions are included for getting
'SNPs', and data for 'genotypes', 'phenotypes', annotations, and bulk
downloads of data by user.

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
