%global packname  iq
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          2%{?dist}%{?buildtag}
Summary:          Protein Quantification in Mass Spectrometry-Based Proteomics

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10

%description
An implementation of the maximal peptide ratio extraction module of the
MaxLFQ algorithm by Cox et al. (2014) <doi:10.1074/mcp.M113.031591> in a
complete pipeline for processing proteomics data in data-independent
acquisition mode (Pham et al. 2020 <doi:10.1093/bioinformatics/btz961>).
It offers additional options for protein quantification using the N most
intense fragment ions, using all fragment ions, and a wrapper for the
median polish algorithm by Tukey (1977, ISBN:0201076160).

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
